import os
from pyrogram import Client

# Always import config
from config import Config


if __name__ == "__main__":

    plugins = dict(
        root="plugins"
    )

    app = Client(
        name="filter_bot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=100
    )

    # Safe AUTH_USERS handling
    try:
        Config.AUTH_USERS.add(str(680815375))
    except AttributeError:
        pass

    print("Bot started successfully...")
    app.run()
