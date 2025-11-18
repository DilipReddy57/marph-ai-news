# GitHub Token Setup - IMPORTANT

## ❌ Current Issue
Your token is missing the `workflow` scope needed to push GitHub Actions files.

## ✅ How to Fix

### Step 1: Generate New Token with Correct Scopes

1. Go to: https://github.com/settings/tokens/new
2. **Note**: "AI News Relay Agent - Full Access"
3. **Expiration**: Choose your preference (90 days recommended)
4. **Select these scopes**:
   - ✅ **repo** (Full control of private repositories)
   - ✅ **workflow** (Update GitHub Action workflows) ← **THIS IS REQUIRED**
5. Click **"Generate token"**
6. Copy the new token (starts with `ghp_`)

### Step 2: Provide the New Token

Share the new token with me and I'll push immediately.

## Why This Happened

GitHub requires explicit `workflow` scope permission to:
- Create workflow files in `.github/workflows/`
- Update existing workflow files
- Modify GitHub Actions configurations

Your current token only has `repo` scope, which isn't enough for workflow files.

## Alternative: Push Without Workflow File

If you want to push NOW without the workflow file:

```bash
# Remove workflow file temporarily
git rm .github/workflows/ai-news-daily.yml
git commit -m "Remove workflow (will add manually later)"
git push -u origin main

# Then manually create the workflow file on GitHub:
# 1. Go to repository → Actions → New workflow
# 2. Copy content from ai-news-daily.yml
# 3. Commit directly to main branch
```

---

**Quick Link**: https://github.com/settings/tokens/new?scopes=repo,workflow&description=AI+News+Relay+Agent
