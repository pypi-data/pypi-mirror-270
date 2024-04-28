from .interfaces.openai import openai
from .interfaces.cohere import cohere


def init(api_key: str, anonymize: bool = True) -> None:
    openai._init(glaider_api_key=api_key)
    cohere._init(glaider_api_key=api_key)
