import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app




########################### بوت حذف
@app.on_message(filters.command(["الحذف", "عاوز احذف", "عاوزه احذف"], ""))
async def svksksa(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/a6137caa707bdb1247d7c.jpg",
        caption=f"""[خش احذف محدش هيمسك فيك يلا غور فداهية 😂❤](https://t.me/LC6BOT)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اضـغـط لـدخول للـبوت", url=f"https://t.meLC6BOT")
                ]
           ]
        ),
    )
   
   
 ########################### قول  
@app.on_message(filters.command(["قول", "كول"], ""))
 async def svksksa(client: Client, message: Message):
    await message.reply_photo
    video=f"https://telegra.ph/file/9a8329cc7b5fc2df92a2f.mp4"
    
