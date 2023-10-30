from aiogram import Bot
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import BotCommand

button_1: KeyboardButton = KeyboardButton(text='Старт')
button_2: KeyboardButton = KeyboardButton(text='Правила')

keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_1], [button_2]],
                                                    resize_keyboard=True)

async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(
                                    command=command,
                                     description=description
                                     ) for command,
                                     description in {'/start': 'Start', '/help': 'Help'}.items()
                        ]
    await bot.set_my_commands(main_menu_commands)