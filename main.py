#!/usr/bin/env python3
import sys
import os

# Add src to path so we can import the package
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from ai_news_relay.collectors import NewsCollector
from ai_news_relay.generator import DigestGenerator
from ai_news_relay.publisher import TelegramPublisher
from ai_news_relay.utils import logger

def main():
    """Main execution flow."""
    logger.info("=" * 50)
    logger.info("AI News Relay Agent - Starting Execution")
    logger.info("=" * 50)

    try:
        # 1. Collect
        collector = NewsCollector()
        articles = collector.fetch_all()

        # 2. Generate
        generator = DigestGenerator()
        digest = generator.generate(articles)

        # 3. Publish
        publisher = TelegramPublisher()
        success = publisher.send_message(digest)

        if success:
            logger.info("✅ Daily digest completed successfully!")
            sys.exit(0)
        else:
            logger.error("❌ Failed to send digest.")
            sys.exit(1)

    except Exception as e:
        logger.exception(f"❌ Critical Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
