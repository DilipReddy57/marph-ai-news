# 🤖 AI News Relay Agent

A professional, modular Python application that collects daily AI news from multiple sources and delivers comprehensive digests to Telegram.

## ✨ Features

- **100% FREE**: No paid APIs required
- **Modular Architecture**: Clean separation of concerns
- **Robust**: Uses `requests` and `feedparser` for reliable data fetching
- **Type-Safe**: Pydantic models for configuration and data validation
- **Automated**: GitHub Actions workflow for daily 9 PM IST delivery
- **Extensible**: Easy to add new news sources

## 📁 Project Structure

```
marph-ai-news/
├── src/
│   └── ai_news_relay/
│       ├── __init__.py
│       ├── config.py       # Configuration management (Pydantic)
│       ├── models.py       # Data structures (Article)
│       ├── collectors.py   # News fetching (RSS, APIs)
│       ├── generator.py    # Markdown digest generation
│       ├── publisher.py    # Telegram integration
│       └── utils.py        # Logging utilities
├── .vscode/                # VS Code configuration
├── main.py                 # Entry point
├── requirements.txt        # Dependencies
└── .env.example           # Environment template
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file in the project root:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

### 3. Run Locally

```bash
python main.py
```

Or use VS Code's **Run and Debug** (F5).

## 🔧 Configuration

All configuration is managed through environment variables (see `src/ai_news_relay/config.py`):

| Variable                  | Required | Default | Description                             |
| ------------------------- | -------- | ------- | --------------------------------------- |
| `TELEGRAM_BOT_TOKEN`      | ✅       | -       | Your Telegram bot token from @BotFather |
| `TELEGRAM_CHAT_ID`        | ✅       | -       | Your Telegram chat ID                   |
| `MAX_ARTICLES_PER_SOURCE` | ❌       | 2       | Articles to fetch per source            |
| `MAX_DIGEST_LENGTH`       | ❌       | 4090    | Maximum message length                  |
| `LOG_LEVEL`               | ❌       | INFO    | Logging level                           |

## 📰 News Sources

### RSS Feeds

- TechCrunch AI
- MIT Technology Review AI
- Wired AI
- The Verge AI
- VentureBeat AI

### APIs

- Hacker News (Algolia API)

## 🤝 Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black src/ main.py
```

### Linting

```bash
pylint src/ main.py
```

## 🔐 Security

- ✅ Credentials stored in environment variables
- ✅ `.env` file excluded from git
- ✅ GitHub Secrets for CI/CD
- ✅ No hardcoded tokens

## 📅 Automation

The GitHub Actions workflow (`.github/workflows/ai-news-daily.yml`) runs automatically:

- **Schedule**: Daily at 9:00 PM IST (15:30 UTC)
- **Manual**: Can be triggered from the Actions tab

## 📝 License

MIT License - Feel free to use and modify!

## 🙏 Acknowledgments

Built with:

- [Requests](https://requests.readthedocs.io/) - HTTP library
- [Feedparser](https://feedparser.readthedocs.io/) - RSS/Atom parser
- [Pydantic](https://docs.pydantic.dev/) - Data validation
- [PyTZ](https://pythonhosted.org/pytz/) - Timezone support
