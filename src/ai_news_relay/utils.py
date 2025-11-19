import logging
import sys
from .config import settings

def setup_logging():
    """Configure structured logging for the application."""
    
    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Quiet down some noisy libraries
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    
    return logging.getLogger("ai_news_relay")

logger = setup_logging()
