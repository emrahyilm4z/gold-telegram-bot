"""
Gold Prices Telegram Bot
Sends Turkish gold prices (gram, quarter, ata gold) 
to the specified Telegram group every hour.
Data Source: Truncgil Finance API
"""

import asyncio
import os
import aiohttp
from datetime import datetime
from telegram import Bot
from telegram.constants import ParseMode
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot Configuration (from environment variables)
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))
UPDATE_INTERVAL_SECONDS = 3600  # 1 hour (60 minutes * 60 seconds)

# Truncgil Finance API endpoint
GOLD_API_URL = "https://finans.truncgil.com/v4/today.json"


async def fetch_gold_prices() -> dict:
    """Fetches gold prices from Truncgil API."""
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(GOLD_API_URL, timeout=10) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"API error: Status {response.status}")
                    return None
        except Exception as error:
            print(f"Price fetch error: {error}")
            return None


def format_price(price) -> str:
    """Formats the price with Turkish number formatting."""
    try:
        if isinstance(price, (int, float)):
            # Turkish format: 1.234,56
            return f"{price:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return str(price)
    except:
        return str(price)


def get_change_emoji(change) -> str:
    """Returns emoji based on price change direction."""
    try:
        change_value = float(change)
        if change_value > 0:
            return "📈"
        elif change_value < 0:
            return "📉"
        else:
            return "➖"
    except:
        return "➖"


def create_message(data: dict) -> str:
    """Creates the Telegram message with gold prices."""
    update_date = data.get("Update_Date", datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    
    # Gold types from Truncgil API
    gram_gold = data.get("GRA", {})
    quarter_gold = data.get("CEYREKALTIN", {})
    full_gold = data.get("TAMALTIN", {})
    ata_gold = data.get("ATAALTIN", {})
    
    message = f"""💰 *ALTIN FİYATLARI*
_{update_date}_

🪙 *Gram*: `{format_price(gram_gold.get('Buying', 0))}` / `{format_price(gram_gold.get('Selling', 0))}` ₺ {get_change_emoji(gram_gold.get('Change', 0))} {gram_gold.get('Change', 0)}%

🥇 *Çeyrek*: `{format_price(quarter_gold.get('Buying', 0))}` / `{format_price(quarter_gold.get('Selling', 0))}` ₺ {get_change_emoji(quarter_gold.get('Change', 0))} {quarter_gold.get('Change', 0)}%

🏅 *Tam*: `{format_price(full_gold.get('Buying', 0))}` / `{format_price(full_gold.get('Selling', 0))}` ₺ {get_change_emoji(full_gold.get('Change', 0))} {full_gold.get('Change', 0)}%

👑 *Ata*: `{format_price(ata_gold.get('Buying', 0))}` / `{format_price(ata_gold.get('Selling', 0))}` ₺ {get_change_emoji(ata_gold.get('Change', 0))} {ata_gold.get('Change', 0)}%

_Alış / Satış • Ezeogli Bot_"""
    return message


async def send_gold_prices():
    """Main function: Sends gold prices to Telegram group."""
    # Validate configuration
    if not BOT_TOKEN or not CHAT_ID:
        print("❌ Error: BOT_TOKEN and CHAT_ID must be set in .env file!")
        print("   Create a .env file with your credentials (see .env.example)")
        return
    
    bot = Bot(token=BOT_TOKEN)
    
    print("🚀 Gold Prices Bot started!")
    print(f"📢 Target group: {CHAT_ID}")
    print(f"⏱️  Update interval: {UPDATE_INTERVAL_SECONDS} seconds ({UPDATE_INTERVAL_SECONDS // 60} minutes)")
    print("-" * 40)
    
    while True:
        try:
            # Fetch prices from API
            data = await fetch_gold_prices()
            
            if data:
                # Create and send message
                message = create_message(data)
                await bot.send_message(
                    chat_id=CHAT_ID,
                    text=message,
                    parse_mode=ParseMode.MARKDOWN
                )
                print(f"✅ [{datetime.now().strftime('%H:%M:%S')}] Prices sent successfully!")
            else:
                print(f"❌ [{datetime.now().strftime('%H:%M:%S')}] Failed to fetch prices!")
                
        except Exception as error:
            print(f"❌ Error: {error}")
        
        # Wait for next update
        await asyncio.sleep(UPDATE_INTERVAL_SECONDS)


if __name__ == "__main__":
    asyncio.run(send_gold_prices())
