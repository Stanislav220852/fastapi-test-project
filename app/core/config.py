from pydantic_settings import BaseSettings, SettingsConfigDict
import os
class Settings(BaseSettings):
    ALGORITHM: str = "HS256"
    SECRET_KEY:str = "SECRET_KEY"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 720
    API_PORT:int = 8000
    DEBAG:bool = True
    
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: int = int(os.getenv("DB_PORT"))
    DB_USER: str = os.getenv("DB_USER")
    DB_PASS: str = os.getenv("DB_PASS")
    DB_NAME: str = os.getenv("DB_NAME")
    
    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL_psycopg(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    

    
    model_config = SettingsConfigDict(env_file='.env')
        

settings = Settings()