import os
import logging
import asyncio
from config import BOT_USERNAME
from os import getenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# config vars
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER = os.getenv("OWNER")

# pyrogram client
app = Client(
            "banall",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
)

# start command
@app.on_message(filters.command("chita_hi_kehde") & filters.private)
async def start_command(client, message: Message):
    user = message.from_user
    await message.reply_photo(
        photo=f"https://files.catbox.moe/qej5mx.jpg",
        caption=f"**✦ » ʜᴇʏ {user.mention}**\n**✦ » ᴛʜɪs ɪs ᴀ sɪᴍᴘʟᴇ ʙᴀɴ ᴀʟʟ ʙᴏᴛ ᴡʜɪᴄʜ ɪs ʙᴀsᴇᴅ ᴏɴ ᴘʏʀᴏɢʀᴀᴍ ʟɪʙʀᴀʀʏ.**\n\n**✦ » ʙᴀɴ ᴏʀ ᴅᴇsᴛʀᴏʏ ᴀʟʟ ᴛʜᴇ ᴍᴇᴍʙᴇʀs ғʀᴏᴍ ᴀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ɪɴ ᴀ ғᴇᴡ sᴇᴄᴏɴᴅs.**\n\n**✦ » ᴄʜᴇᴄᴋ ᴍʏ ᴀʙɪʟɪᴛʏ ɢɪᴠᴇ ᴍᴇ ғᴜʟʟ ᴘᴏᴡᴇʀs ᴀɴᴅ ᴛʏᴘᴇ `/banall` ᴛᴏ ꜱᴇᴇ ᴍᴀɢɪᴄ ɪɴ ɢʀᴏᴜᴘ.**\n\n**✦ » 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ »  <a href=t.me/ll_ALPHA_BABY_lll>⎯᪵፝֟፝֟⎯꯭𓆩꯭ 𝐀 ꯭ʟ ꯭ᴘ ꯭ʜ꯭ ᴧ꯭⎯꯭꯭꯭̽🥂꯭༎꯭ 𓆪꯭ </a>**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚜️ Aᴅᴅ ᴍᴇ Bᴀʙʏ ⚜️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton("🔸 ❍ᴡɴᴇʀ🔸", url="http://t.me/ll_ALPHA_BABY_lll"),
                    InlineKeyboardButton("▫️ 𝗨ᴘᴅᴀᴛᴇs ▫️", url="http://t.me/PURVI_SUPPORT")
                ]                
            ]
        )
    )

# banall command
@app.on_message(filters.command("banall") & filters.group)
async def banall_command(client, message: Message):
    chat_id = message.chat.id
    await message.reply("🚨 Banall started... This may take time for 4k members!")

    async for member in app.get_chat_members(chat_id):
        try:
            # Admins aur owner ko skip karo
            if member.status in ("administrator", "owner"):
                print(f"Skipping admin/owner {member.user.id}")
                continue

            # Member ban karo
            await app.ban_chat_member(chat_id=chat_id, user_id=member.user.id)
            print(f"Kicked {member.user.id} from {chat_id}")
            await asyncio.sleep(0.3)  # floodwait safe delay
        except Exception as e:
            print(f"Failed to ban {member.user.id}: {e}")

    await message.reply("✅ Banall completed! Group is now empty.")

# start bot client
app.start()
print("Banall-Bot Booted Successfully")
idle()
