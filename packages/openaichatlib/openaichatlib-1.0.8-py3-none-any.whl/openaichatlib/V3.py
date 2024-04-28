"""
A simple wrapper for the official ChatGPT API
"""
import json
import os
from pathlib import Path
from typing import AsyncGenerator
from typing import Optional

import httpx
import requests
import tiktoken

from . import typings as t
from .utils import get_filtered_keys_from_object

ENGINES_CLAUDE_MAX = [
    "claude-3-opus-20240229",
    "claude-3-sonnet-20240229",
    "claude-3-haiku-20240307",
    "claude-2.1",
]

ENGINES_CLAUDE_LOW = [
    "claude-2.0",
    "claude-instant-1.2",
]

ENGINES_CLAUDE = [
    *ENGINES_CLAUDE_MAX,

    *ENGINES_CLAUDE_LOW,
]

ENGINES_GPT35_TURBO = [
    "gpt-3.5-turbo-0125",
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-1106",
]

ENGINES_GPT35_16K = [
    "gpt-3.5-turbo-16k",
    "gpt-3.5-turbo-16k-0613",
]

ENGINES_GPT4 = [
    "gpt-4",
    "gpt-4-0613",
]

ENGINES_GPT4_32K = [
    "gpt-4-32k",
    "gpt-4-32k-0613",
]

ENGINES_PREVIEW = [
    "gpt-4-0125-preview",
    "gpt-4-turbo-preview",
    "gpt-4-1106-preview",
    "gpt-4-vision-preview",
    "gpt-4-1106-vision-preview",
]

ENGINES = [
    "gpt-3.5-turbo-instruct",
    "gpt-3.5-turbo-0613",

    *ENGINES_GPT35_TURBO,
    *ENGINES_GPT35_16K,

    *ENGINES_GPT4,
    *ENGINES_GPT4_32K,

    *ENGINES_PREVIEW,
    *ENGINES_CLAUDE,
]


