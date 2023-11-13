import asyncio
from handlers import admin_handlers, user_handlers
from config import load_config, Config, set_main_menu
from aiogram import Bot, Dispatcher


async def main() -> None:
    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.bot.token,
              parse_mode='HTML')
    await set_main_menu(bot)
    dp = Dispatcher()

    # Регистрируем роутеры в диспетчере
    dp.include_router(admin_handlers.router)
    dp.include_router(user_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    print('Бот запущен')
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())



if __name__ == '__main__':
    asyncio.run(main())
