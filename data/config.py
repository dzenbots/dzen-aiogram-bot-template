from dataclasses import dataclass
from typing import Any

from environs import Env
from google.oauth2.service_account import Credentials


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Miscellaneous:
    scoped_credentials: Any = None
    google_spreadsheet_key: str = None
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous


def get_scoped_credentials(credentials, scopes):
    def prepare_credentials():
        return credentials.with_scopes(scopes)

    return prepare_credentials


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    scopes = [
        "https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"
    ]

    google_credentials = Credentials.from_service_account_file(env.str('GOOGLE_CREDENTIALS_FILE'))
    scoped_credentials = get_scoped_credentials(google_credentials, scopes)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS"),
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        ),
        misc=Miscellaneous(
            scoped_credentials=scoped_credentials,
            google_spreadsheet_key=env.str('GOOGLE_SPREADSHEET_KEY')
        )
    )
