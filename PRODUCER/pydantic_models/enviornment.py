import os
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    broker_host:str = Field(..., env='BROKER_HOST')
    run_env:str = Field(..., env='RUN_ENV')
    reverse_proxy_host:str = Field(..., env='REVERSE_PROXY_HOST')


    class Config:
        env_file = None
        env_file_encoding = 'utf-8'


def get_settings():
    run_env:str = os.environ['RUN_ENV']
    return Settings(_env_file=f'{run_env}.env', _env_file_encoding='utf-8')
