#youtubeslgeekshow

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

from bot import bot as app

#song text
TEXT = "🌟Use Bellow Format \n\n💫 Format :- /song <song name >"
#lyric text
LYRIC = "🌟Use Bellow Format \n\n💫 Format :- /lyric <lyric name >"
#Video Download text
VIDEO = "🌟Use Bellow Format \n\n💫 Format :- /lyric <lyric name >"
#saavn  text
SAAVN = "🌟Use Bellow Format \n\n💫 Format :- /lyric <lyric name >"

@app.on_callback_query(filters.regex("help"))
async def help(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Help menu off szsong bot
""",
        reply_markup=InlineKeyboardMarkup(
            [       
                [
                    InlineKeyboardButton(
                         "Song Download", callback_data="songback"
                    ),
                    InlineKeyboardButton(
                        "lyric Download", callback_data="lyricback")
                ],[
                    InlineKeyboardButton(
                        "Video Download", callback_data="videoback"
                    ),
                    InlineKeyboardButton(
                        "saavn Download ", callback_data="saavnback")
                 ],[
                    InlineKeyboardButton(
                        "Next", callback_data="cbcmds"
                    )
                  ]
           ]
        ),
     disable_web_page_preview=True
    )
@app.on_callback_query(filters.regex("songback"))
async def song_callbacc(_, CallbackQuery):
    text = TEXT
    await app.answer_callback_query(CallbackQuery.id, text, show_alert=True)  
    
@app.on_callback_query(filters.regex("lyricback"))
async def lyric_callbacc(_, CallbackQuery):
    text = LYRIC
    await app.answer_callback_query(CallbackQuery.id, text, show_alert=True)     
    
@app.on_callback_query(filters.regex("videoback"))
async def video_callbacc(_, CallbackQuery):
    text = VIDEO
    await app.answer_callback_query(CallbackQuery.id, text, show_alert=True)   

@app.on_callback_query(filters.regex("saavnback"))
async def saavn_callbacc(_, CallbackQuery):
    text = SAAVN
    await app.answer_callback_query(CallbackQuery.id, text, show_alert=True)  
    
     
    
