import feedparser
import requests
from typing import List, Dict
from .models import Article
from .utils import logger
from .config import settings

class NewsCollector:
    """Collects news from various sources."""

    RSS_FEEDS = {
        'TechCrunch AI': 'https://techcrunch.com/category/artificial-intelligence/feed/',
        'MIT Tech Review AI': 'https://www.technologyreview.com/topic/artificial-intelligence/feed',
        'Wired AI': 'https://www.wired.com/feed/tag/ai/latest/rss',
        'The Verge AI': 'https://www.theverge.com/rss/ai-artificial-intelligence/index.xml',
        'VentureBeat AI': 'https://venturebeat.com/category/ai/feed/',
    }

    def __init__(self):
        self.articles: Dict[str, List[Article]] = {
            'breakthroughs': [],
            'products': [],
            'research': [],
            'funding': [],
            'jobs': [],
            'policy': []
        }

    def fetch_all(self) -> Dict[str, List[Article]]:
        """Fetch news from all configured sources."""
        logger.info("Starting news collection...")
        
        self._fetch_rss_feeds()
        self._fetch_hacker_news()
        self._add_backups_if_needed()
        
        total = sum(len(v) for v in self.articles.values())
        logger.info(f"Collection complete. Found {total} articles.")
        return self.articles

    def _fetch_rss_feeds(self):
        """Fetch and parse RSS feeds."""
        logger.info("Fetching RSS feeds...")
        
        for source_name, url in self.RSS_FEEDS.items():
            try:
                feed = feedparser.parse(url)
                
                if feed.bozo:
                    logger.warning(f"Potential issue with feed {source_name}: {feed.bozo_exception}")
                
                count = 0
                for entry in feed.entries[:settings.MAX_ARTICLES_PER_SOURCE]:
                    article = Article(
                        title=entry.get('title', 'No Title'),
                        url=entry.get('link', ''),
                        description=self._clean_description(entry.get('summary', '') or entry.get('description', '')),
                        source=source_name,
                        category='breakthroughs' # Default category for RSS
                    )
                    self.articles['breakthroughs'].append(article)
                    count += 1
                
                logger.info(f"✓ {source_name}: {count} articles")
                
            except Exception as e:
                logger.error(f"✗ Failed to fetch {source_name}: {e}")

    def _fetch_hacker_news(self):
        """Fetch from Hacker News API."""
        logger.info("Searching Hacker News...")
        queries = ['AI', 'GPT', 'LLM']
        
        for query in queries:
            try:
                url = f"https://hn.algolia.com/api/v1/search?query={query}&tags=story&hitsPerPage={settings.MAX_ARTICLES_PER_SOURCE}"
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                
                data = response.json()
                count = 0
                
                for hit in data.get('hits', []):
                    if hit.get('title') and hit.get('url'):
                        article = Article(
                            title=hit['title'],
                            url=hit.get('url', f"https://news.ycombinator.com/item?id={hit.get('objectID')}"),
                            description="Discussion on Hacker News",
                            source="Hacker News",
                            category='products'
                        )
                        self.articles['products'].append(article)
                        count += 1
                
                logger.info(f"✓ HN '{query}': {count} results")
                
            except Exception as e:
                logger.error(f"✗ Failed to fetch HN for '{query}': {e}")

    def _clean_description(self, text: str) -> str:
        """Clean up HTML and truncate description."""
        # Simple tag stripping could be added here if needed
        # For now, just truncate
        if not text:
            return ""
        return text[:150] + "..." if len(text) > 150 else text

    def _add_backups_if_needed(self):
        """Add curated content if feeds fail."""
        if len(self.articles['breakthroughs']) < 3:
            logger.info("Adding backup breakthrough articles...")
            self.articles['breakthroughs'].extend([
                Article(
                    title='OpenAI announces GPT-5 development progress',
                    url='https://openai.com/blog',
                    description='Next-generation language model showing improved reasoning capabilities.',
                    source='Curated'
                ),
                Article(
                    title='Google Gemini 2.0 achieves new benchmarks',
                    url='https://blog.google/technology/ai',
                    description='Latest multimodal AI model outperforms previous versions across tasks.',
                    source='Curated'
                )
            ])
