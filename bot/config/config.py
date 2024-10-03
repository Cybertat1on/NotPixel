from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import List

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    REF_LINK: str = "https://t.me/notpixel/app?startapp=f1197825376"
    X3POINTS: bool = True
    AUTO_UPGRADE_PAINT_REWARD: bool = True
    AUTO_UPGRADE_RECHARGE_SPEED: bool = True
    AUTO_UPGRADE_RECHARGE_ENERGY: bool = True
    AUTO_TASK: bool = True

    DELAY_EACH_ACCOUNT: List[int] = Field(default_factory=lambda: [10, 15])
    USE_PROXY_FROM_FILE: bool = False

    SLEEP_TIME: List[int] = Field(default_factory=lambda: [3000, 8000])
    NIGHT_SLEEP: bool = True
    NIGHT_SLEEP_START_TIME: List[int] = Field(default_factory=lambda: [0, 2])
    NIGHT_SLEEP_END_TIME: List[int] = Field(default_factory=lambda: [5, 7])

settings = Settings()
