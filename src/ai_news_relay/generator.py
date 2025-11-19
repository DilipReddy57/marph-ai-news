from datetime import datetime
import pytz
from typing import Dict, List
from .models import Article
from .config import settings
from .utils import logger

class DigestGenerator:
    """Generates the markdown digest from collected articles."""

    def generate(self, articles: Dict[str, List[Article]]) -> str:
        """Create the formatted markdown digest."""
        logger.info("Generating digest...")
        
        lines = []
        lines.append("🤖 *AI NEWS DAILY DIGEST*")
        lines.append(f"📅 {datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%B %d, %Y')}")
        lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        lines.append("")

        # Order of sections
        sections = [
            ('breakthroughs', "🚀 *BREAKTHROUGH DEVELOPMENTS*"),
            ('products', "⚡ *NEW PRODUCTS & TOOLS*"),
            ('research', "📚 *RESEARCH HIGHLIGHTS*"),
            ('funding', "💰 *FUNDING & INVESTMENTS*"),
            ('jobs', "💼 *AI JOB OPPORTUNITIES*"),
            ('policy', "⚖️ *POLICY & REGULATION*")
        ]

        for key, header in sections:
            if articles.get(key):
                lines.append(header)
                lines.append("")
                for i, article in enumerate(articles[key][:4], 1):
                    lines.append(f"{i}. {article.to_markdown()}")
                    lines.append("")

        # Footer
        lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        lines.append("📊 *Key Insight:* AI technology advancing rapidly with increased focus on practical applications.")
        lines.append("")
        lines.append("⏰ *Next update: Tomorrow 9 PM IST*")
        lines.append("")
        lines.append("_Powered by AI News Relay Agent_")

        digest = "\n".join(lines)
        
        # Length check
        if len(digest) > settings.MAX_DIGEST_LENGTH:
            logger.warning(f"Digest too long ({len(digest)} chars). Truncating...")
            digest = digest[:settings.MAX_DIGEST_LENGTH - 100] + "\n\n*[Truncated]*"
            
        return digest
