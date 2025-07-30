from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from typing import Optional
from langchain_openai import ChatOpenAI

class WaterMakerSettings(BaseSettings):
    MODEL_NAME: str
    OPENROUTER_TOKEN: str
    PROVIDER: str
    llm: Optional[ChatOpenAI] = None

    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "./../.env"), extra="ignore")

    def get_key_provider(self) -> str:
        return self.PROVIDER
    def get_llm_name(self) -> str:
        return self.MODEL_NAME

    def get_llm_token(self) -> str:
        return self.OPENROUTER_TOKEN

settings = WaterMakerSettings()