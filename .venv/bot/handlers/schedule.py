from aiogram import F, Router, types
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from bot.services.schedule import get_schedule, get_available_classes
from bot.keyboards.class_choise_kb import create_classes_keyboard

router = Router()
CLASS_DATA = dict()

def format_schedule(schedule, day):
    day_schedule = [row for row in schedule if row[0] == day]
    if not day_schedule:
        return f"На {day} расписание отсутствует."

    return "\n".join(
        f"{row[3]}: {row[4]}" for row in day_schedule
    )


@router.message(Command(commands='schedule'))
async def process_schedule_command(message: Message):
    available_classes = sorted(get_available_classes('number'))
    await message.answer(
        text=f'Выбери класс:',
        reply_markup=create_classes_keyboard(available_classes, 'number')
    )


@router.callback_query(F.data.startswith('number'))
async def process_number_press(callback):
    CLASS_DATA['class_number'] = callback.data.split('_')[1]
    available_classes = get_available_classes('letter', CLASS_DATA['class_number'])
    await callback.message.edit_text(
        text='Выбери букву класса:',
        reply_markup=create_classes_keyboard(available_classes, 'letter')
    )
    await callback.answer()


@router.callback_query(F.data.startswith('letter'))
async def process_number_press(callback):
    CLASS_DATA['class_letter'] = callback.data.split('_')[1]
    available_days = get_available_classes('day', CLASS_DATA['class_number'], CLASS_DATA['class_letter'])
    await callback.message.edit_text(
        text='Выбери день недели',
        reply_markup=create_classes_keyboard(available_days, 'day')
    )
    await callback.answer()


@router.callback_query(F.data.startswith('day'))
async def process_day_press(callback):
    CLASS_DATA['class_day'] = callback.data.split('_')[1]

    schedule = get_schedule(CLASS_DATA['class_number'], CLASS_DATA['class_letter'])

    if schedule:
        day_schedule = format_schedule(schedule, CLASS_DATA['class_day'])
        await callback.message.edit_text(text=f"{day_schedule}")
    else:
        await callback.message.edit_text(text=f"Расписание для {CLASS_DATA['class_number']}{CLASS_DATA['class_letter']} не найдено.")
    await callback.answer()