class Chatbot:
    """
    Official ChatGPT API
    """

    def __init__(
            self,
            api_key: str,
            api_url: str = os.environ.get("API_URL") or "https://api.openai.com/v1/chat/completions",
            engine: str = os.environ.get("GPT_ENGINE") or "gpt-3.5-turbo",
            proxy: str = None,
            timeout: float = None,
            max_tokens: int = None,
            customize_header: dict = None,
            temperature: float = 0.5,
            top_p: float = 1.0,
            reply_count: int = 1,
            truncate_limit: int = None,
            system_prompt: str = "You are ChatGPT, a large language model trained by OpenAI. Respond conversationally",
            count_tokens: bool = True,
    ) -> None:
        """
        Initialize Chatbot with API key (from https://platform.openai.com/account/api-keys)
        """
        self.api_url: str = api_url
        self.engine: str = engine
        self.api_key: str = api_key
        self.customize_header = customize_header
        self.system_prompt: str = system_prompt
        self.count_tokens = count_tokens
        self.max_tokens: int = max_tokens or (
            16_000
            if engine in ENGINES_GPT35_TURBO
            else 120_000
            if engine in ENGINES_PREVIEW
            else 32_000
            if engine in ENGINES_GPT4_32K
            else 8_000
            if engine in ENGINES_GPT4
            else 200_000
            if engine in ENGINES_CLAUDE_MAX
            else 100_000
            if engine in ENGINES_CLAUDE_LOW
            else 4_000
        )
        self.truncate_limit: int = truncate_limit or (
            15_500
            if engine in ENGINES_GPT35_TURBO
            else 119_500
            if engine in ENGINES_PREVIEW
            else 31_500
            if engine in ENGINES_GPT4_32K
            else 7_500
            if engine in ENGINES_GPT4
            else 199_500
            if engine in ENGINES_CLAUDE_MAX
            else 99_500
            if engine in ENGINES_CLAUDE_LOW
            else 3_500
        )
        self.temperature: float = temperature
        self.top_p: float = top_p
        self.reply_count: int = reply_count
        self.timeout: float = timeout
        self.proxy = proxy
        self.session = requests.Session()
        self.session.proxies.update(
            {
                "http": proxy,
                "https": proxy,
            },
        )
        if proxy := (
                proxy or os.environ.get("all_proxy") or os.environ.get("ALL_PROXY") or None
        ):
            if "socks5h" not in proxy:
                self.aclient = httpx.AsyncClient(
                    follow_redirects=True,
                    proxies=proxy,
                    timeout=timeout,
                )
        else:
            self.aclient = httpx.AsyncClient(
                follow_redirects=True,
                proxies=proxy,
                timeout=timeout,
            )

        self.conversation: dict[str, list[dict]] = {
            "default": [
                {
                    "role": "system",
                    "content": system_prompt,
                },
            ],
        }

        # if self.get_token_count("default") > self.max_tokens:
        #     raise t.ActionRefuseError("System prompt is too long")

    def add_to_conversation(
            self,
            message,
            role: str,
            convo_id: str = "default",
    ) -> None:
        """
        Add a message to the conversation
        """
        self.conversation[convo_id].append({"role": role, "content": message})

    def __truncate_conversation(self, convo_id: str = "default") -> None:
        """
        Truncate the conversation
        """
        if not self.count_tokens:
            return
        if self.engine in ENGINES_CLAUDE:
            return
        while True:
            if (
                    self.get_token_count(convo_id) > self.truncate_limit
                    and len(self.conversation[convo_id]) > 1
            ):
                # Don't remove the first message
                self.conversation[convo_id].pop(1)
            else:
                break

    # https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
    def get_token_count(self, convo_id: str = "default") -> int:
        """
        Get token count
        """
        if not self.count_tokens:
            return 0
        if self.engine not in ENGINES:
            raise NotImplementedError(
                f"Engine {self.engine} is not supported. Select from {ENGINES}",
            )
        tiktoken.model.MODEL_TO_ENCODING["gpt-4"] = "cl100k_base"

        encoding = tiktoken.encoding_for_model(self.engine)

        num_tokens = 0
        for message in self.conversation[convo_id]:
            # every message follows <im_start>{role/name}\n{content}<im_end>\n
            num_tokens += 5
            for key, value in message.items():
                if isinstance(value, str):
                    num_tokens += len(encoding.encode(value))
                if isinstance(value, list):
                    for content in value:
                        try:
                            num_tokens += len(encoding.encode(content[content['type']]))
                        except Exception as e:
                            print(f"Warning: error count token type: {e}")
                if key == "name":  # if there's a name, the role is omitted
                    num_tokens += 5  # role is always required and always 1 token
        num_tokens += 5  # every reply is primed with <im_start>assistant
        return num_tokens

    def get_max_tokens(self, convo_id: str) -> Optional[int]:
        """
        Get max tokens
        """
        if not self.count_tokens:
            return None
        if self.engine in ENGINES_GPT35_TURBO or self.engine in ENGINES_PREVIEW or self.engine in ENGINES_CLAUDE:
            return 4096
        return self.max_tokens - self.get_token_count(convo_id)

    def ask_stream(
            self,
            prompt,
            role: str = "user",
            convo_id: str = "default",
            model: str = None,
            pass_history: bool = True,
            json_format: bool = False,
            stream: bool = True,
            **kwargs,
    ):
        """
        Ask a question
        """
        # Make conversation if it doesn't exist
        if convo_id not in self.conversation:
            self.reset(convo_id=convo_id, system_prompt=self.system_prompt)
        self.add_to_conversation(prompt, "user", convo_id=convo_id)
        self.__truncate_conversation(convo_id=convo_id)
        # Get response
        if os.environ.get("API_URL") and os.environ.get("MODEL_NAME"):
            # https://learn.microsoft.com/en-us/azure/cognitive-services/openai/chatgpt-quickstart?tabs=command-line&pivots=rest-api
            url = (
                    os.environ.get("API_URL")
                    + "openai/deployments/"
                    + os.environ.get("MODEL_NAME")
                    + "/chat/completions?api-version=2023-05-15"
            )
            headers = {"Content-Type": "application/json", "api-key": self.api_key}
        else:
            url = (
                self.api_url
            )
            headers = {"Authorization": f"Bearer {kwargs.get('api_key', self.api_key)}"}
        payload = {
            "model": os.environ.get("MODEL_NAME") or model or self.engine,
            "messages": self.conversation[convo_id] if pass_history else [prompt],
            "stream": stream,
            # kwargs
            "temperature": kwargs.get("temperature", self.temperature),
            "top_p": kwargs.get("top_p", self.top_p),
            "n": kwargs.get("n", self.reply_count),
        }
        max_tokens = kwargs.get("max_tokens", None) or self.get_max_tokens(convo_id=convo_id)
        if max_tokens:
            payload["max_tokens"] = max_tokens
        if json_format:
            payload["response_format"] = {
                "type": "json_object"
            }
        presence_penalty = kwargs.get("presence_penalty", None)
        if presence_penalty:
            payload["presence_penalty"] = presence_penalty
        frequency_penalty = kwargs.get("frequency_penalty", None)
        if frequency_penalty:
            payload["frequency_penalty"] = frequency_penalty
        user = kwargs.get("user", None)
        if user:
            payload["user"] = user
        if self.customize_header:
            headers.update(self.customize_header)
        response = self.session.post(
            url,
            headers=headers,
            json=payload,
            timeout=kwargs.get("timeout", self.timeout),
            stream=stream,
        )
        if response.status_code != 200:
            raise t.APIConnectionError(
                f"{response.status_code} {response.reason} {response.text}",
            )
        response_role: str = "assistant"
        full_response: str = ""
        if stream:
            for line in response.iter_lines():
                if not line:
                    continue
                # Remove "data: "
                line = line.decode("utf-8")[6:]
                if line == "[DONE]":
                    break
                resp: dict = json.loads(line)
                choices = resp.get("choices")
                if not choices:
                    continue
                delta = choices[0].get("delta")
                if not delta:
                    continue
                if "role" in delta:
                    response_role = delta["role"]
                if "content" in delta:
                    content = delta["content"]
                    full_response += content
                    yield content
        else:
            resp: dict = response.json()
            choices = resp.get("choices")
            delta = choices[0].get("message")
            response_role = delta["role"]
            content = delta["content"]
            full_response = content
            yield content
        self.add_to_conversation(full_response, response_role, convo_id=convo_id)

    async def ask_stream_async(
            self,
            prompt,
            role: str = "user",
            convo_id: str = "default",
            model: str = None,
            pass_history: bool = True,
            json_format: bool = False,
            **kwargs,
    ) -> AsyncGenerator[str, None]:
        """
        Ask a question
        """
        # Make conversation if it doesn't exist
        if convo_id not in self.conversation:
            self.reset(convo_id=convo_id, system_prompt=self.system_prompt)
        self.add_to_conversation(prompt, "user", convo_id=convo_id)
        self.__truncate_conversation(convo_id=convo_id)
        payload = {
            "model": model or self.engine,
            "messages": self.conversation[convo_id] if pass_history else [prompt],
            "stream": True,
            # kwargs
            "temperature": kwargs.get("temperature", self.temperature),
            "top_p": kwargs.get("top_p", self.top_p),
            "n": kwargs.get("n", self.reply_count),
        }
        max_tokens = kwargs.get("max_tokens", None) or self.get_max_tokens(convo_id=convo_id)
        if max_tokens:
            payload["max_tokens"] = max_tokens
        if json_format:
            payload["response_format"] = {
                "type": "json_object"
            }
        presence_penalty = kwargs.get("presence_penalty", None)
        if presence_penalty:
            payload["presence_penalty"] = presence_penalty
        frequency_penalty = kwargs.get("frequency_penalty", None)
        if frequency_penalty:
            payload["frequency_penalty"] = frequency_penalty
        user = kwargs.get("user", None)
        if user:
            payload["user"] = user
        headers = {"Authorization": f"Bearer {kwargs.get('api_key', self.api_key)}"}
        if self.customize_header:
            headers.update(self.customize_header)
        # Get response
        async with self.aclient.stream(
                "post",
                self.api_url,
                headers=headers,
                json=payload,
                timeout=kwargs.get("timeout", self.timeout),
        ) as response:
            if response.status_code != 200:
                await response.aread()
                raise t.APIConnectionError(
                    f"{response.status_code} {response.reason_phrase} {response.text}",
                )

            response_role: str = "assistant"
            full_response: str = ""
            async for line in response.aiter_lines():
                line = line.strip()
                if not line:
                    continue
                # Remove "data: "
                line = line[6:]
                if line == "[DONE]":
                    break
                resp: dict = json.loads(line)
                if "error" in resp:
                    raise t.ResponseError(f"{resp['error']}")
                choices = resp.get("choices")
                if not choices:
                    continue
                delta: dict[str, str] = choices[0].get("delta")
                if not delta:
                    continue
                if "role" in delta:
                    response_role = delta["role"]
                if "content" in delta:
                    content: str = delta["content"]
                    full_response += content
                    yield content
        self.add_to_conversation(full_response, response_role, convo_id=convo_id)

    async def ask_async(
            self,
            prompt,
            role: str = "user",
            convo_id: str = "default",
            model: str = None,
            pass_history: bool = True,
            json_format: bool = False,
            **kwargs,
    ) -> str:
        """
        Non-streaming ask
        """
        response = self.ask_stream_async(
            prompt=prompt,
            role=role,
            convo_id=convo_id,
            json_format=json_format,
            **kwargs,
        )
        full_response: str = "".join([r async for r in response])
        return full_response

    def ask(
            self,
            prompt,
            role: str = "user",
            convo_id: str = "default",
            model: str = None,
            pass_history: bool = True,
            json_format: bool = False,
            **kwargs,
    ) -> str:
        """
        Non-streaming ask
        """
        response = self.ask_stream(
            prompt=prompt,
            role=role,
            convo_id=convo_id,
            model=model,
            pass_history=pass_history,
            json_format=json_format,
            stream=False,
            **kwargs,
        )
        full_response: str = "".join(response)
        return full_response

    def rollback(self, n: int = 1, convo_id: str = "default") -> None:
        """
        Rollback the conversation
        """
        for _ in range(n):
            self.conversation[convo_id].pop()

    def reset(self, convo_id: str = "default", system_prompt: str = None) -> None:
        """
        Reset the conversation
        """
        self.conversation[convo_id] = [
            {"role": "system", "content": system_prompt or self.system_prompt},
        ]

    def save(self, file: str, *keys: str) -> None:
        """
        Save the Chatbot configuration to a JSON file
        """
        with open(file, "w", encoding="utf-8") as f:
            data = {
                key: self.__dict__[key]
                for key in get_filtered_keys_from_object(self, *keys)
            }
            # saves session.proxies dict as session
            # leave this here for compatibility
            data["session"] = data["proxy"]
            del data["aclient"]
            json.dump(
                data,
                f,
                indent=2,
            )

    def load(self, file: Path, *keys_: str) -> None:
        """
        Load the Chatbot configuration from a JSON file
        """
        with open(file, encoding="utf-8") as f:
            # load json, if session is in keys, load proxies
            loaded_config = json.load(f)
            keys = get_filtered_keys_from_object(self, *keys_)

            if (
                    "session" in keys
                    and loaded_config["session"]
                    or "proxy" in keys
                    and loaded_config["proxy"]
            ):
                self.proxy = loaded_config.get("session", loaded_config["proxy"])
                self.session = httpx.Client(
                    follow_redirects=True,
                    proxies=self.proxy,
                    timeout=self.timeout,
                    cookies=self.session.cookies,
                    headers=self.session.headers,
                )
                self.aclient = httpx.AsyncClient(
                    follow_redirects=True,
                    proxies=self.proxy,
                    timeout=self.timeout,
                    cookies=self.session.cookies,
                    headers=self.session.headers,
                )
            if "session" in keys:
                keys.remove("session")
            if "aclient" in keys:
                keys.remove("aclient")
            self.__dict__.update({key: loaded_config[key] for key in keys})
