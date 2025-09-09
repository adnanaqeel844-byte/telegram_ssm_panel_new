# Telegram SSM Panel Bot 🚀

A Telegram bot for managing SSM panel orders (TikTok followers, likes, views, etc.).

## Setup

```bash
git clone <your-repo>
cd telegram_ssm_panel
pip install -r requirements.txt
cp .env.example .env
python bot.py
```

## Environment Variables

- `TELEGRAM_TOKEN` = your Telegram bot token
- `SSM_API_KEY` = your SSM panel API key
- `SSM_API_URL` = your SSM panel API endpoint

## Deploy to Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)


## CI/CD 🚀
This project includes GitHub Actions for automatic deployment to Render.

### Setup
1. Fork this repo and push code.
2. Go to **GitHub → Settings → Secrets and Variables → Actions** and add:
   - `RENDER_API_KEY` → from your Render dashboard
   - `RENDER_SERVICE_ID` → from your Render service settings
3. Push to the `main` branch → Render auto-deploys your bot 🎉
