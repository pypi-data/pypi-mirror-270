from glaider.providers.openai_wrapper import OpenAIWrapper
import os
from functools import wraps
from typing import List, Dict, Optional
import requests
import datetime


def check_api_keys(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Get the 'self' instance from args if present
        instance = args[0] if args else None

        if instance and hasattr(instance, '_openai_wrapper'):
            openai_api_key = instance._openai_wrapper.get_api_key()
        else:
            openai_api_key = os.getenv('OPENAI_API_KEY')
            instance._openai_wrapper.set_api_key(openai_api_key)

        glaider_api_key = getattr(instance, '_glaider_api_key', None) or os.getenv('GLAIDER_API_KEY')

        if not openai_api_key:
            raise ValueError("Missing OpenAI API keys")
        if not glaider_api_key:
            raise ValueError("Missing Glaider API keys")

        return func(*args, **kwargs)
    return wrapper


class OpenAIInterface:

    def __init__(self):
        self._glaider_api_key = None
        self._anonymization = True
        self._openai_wrapper = None
        self._openai_wrapper = OpenAIWrapper()

    def _init(self, glaider_api_key):
        self._glaider_api_key = glaider_api_key

    @property
    def api_key(self):
        return self._openai_wrapper.get_api_key()

    @api_key.setter
    def api_key(self, value):
        self._openai_wrapper.set_api_key(value)

    @check_api_keys
    def chat_completion_create(self,
            model: str = "gpt-3.5-turbo",
            messages: Optional[List[Dict[str, str]]] = None,
            temperature: float = 0.0,
            max_tokens: int = 2000,
            **kwargs
    ):
        """
        Use OpenAI's completion API to generate a response to a prompt

        :return: Dictionary with LLM response and metadata
        """
        if messages is None:
            messages = [{"role": "assistant", "content": "You are an intelligent assistant."}]

        resp, sensitive_detected = self._openai_wrapper.send_openai_request(
            "ChatCompletion",
            "create",
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs,
        )
        self._notify_backend(sensitive_detected)
        return resp

    @check_api_keys
    def chat_completion_create_stream(self,
            model: str = "gpt-3.5-turbo",
            messages: Optional[List[Dict[str, str]]] = None,
            temperature: float = 0.0,
            max_tokens: int = 2000,
            **kwargs
    ):
        if messages is None:
            messages = [{"role": "assistant", "content": "You are an intelligent assistant."}]

        resp, sensitive_detected = self._openai_wrapper.send_openai_request(
            "ChatCompletion",
            "create",
            model=model,
            messages=messages,
            temperature=temperature,
            stream=True,
            max_tokens=max_tokens,
            **kwargs,
        )
        self._notify_backend(sensitive_detected)
        return resp

    @check_api_keys
    def completion_create(self,
            model: str = "text-davinci-003",
            prompt: str = "",
            temperature: float = 0.0,
            max_tokens: int = 50,
            **kwargs
    ):
        """
        Use OpenAI's chat_completion API to generate a response given a chat (series of prompts)

        :return: Dictionary with LLM response and metadata
        """
        resp, sensitive_detected = self._openai_wrapper.send_openai_request(
            "Completion",
            "create",
            model=model,
            max_tokens=max_tokens,
            prompt=prompt,
            temperature=temperature,
            **kwargs,
        )
        self._notify_backend(sensitive_detected)
        return resp

    @check_api_keys
    def completion_create_stream(self,
            model: str = "text-davinci-003",
            prompt: str = "",
            temperature: float = 0.0,
            max_tokens: int = 50,
            **kwargs
    ):
        resp, sensitive_detected = self._openai_wrapper.send_openai_request(
            "Completion",
            "create",
            model=model,
            max_tokens=max_tokens,
            prompt=prompt,
            temperature=temperature,
            stream=True,
            **kwargs,
        )
        self._notify_backend(sensitive_detected)
        return resp

    @check_api_keys
    def embedding_create(self,
            embedding_texts: List[str],
            model: str = "text-embedding-ada-002",
    ):
        """
        Use OpenAI to turn a list of prompts into vectors

        :return: List of embeddings (a vector for each input prompt) and metadata
        """
        resp, sensitive_detected = self._openai_wrapper.send_openai_request(
            "Embedding",
            "create",
            embedding_texts=embedding_texts,
            model=model,
        )
        self._notify_backend(sensitive_detected)
        return resp

    @check_api_keys
    def edits_create(self,
            prompt: str,
            instruction: str,
            model: str = "text-davinci-edit-001",
    ):
        """
        Use OpenAI's edit API to edit a prompt given some instruction

        :return: Dictionary with edited prompts and metadata
        """
        resp, sensitive_detected = self._openai_wrapper.send_openai_request(
            "Edits",
            "create",
            prompt=prompt,
            instruction=instruction,
            model=model,
        )
        self._notify_backend(sensitive_detected)
        return resp

    def _notify_backend(self, sensitive_detected):
        for pii_detected in sensitive_detected:
            response = requests.post('http://localhost:8000/log-prompt', json={
                'username': "userExample",
                'department': "IT",
                'action': "Anonymized",
                'risk': pii_detected['risk'],
                'datetime': datetime.datetime.now().isoformat(),
                '_type': pii_detected['type'],
                'detection': "sent",
                'model': "SDK - openai",
                'cid': self._glaider_api_key
            }, headers={'Content-Type': 'application/json'})
            print('Backend notified, response status:', response.status_code)


openai = OpenAIInterface()
