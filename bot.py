from pyrogram import Client, filters
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import InputStream, AudioPiped
import yt_dlp

api_id = 123456  # yahan apna api_id likhna hai
api_hash = "your_api_hash"
bot_token = "your_bot_token"

app = Client("mybot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
call = PyTgCalls(app)

def download_audio(query):
    ydl_opts = {"format": "bestaudio/best", "outtmpl": "song.%(ext)s", "quiet": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(f"ytsearch:{query}", download=True)
    return "song.webm"

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text("🎵 /play <song name> bhejo VC me song bajane ke liye!")

@app.on_message(filters.command("play") & filters.group)
async def play(_, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /play <song name>")
    query = " ".join(message.command[1:])
    await message.reply_text(f"🔎 '{query}' dhoondh raha hoon...")
    file = download_audio(query)
    chat_id = message.chat.id
    await call.join_group_call(chat_id, InputStream(AudioPiped(file)))
    await message.reply_text("▶️ Song play ho raha hai VC me!")

app.start()
call.start()
print("Bot chal gaya ✅")
idle()
