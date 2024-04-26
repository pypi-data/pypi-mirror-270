# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/4/2 16:18
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: langchain_instance.py
from typing import Any, List, Optional

from langchain.callbacks.manager import AsyncCallbackManagerForLLMRun, CallbackManagerForLLMRun
from langchain.chat_models import ChatOpenAI
from langchain.schema import BaseMessage, ChatResult

from agentuniverse.llm.llm import LLM


class LangchainOpenAI(ChatOpenAI):
    """Langchain OpenAI LLM wrapper."""

    llm: Optional[LLM] = None

    def __init__(self, llm: LLM):
        """The __init__ method.

        The agentUniverse LLM instance is passed to this class as an argument.
        Convert the attributes of AgentUniverse(AU) LLM instance to the LangchainOpenAI object for initialization

        Args:
            llm (LLM): the AgentUniverse(AU) LLM instance.
        """
        init_params = dict()
        init_params['model_name'] = llm.model_name if llm.model_name is not None else 'gpt-3.5-turbo'
        init_params['temperature'] = llm.temperature if llm.temperature is not None else 0.7
        init_params['request_timeout'] = llm.request_timeout
        init_params['max_tokens'] = llm.max_tokens
        init_params['max_retries'] = llm.max_retries if llm.max_retries is not None else 2
        init_params['streaming'] = llm.streaming if llm.streaming is not None else False
        init_params['openai_api_key'] = llm.openai_api_key
        init_params['openai_organization'] = llm.openai_organization
        init_params['openai_api_base'] = llm.openai_api_base
        init_params['openai_proxy'] = llm.openai_proxy
        super().__init__(**init_params)
        self.llm = llm

    def _generate(
            self,
            messages: List[BaseMessage],
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
            stream: Optional[bool] = None,
            **kwargs,
    ) -> ChatResult:
        """Run the Langchain OpenAI LLM."""
        message_dicts, params = self._create_message_dicts(messages, stop)
        params = {**params, **kwargs}
        llm_output = self.llm.call(messages=message_dicts, **params)
        return self._create_chat_result(llm_output.raw)

    async def _agenerate(
            self,
            messages: List[BaseMessage],
            stop: Optional[List[str]] = None,
            run_manager: Optional[AsyncCallbackManagerForLLMRun] = None,
            stream: Optional[bool] = None,
            **kwargs: Any,
    ) -> ChatResult:
        """Asynchronously run the Langchain OpenAI LLM."""
        message_dicts, params = self._create_message_dicts(messages, stop)
        params = {**params, **kwargs}
        llm_output = await self.llm.acall(messages=message_dicts, **params)
        return self._create_chat_result(llm_output.raw)
