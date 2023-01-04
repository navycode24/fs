# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/userbotch & t.me/ramsupportt
# Add Code FROM 3-BUTTONS <https://github.com/ramadhani892/3-BUTTONS

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_GROUP2
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink2),
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink),
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink),
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons

def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink),
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2:
        buttons = [
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink),
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
