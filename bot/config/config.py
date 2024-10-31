from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    USE_REF: bool = True
    REF_ID: str = 'f1197825376'

    USE_RANDOM_DELAY_IN_RUN: bool = True
    RANDOM_DELAY_IN_RUN: list[int] = [5, 60]

    SLEEP_TIME_IN_MINUTES: list[int] = [30, 60]

    ENABLE_AUTO_TASKS: bool = True
    ENABLE_AUTO_DRAW: bool = True
    UNSAFE_ENABLE_JOIN_TG_CHANNELS: bool = False
    ENABLE_CLAIM_REWARD: bool = True
    ENABLE_AUTO_UPGRADE: bool = True
    ENABLE_AUTO_PUMPKINS: bool = True

    ENABLE_AUTO_JOIN_TO_SQUAD_CHANNEL: bool = False
    ENABLE_AUTO_JOIN_TO_SQUAD: bool = True
    SQUAD_SLUG: str = "CybertationPixel"

    DISABLE_IN_NIGHT: bool = False
    NIGHT_TIME: list[int] = [23, 6]

    ENABLE_SOCKETS: bool = False
    ENABLE_CHECK_UPDATED_IMAGE_MODE: bool = False
    ENABLE_SERVER_MODE: bool = False

    ENABLE_RANDOM_CUSTOM_TEMPLATE: bool = True
    RANDOM_TEMPLATE_IDS: list[int] = [
        6103707977, 1479673219, 1041243367, 2087855212,
        2100761925, 508528154, 474917422, 7151956877,
        5098860372, 751725586, 1197825376
    ]

    ENABLE_DRAW_CUSTOM_TEMPLATE: bool = True
    CUSTOM_TEMPLATE_ID: int = 1197825376

    ENABLE_SSL: bool = False

    PAINT_REWARD_MAX: int = 7
    ENERGY_LIMIT_MAX: int = 7
    RE_CHARGE_SPEED_MAX: int = 11

    BOOSTS_BLACK_LIST: list[str] = ['invite3frens', 'INVITE_FRIENDS', 'TON_TRANSACTION', 'BOOST_CHANNEL', 'ACTIVITY_CHALLENGE', 'CONNECT_WALLET']
    TASKS_TODO_LIST: list[str] = ["pumpkin", "x:notcoin", "x:notpixel", "paint20pixels", "leagueBonusSilver", "leagueBonusGold", "leagueBonusPlatinum", "channel:notpixel_channel", "channel:notcoin", "boinkTask", "makePixelAvatar", "joinSquad"]

    USE_PROXY_FROM_FILE: bool = True

    SHOW_TEMPLATES_LIST: bool = False # DON'T TOUCH IT
    OPEN_TEMPLATES_LIST_IN_BROWSER: bool = True

    # ------ LEGACY CONFIGURATIONS ------
    ENABLE_DRAW_ART: bool = False
    DRAW_ART_COORDS: list[dict] = [
        {
            'color': "#6A5CFF",
            'x': { 'type': 'diaposon', 'value': [995, 999] },
            'y': { 'type': 'random', 'value': [995, 999] }
        }
    ]
    DRAW_RANDOM_X_DIAPOSON: list[int] = [390, 435]
    DRAW_RANDOM_Y_DIAPOSON: list[int] = [415, 445]
    DRAW_RANDOM_COLORS: list[str] = ["#3690EA"]
    ENABLE_EXPERIMENTAL_X3_MODE: bool = True
    UNABLE_JOIN_TG_CHANNELS: bool = False
    # ------ LEGACY CONFIGURATIONS ------

settings = Settings()


