import html
import time
from datetime import datetime
from io import BytesIO

from telegram import ParseMode, Update
from telegram.error import BadRequest, TelegramError, Unauthorized
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram.utils.helpers import mention_html

import SuzuneV2.modules.sql.global_bans_sql as sql
from SuzuneV2.modules.sql.users_sql import get_user_com_chats
from SuzuneV2 import (
    DEV_USERS,
    EVENT_LOGS,
    OWNER_ID,
    STRICT_GBAN,
    DRAGONS,
    SUPPORT_CHAT,
    SPAMWATCH_SUPPORT_CHAT,
    DEMONS,
    TIGERS,
    WOLVES,
    sw,
    dispatcher,
)
from SuzuneV2.modules.helper_funcs.chat_status import (
    is_user_admin,
    support_plus,
    user_admin,
)
from SuzuneV2.modules.helper_funcs.extraction import (
    extract_user,
    extract_user_and_text,
)
from SuzuneV2.modules.helper_funcs.misc import send_to_list


@run_async
@support_plus
async def gban(pbot, message):
    await pbot.send_message(
            chat_id=EVENT_LOGS,
            text=(
                f"🚨GBAN NOTIFICATION🚨\n"
        f"<b>⭐From:</b> <code>{chat_origin}</code>\n"
        f"<b>⭐Admin:</b> {mention_html(user.id, user.first_name)}\n"
        f"<b>⚠️Banned User:</b> {mention_html(user_chat.id, user_chat.first_name)}\n"
        f"<b>⚠️Banned User ID:</b> <code>{user_chat.id}</code>\n"
        f"<b>✅Event Stamp:</b> <code>{current_time}</code>"
            )
        )
        
        
        

GBAN_HANDLER = CommandHandler("gban", gban)

dispatcher.add_handler(GBAN_HANDLER)