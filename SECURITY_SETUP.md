# 🔐 Security Setup - Telegram Bot Token Protection

## ⚠️ CRITICAL: Your bot token was publicly visible!

**Security Risk Fixed**: Bot token and chat ID are now stored securely using environment variables.

---

## 🛡️ What Changed

### Before (INSECURE ❌):

```python
TELEGRAM_BOT_TOKEN = "your_old_token_here"  # PUBLIC!
TELEGRAM_CHAT_ID = "your_chat_id_here"  # PUBLIC!
```

### After (SECURE ✅):

```python
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")  # From environment
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")      # From environment
```

---

## 🚨 IMMEDIATE ACTION REQUIRED

### Step 1: Revoke Your Current Bot Token

Your old token is compromised (it was in public repo). You MUST create a new one:

1. **Open Telegram** and message **@BotFather**
2. Send command: `/revoke`
3. Select your bot: **@YourBotName**
4. Confirm revocation
5. Send command: `/newbot` or use your existing bot
6. Get your **NEW token** (keep it secret!)

### Step 2: Add Secrets to GitHub

1. Go to: https://github.com/DilipReddy57/marph-ai-news/settings/secrets/actions
2. Click **"New repository secret"**

**Add these TWO secrets:**

**Secret 1:**

- **Name**: `TELEGRAM_BOT_TOKEN`
- **Value**: `your_new_bot_token_here` (from @BotFather)

**Secret 2:**

- **Name**: `TELEGRAM_CHAT_ID`
- **Value**: `your_chat_id_here`

### Step 3: Verify Setup

After adding secrets:

1. Go to **Actions** tab
2. Click **"Run workflow"**
3. Check if it completes successfully
4. Verify message received in Telegram

---

## 💻 For Local Testing

### Option 1: Using .env file (Recommended)

1. **Create `.env` file** in project root:

```bash
TELEGRAM_BOT_TOKEN=your_new_token_here
TELEGRAM_CHAT_ID=939907290
```

2. **Load and run**:

```bash
# Load environment variables
export $(cat .env | xargs)

# Run script
python ai_news_complete.py
```

### Option 2: Direct export

```bash
export TELEGRAM_BOT_TOKEN="your_new_token_here"
export TELEGRAM_CHAT_ID="939907290"
python ai_news_complete.py
```

### Option 3: Python-dotenv (Advanced)

Install package:

```bash
pip install python-dotenv
```

Add to top of `ai_news_complete.py`:

```python
from dotenv import load_dotenv
load_dotenv()  # Load .env file
```

---

## 🔒 Security Best Practices

### ✅ DO:

- Store tokens in GitHub Secrets for CI/CD
- Use `.env` files for local development (never commit!)
- Revoke compromised tokens immediately
- Use different tokens for dev/prod if possible
- Regularly rotate tokens (every 3-6 months)

### ❌ DON'T:

- Hard-code tokens in source code
- Commit `.env` files to git
- Share tokens in chat/email
- Use same token across multiple projects
- Leave unused bots/tokens active

---

## 🚨 What If Token is Compromised?

If someone gets your bot token, they can:

- Send messages to any chat the bot has access to
- Impersonate your bot
- Spam users
- Get bot information

**Solution**: Revoke token immediately via @BotFather

---

## 📋 Security Checklist

After following this guide:

- [ ] Revoked old compromised token
- [ ] Created new bot token
- [ ] Added `TELEGRAM_BOT_TOKEN` to GitHub Secrets
- [ ] Added `TELEGRAM_CHAT_ID` to GitHub Secrets
- [ ] Tested workflow with new secrets
- [ ] Verified `.env` is in `.gitignore`
- [ ] Deleted any old tokens from notes/docs
- [ ] Set reminder to rotate token in 6 months

---

## 🔗 Helpful Links

- **BotFather**: https://t.me/botfather
- **GitHub Secrets**: https://github.com/DilipReddy57/marph-ai-news/settings/secrets/actions
- **Telegram Bot API**: https://core.telegram.org/bots/api

---

## ✅ Verification

After setup, your script will show:

```
✅ Token loaded from environment
✅ Chat ID loaded from environment
```

If missing:

```
❌ ERROR: Missing required environment variables!
```

---

**Remember**: Treat bot tokens like passwords. Never share or commit them!
