import requests
from .config import settings
from .utils import logger

class TelegramPublisher:
    """Handles publishing content to Telegram."""

    def __init__(self):
        self.base_url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}"

    def send_message(self, text: str) -> bool:
        """Send a markdown message to the configured chat."""
        logger.info("Sending digest to Telegram...")
        
        url = f"{self.base_url}/sendMessage"
        payload = {
            "chat_id": settings.TELEGRAM_CHAT_ID,
            "text": text,
            "parse_mode": "Markdown",
            "disable_web_page_preview": True
        }

        try:
            response = requests.post(url, json=payload, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            if result.get("ok"):
                logger.info(f"✓ Delivered! Message ID: {result['result']['message_id']}")
                return True
            else:
                logger.error(f"✗ Telegram API Error: {result.get('description')}")
                return False
                
        except requests.exceptions.RequestException as e:
            logger.error(f"✗ Network Error sending to Telegram: {e}")
            return False
