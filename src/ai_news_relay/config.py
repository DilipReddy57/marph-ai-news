from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""
    
    TELEGRAM_BOT_TOKEN: str = Field(..., description="Telegram Bot Token")
    TELEGRAM_CHAT_ID: str = Field(..., description="Telegram Chat ID")
    
    # Optional configuration with defaults
    MAX_ARTICLES_PER_SOURCE: int = 2
    MAX_DIGEST_LENGTH: int = 4090
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()
