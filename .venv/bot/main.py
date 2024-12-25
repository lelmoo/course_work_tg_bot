import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from handlers import common, schedule
from config import BOT_TOKEN


logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))

    dp = Dispatcher()

    dp.include_router(common.router)
    dp.include_router(schedule.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())