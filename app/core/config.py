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
    DB_URL:str = "postgresql+asyncpg://postgres:1111@localhost:5432/todo"
    POSTGRES_USER:str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD:str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB:str =  os.getenv("POSTGRES_DB")
    
    

    
    model_config = SettingsConfigDict(env_file='.env')
        

settings = Settings()