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
from pyrogram import (
    Client,
    Filters,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


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

@pyrogram.Client.on_callback_query()
async def cb_handler(bot, update):

    if "close" in update.data:
        await update.message.delete()


@pyrogram.Client.on_message(pyrogram.Filters.command(["help"]))
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

@pyrogram.Client.on_message(pyrogram.Filters.command(["about"]))
async def about_me(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/about")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_ME.format(
            bot.username
        ),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/start")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('📌Support📌', url="t.me/KL35Cinemas"),
                    InlineKeyboardButton('😎Creator😎', url="t.me/KL35RonaldoFan")
                ],
                [
                    InlineKeyboardButton('❤️My Group❤️', url="t.me/KL35Cinemas"),
                    InlineKeyboardButton('💛My Channel💛', url="t.me/KL35Cinemaz")
                ],
                [
                    InlineKeyboardButton('🆒Source Code🆒', url="https://bit.ly/2AVFsoD"),
                    InlineKeyboardButton('🔐Close🔐', callback_data="close")
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )

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
    TRChatBase(update.from_user.id, update.photo, "/kl35thumb")
    await bot.send_photo(
        chat_id=update.chat.id,
        photo=Translation.KL35_THUMBNAIL_PHOTO,
        reply_to_message_id=update.message_id
    )
