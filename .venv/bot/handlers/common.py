from aiogram import F, Router, types
from aiogram.filters import Command, CommandStart
from aiogram.types import Message



router = Router()


@router.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer(text='Привет! Я бот для расписания.\n\n Чтобы получить расписание, напиши /schedule\n\nЧтобы начать заново, напиши /start')

