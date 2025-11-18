# 🤖 AI News Relay Agent

Automated daily AI news aggregator that collects, summarizes, and delivers comprehensive AI updates to your Telegram account.

## ✨ Features

- **📰 Multi-Source News Collection**: Aggregates from 10+ AI sources including OpenAI, Google, Meta, Microsoft
- **🎯 Smart Categorization**: Organizes news into Breakthroughs, Products, Research, Funding, Jobs, Policy
- **🌍 Regional Coverage**: Separate tracking for India and US funding/opportunities
- **📱 Telegram Delivery**: Direct delivery to your Telegram with formatted digest (4000+ characters)
- **⏰ Automated Scheduling**: Runs daily at 9 PM IST via GitHub Actions
- **💾 Backup System**: Saves all digests to `/workspace/summaries/`
- **📊 Execution Logging**: Tracks all runs in `/workspace/logs/`

## 📋 News Categories

1. **🚀 Breakthrough Developments** - Major AI model releases, breakthroughs
2. **⚡ New Products & Tools** - Product launches, feature updates
3. **📚 Research Highlights** - Academic papers, research advances
4. **💰 Funding & Investments** - Startup funding (India & US separately)
5. **💼 AI Job Opportunities** - Hiring announcements from major companies
6. **⚖️ Policy & Regulation** - Government policies, regulations

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Telegram Bot Token
- Telegram Chat ID
- Anthropic API Key (for web searches)

### Configuration

The bot is already configured with:
- **Bot Token**: `8283610283:AAHJqg9AexBYFm15v-eWV39Pe8wC8gKnQP8`
- **Chat ID**: `939907290`
- **Schedule**: Daily at 9:00 PM IST (15:30 UTC)

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/ai-news-relay-agent.git
cd ai-news-relay-agent

# Install dependencies
pip install requests anthropic pytz

# Run manually
python ai_news_complete.py
```

## ⚙️ GitHub Actions Setup

### 1. Create GitHub Repository

```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit: AI News Relay Agent"

# Add remote and push
git remote add origin https://github.com/YOUR_USERNAME/ai-news-relay-agent.git
git branch -M main
git push -u origin main
```

### 2. Configure Secrets

Go to your GitHub repository → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Add the following secret:
- **Name**: `ANTHROPIC_API_KEY`
- **Value**: Your Anthropic API key

### 3. Enable GitHub Actions

1. Go to **Actions** tab in your repository
2. Enable workflows if prompted
3. The workflow will run automatically at 9 PM IST daily
4. You can also trigger manually using "Run workflow" button

## 📁 Project Structure

```
ai-news-relay-agent/
├── ai_news_complete.py          # Main script
├── .github/
│   └── workflows/
│       └── ai-news-daily.yml    # GitHub Actions workflow
├── summaries/                   # Backup digests (created on first run)
├── logs/                        # Execution logs (created on first run)
├── README.md                    # This file
└── requirements.txt             # Python dependencies
```

## 🔧 Manual Execution

Run the script anytime:

```bash
export ANTHROPIC_API_KEY="your-key-here"
python ai_news_complete.py
```

## 📊 Output Format

The digest includes:
- **Character Target**: 4000+ characters (max 4090 for Telegram limit)
- **Format**: Markdown with clickable links
- **Sections**: 6 main categories with multiple articles each
- **Footer**: Key insights and next update time

### Example Output

```
🤖 AI NEWS DAILY DIGEST
📅 November 18, 2025
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 BREAKTHROUGH DEVELOPMENTS

1. OpenAI releases GPT-5.1 with reasoning capabilities
   New model shows 40% improvement in complex reasoning...
   🔗 https://openai.com/gpt-5-1

...

💰 FUNDING & INVESTMENTS

🇮🇳 India:
1. Sarvam AI secures $41M funding...

🇺🇸 United States:
1. Cohere raises $500M Series D...

...
```

## 🛠️ Customization

### Change Schedule

Edit `.github/workflows/ai-news-daily.yml`:

```yaml
schedule:
  - cron: '30 15 * * *'  # Change this
```

Use [Crontab Guru](https://crontab.guru/) to generate cron expressions.

### Modify Categories

Edit `ai_news_complete.py` and adjust the `articles` dictionary in `generate_comprehensive_digest()`.

### Add More Sources

Add queries to the `queries` list in `search_ai_news()`.

## 📝 Logs & Monitoring

### Execution Logs
Location: `/workspace/logs/execution.log`

```
[2025-11-18 21:00:00 IST] SUCCESS - Message ID: 123
[2025-11-19 21:00:00 IST] SUCCESS - Message ID: 124
```

### Backup Digests
Location: `/workspace/summaries/ai_news_YYYYMMDD_HHMMSS.md`

## 🐛 Troubleshooting

### Issue: Telegram delivery fails
- Check bot token and chat ID are correct
- Verify bot has permission to send messages to the chat
- Check character limit (must be under 4096)

### Issue: GitHub Action fails
- Verify `ANTHROPIC_API_KEY` secret is set
- Check Actions tab for detailed error logs
- Ensure repository has Actions enabled

### Issue: Character count too low/high
- Adjust articles in `generate_comprehensive_digest()`
- Current target: 4000+ chars, max 4090

## 📜 License

MIT License - Feel free to use and modify!

## 🤝 Contributing

Contributions welcome! Please open an issue or PR.

## 📧 Support

For issues or questions, open a GitHub issue.

---

**Last Updated**: November 18, 2025
**Version**: 1.0.0
**Status**: ✅ Production Ready
