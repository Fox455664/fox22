import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
    
)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/06ea0dffac061d340b30a.mp4",
        caption=f"""❅─────✧❅✦❅✧─────❅
▰▰▰▰▰▰▰▰▰▰▰▰▰
么- 𓏺We are developers, #not heroes, so don't bark #like dogs

么- 𓏺Whoever humbles #himself to god will be #exalted 𓏺
▰▰▰▰▰▰▰▰▰▰▰▰▰
❅─────✧❅✦❅✧─────❅
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✧❅¹مــطور❅✧", url=f"https://t.me/F_o_x_5"), 
                 InlineKeyboardButton(
                   "✧❅²مــطور❅✧",       url=f"https://t.me/F_o_x_5"), 
                 
             ],[ 
            InlineKeyboardButton(
                        "❅✧قـناه السـورس✧❅", url=f"https://t.me/fox68899"), 
                   
             ],[ 
                  InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك⚡",
                url=f"https://t.me/{app.username}?startgroup=true"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["المطور فوكس"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("F_o_x_5")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"معلومات مطور السورس\n\n‍ ¦➻ 𝐍𝐀𝐌𝐄 :{name}\n\n ¦➻ 𝐔𝐒𝐄𝐑 :@{usr.username}\n\n ¦➻ 𝐈𝐃 :`{usr.id}`\n\n ¦➻ 𝐁𝐎𝐈 :{usr.bio}\n\nســورس ميــوزك wolf", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["فوكس" , "فوكس","مبرمج السورس"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("F_o_x_5")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"معلومات مطور السورس.\n\n¦➻ 𝐍𝐀𝐌𝐄 :{name}\n\n ¦➻ 𝐔𝐒𝐄𝐑 :@{usr.username}\n\n ¦➻ 𝐈𝐃 :`{usr.id}`\n\n ¦➻ 𝐁𝐎𝐈 :{usr.bio}\n\nسـورس مـيوزك wolf", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )



@app.on_message(
    command(["مطور السورس" , "فوكي","فوكس"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("F_o_x_5")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"معلومات مبرمج السورس.\n\n¦➻ 𝐍𝐀𝐌𝐄 :{name}\n\n ¦➻ 𝐔𝐒𝐄𝐑 :@{usr.username}\n\n ¦➻ 𝐈𝐃 :`{usr.id}`\n\n ¦➻ 𝐁𝐎𝐈 :{usr.bio}\n\nسـورس مـيوزك wolf", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )



