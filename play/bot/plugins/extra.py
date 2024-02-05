from play.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
import time
import shutil, psutil
from utils_bot import *
from play import StartTime

        
    
@StreamBot.on_message(filters.command('stats') & filters.private)
async def stats(bot, update):
  currentTime = readable_time((time.time() - StartTime))
  total, used, free = shutil.disk_usage('.')
  total = get_readable_file_size(total)
  used = get_readable_file_size(used)
  free = get_readable_file_size(free)
  sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
  recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
  cpuUsage = psutil.cpu_percent(interval=0.5)
  memory = psutil.virtual_memory().percent
  disk = psutil.disk_usage('/').percent
  botstats = f'<b>⏳ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ:</b> {currentTime}\n' \
            f'<b>⚙ ᴛᴏᴛᴀʟ ᴅɪꜱᴋ ꜱᴘᴀᴄᴇ:</b> {total}\n' \
            f'<b>⚠ ᴜꜱᴇᴅ:</b> {used}  ' \
            f'<b>♻ ꜰʀᴇᴇ:</b> {free}\n\n' \
            f'📊 ᴅᴀᴛᴀ ᴜꜱᴀɢᴇ 📊\n<b>📤 ᴜᴘʟᴏᴀᴅ:</b> {sent}\n' \
            f'<b>📥 ᴅᴏᴡɴʟᴏᴀᴅ:</b> {recv}\n\n' \
            f'<b>⚡ ᴄᴘᴜ:</b> {cpuUsage}% ' \
            f'<b>♻ ʀᴀᴍ:</b> {memory}% ' \
            f'<b>🌐 ᴅɪꜱᴋ:</b> {disk}%'
  await update.reply_text(botstats)
