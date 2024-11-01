from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

kb_male = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = 'Мужской 👨🏻‍🦰'),
    KeyboardButton(text = 'Женский 👩🏻')]
],
                resize_keyboard=True,
                one_time_keyboard=True,
                input_field_placeholder='Выбеите свой пол')


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = 'Подобрать фильм 🎞'),
    KeyboardButton(text = 'Понравившиеся фильмы ❤️')]
],
                resize_keyboard=True,
                one_time_keyboard=True,
                input_field_placeholder='Выбирите действие в меню')

films_for_selection = ['Хемилгтон','Расследование 13', 'Человеческие отношения','Будь честным','Знак вомпира','Красная бумага','Паутина грёз','Афганские рыцари','Дезертир',]

async def inline_film():
    keyboard = InlineKeyboardBuilder()
    for film in films_for_selection:
        keyboard.add(InlineKeyboardButton(text=film, callback_data=film))  # Используем callback_data для передачи данных
    return keyboard.adjust(2).as_markup()

