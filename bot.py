from pyrogram import Client, filters

# Yahan apna credentials daalo
api_id = 28853585   # aapka api_id
api_hash = "54a3239f9171bfac0a44449eb8343152"
bot_token = "8283434073:AAGtSkIcoi9sGin4LpICtomq3I5grb0Wppc"

app = Client("music_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text("Hello! Bot chal raha hai ✅")

app.run()
