from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Подъземелье, драконы и записи пользователей'
    description: str = 'Пользователи делают записи'
    secret: str = 'SECRET'
    database_url_lite: str = "sqlite+aiosqlite:///./fastapi.db"

    POSTGRES_DB_NAME: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    REDIS_HOST: str
    REDIS_PORT: int

    @property
    def DATABASE_URL(self):
        return (f'postgresql+asyncpg://{self.POSTGRES_USER}:'
                f'{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:'
                f'{self.POSTGRES_PORT}/{self.POSTGRES_DB_NAME}')

    class Config:
        env_file = '.env'


settings = Settings()
