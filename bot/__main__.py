#MIT License

#Copyright (c) 2021 slgeekshow

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import bot as app
from bot import LOGGER
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from bot.plugins import *
from pyrogram import idle, filters
from bot.plugins.Dev import *
from config import BOT_USERNAME
from bot.helpers.fsub import fsub


text = """
Hello [{}](tg://user?id={}) π

I am **sz song Downloader Bot**

πAvailable Features 

Download  song π§
Download saavn πΌ
Download lyrics π
Download video  π₯
If you want to know how to use me just
touch on `Help` Button π¨

β¬ββββββββββββββ¬
π€ Bot Owner :- [Supun](https://t.me/supunmabot)
π¦ Powered By :- `γSZβ’γ`
β¬ββββββββββββββ¬


β οΈcopyright Β©οΈ 2021 [szteambots](https://t.me/szteambots). ** All Rights Reserved** 
"""

@app.on_message(filters.command("start"))
@fsub()
async def start(client, message): #fsub start
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        button = [
    [
        InlineKeyboardButton(text="Search on youtube here π", switch_inline_query_current_chat="")
    ],
    [
        InlineKeyboardButton(text="Updates Channelπ£", url="https://t.me/szteambots"),
        InlineKeyboardButton(
            text=" Support Groupπ₯", url="https://t.me/slbotzone"
        ),
    ],
    [
        InlineKeyboardButton(text="ποΈ Help ποΈ",  callback_data="xelp")
    ],
    [
        InlineKeyboardButton(text="βAdd Me To Your Groupβ", url=f"http://t.me/{BOT_USERNAME}?startgroup=new"),
    ],
]
    else:
        button = None
    await message.reply_photo(
                    photo="https://telegra.ph/file/29710ffe0c70108ff1955.jpg",
                    reply_markup=InlineKeyboardMarkup(button),
                    caption=text.format(name, user_id))



app.start()
LOGGER.info("""
βββ³βββββββββββββββββββ
βββ«ββ³ββββ³β«ββ³ββ³βββββ³ββ«ββ
β£ββββ«βββ«ββ«ββ«β»β«βββββββββ«
βββ»ββ»βββ»ββββ»ββ»βββββ»ββ»ββ
ββ?β?β?β?  I am supun  β―β―β―β―β
ββ?β?β?β?  Join @sl_bot_zone β―β―β―β―β
""")
idle()
