#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"✯ ᴍʏ ɴᴀᴍᴇ: <a href=https://t.me/SECL4U>ꜰɪʟᴇ ꜱʜᴀʀɪɴɢ ʙᴏᴛ</a>\n✯ ʟɪʙʀᴀʀʏ: ᴘʏʀᴏɢʀᴀᴍ\n✯ ʟᴀɴɢᴜᴀɢᴇ: ᴘʏᴛʜᴏɴ 3\n✯ ʙᴜɪʟᴅ ꜱᴛᴀᴛᴜꜱ: ᴠ2.3.1 [ʙᴇᴛᴀ]\n✯ ꜱᴜᴘᴘᴏʀᴛ: <a href=https://t.me/SECLK>ꜱᴇᴄʟᴋ</a>\n✯ ᴄʀᴇᴀᴛᴏʀ:  <a href=https://t.me/About_Sandaruwan>ꜱᴀɴᴅᴀʀᴜᴡᴀɴ</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
