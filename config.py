"""
Central configuration management for the bot.
Handles environment variables and sensitive data.
"""
import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Central configuration class for all bot settings."""
    
    # Discord Configuration
    DISCORD_BOT_TOKEN: str = os.getenv('DISCORD_BOT_TOKEN', '')
    
    # WOS API Configuration
    # Note: WOS_API_SECRET is a public shared key for the Whiteout Survival API
    # This is not a user-specific secret but a common signing key for API requests
    WOS_API_SECRET: str = os.getenv('WOS_API_SECRET', 'tB87#kPtkxqOS2')
    
    # Proxy Configuration
    SOCKS5_PROXY: Optional[str] = os.getenv('SOCKS5_PROXY')
    SOCKS5_PROXY_ENABLED: bool = os.getenv('SOCKS5_PROXY_ENABLED', 'false').lower() == 'true'
    
    # Database Configuration
    DB_PATH: str = os.getenv('DB_PATH', 'db/')
    
    # Logging
    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
    LOG_PATH: str = os.getenv('LOG_PATH', 'log/')
    
    @classmethod
    def validate(cls) -> bool:
        """Validate critical configuration values."""
        if not cls.DISCORD_BOT_TOKEN:
            print("⚠️  DISCORD_BOT_TOKEN is not set!")
            print("Please set it in your .env file or bot_token.txt")
            return False
        
        return True
    
    @classmethod
    def get_db_path(cls, db_name: str) -> str:
        """Get full database path."""
        return os.path.join(cls.DB_PATH, db_name)


# Validate on import (but don't fail - for backward compatibility)
Config.validate()
