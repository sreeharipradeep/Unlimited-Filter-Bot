from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot import app
from Script import Script

@app.on_message(filters.private & filters.command("start"))
async def start(client, message):
    try:
        await client.send_photo(
            chat_id=message.chat.id,
            photo="https://i.imgur.com/XXXXXXX.jpg",  # 🔴 Replace with your image URL
            caption=Script.START_MSG,
            parse_mode="html",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("➕ Add Me to Group", url="https://t.me/YourBotUsername?startgroup=true")],
                [InlineKeyboardButton("📚 Help", callback_data="help_cb")],
                [InlineKeyboardButton("💬 Support", url="https://t.me/YourSupportGroup")]
            ])
        )
    except Exception as e:
        print(f"Error in start command: {e}")
