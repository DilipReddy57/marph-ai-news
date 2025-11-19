from dataclasses import dataclass
from typing import Optional

@dataclass
class Article:
    """Represents a single news article."""
    title: str
    url: str
    description: str
    source: str
    category: str = "General"
    region: Optional[str] = None

    def to_markdown(self) -> str:
        """Convert article to markdown format."""
        md = f"*{self.title}*\n"
        if self.description:
            md += f"   {self.description}\n"
        md += f"   🔗 {self.url}"
        return md
