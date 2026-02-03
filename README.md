# 🪙 Gold Telegram Bot

A simple Telegram bot that sends Turkish gold prices to a group every hour.

## What does this bot do?

- Gets gold prices from the internet
- Sends prices to your Telegram group
- Updates every 1 hour automatically

## Gold Types

| Turkish Name | English Name |
|-------------|--------------|
| Gram Altın | Gram Gold |
| Çeyrek Altın | Quarter Gold |
| Tam Altın | Full Gold |
| Ata Altın | Ata Gold |

## Message Format

```
💰 ALTIN FİYATLARI
2026-02-04 12:00:00

🪙 Gram: 6.913,52 / 6.915,07 ₺ 📈 0.08%
🥇 Çeyrek: 11.786,68 / 12.083,13 ₺ ➖ 0%
🏅 Tam: 47.146,71 / 48.184,70 ₺ ➖ 0%
👑 Ata: 48.620,04 / 49.958,37 ₺ ➖ 0%

Alış / Satış • Ezeogli Bot
```

## Installation

### Step 1: Install Python

You need Python 3.8 or higher. Download from: https://python.org

### Step 2: Install Libraries

```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables

1. Copy `.env.example` to `.env`
2. Edit `.env` file with your credentials:

```
BOT_TOKEN=your-telegram-bot-token-here
CHAT_ID=your-telegram-chat-id-here
```

**How to get Bot Token:**
1. Open Telegram, search for `@BotFather`
2. Send `/newbot` command
3. Follow the steps and copy the token

**How to get Group ID:**
1. Add `@ShowJsonBot` to your group
2. Send a message - the bot shows your group ID (starts with `-100`)

### Step 4: Run the Bot

```bash
python gold_telegram_bot.py
```

## Deploy to Render.com

### Step 1: Push to GitHub

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

> ⚠️ **Important**: Your `.env` file is NOT pushed to GitHub (it's in `.gitignore`). Your credentials are safe!

### Step 2: Create Render Service

1. Go to [render.com](https://render.com) and sign up
2. Click **New** → **Background Worker**
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: gold-telegram-bot
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python gold_telegram_bot.py`

### Step 3: Add Environment Variables

In Render dashboard, go to **Environment** tab and add:

| Key | Value |
|-----|-------|
| `BOT_TOKEN` | Your Telegram bot token |
| `CHAT_ID` | Your Telegram group ID |

### Step 4: Deploy

Click **Create Background Worker**. The bot will start automatically!

## Files

```
gold-telegram-bot/
├── gold_telegram_bot.py  # Main bot code
├── requirements.txt      # Python libraries
├── .env                  # Your credentials (not in git)
├── .env.example          # Example credentials file
├── .gitignore            # Files to ignore in git
└── README.md             # This file
```

## Troubleshooting

### Bot doesn't start
- Check if Python is installed: `python --version`
- Check if libraries are installed: `pip list`
- Check if `.env` file exists with correct values

### Bot doesn't send messages
- Check your bot token and group ID
- Make sure bot is added to the group
- Make sure bot has permission to send messages

## Data Source

Gold prices from: [Truncgil Finance API](https://finans.truncgil.com)

---

Made with ❤️ for Ezeogli Bot
