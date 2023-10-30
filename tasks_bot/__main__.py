import asyncio
import logging
from aiogram import Dispatcher, Bot 
from config import Config, load_config
from handlers import admin_handlers, commands_handlers, others_handlers
from keyboards import set_main_menu

async def main():
    logging.basicConfig(level=logging.DEBUG)
    config: Config = load_config('tasks_bot/.env')
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    dp.include_router(admin_handlers.router)
    dp.include_router(commands_handlers.router)
    dp.include_router(others_handlers.router)

    await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    #try:
    asyncio.run(main())   
    # except (KeyboardInterrupt, SystemExit):
    #     print('Bot stopped')     