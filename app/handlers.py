from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message,CallbackQuery

import app.keyboards as kb


router = Router()

# Словари для хранения данных о пользователях
user_ages = {}
user_male = {}
age_asked = set()  # Множество для отслеживания пользователей, у которых уже был задан вопрос о возрасте
user_films = {}    # Словарь для хранения выбранных фильмов пользователей

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f'Привет, {message.from_user.first_name}, этот бот поможет выбрать тебе фильм на основе твоих предпочтений. Для начала, какой у тебя пол?', 
        reply_markup=kb.kb_male
    )

@router.message(F.text.in_(['Мужской 👨🏻‍🦰', 'Женский 👩🏻']))
async def ask_male(message: Message):
    user_id = message.from_user.id
    male = message.text
    
    # Сохраняем пол
    user_male[user_id] = male

    # Отмечаем, что пользователя спросили о возрасте
    age_asked.add(user_id)

    await message.answer('Сколько тебе лет? Пожалуйста, введи свой возраст.', reply_markup=None)

@router.message(F.text.isdigit())
async def save_age(message: Message):
    user_id = message.from_user.id
    age = int(message.text)
    
    # Сохраняем возраст пользователя
    user_ages[user_id] = age
    
    # Удаляем пользователя из множества age_asked, т.к. возраст введен корректно
    age_asked.discard(user_id)

    await message.answer(f'Спасибо! Твой возраст: {age} лет.')
    await message.answer('Выберите дальнейшие действия:', reply_markup=kb.main)

# Обработчик для неправильного ввода возраста, если возраст еще не был указан
@router.message(lambda message: message.from_user.id in age_asked)
async def invalid_age_input(message: Message):
    await message.answer("Пожалуйста, введите свой возраст числом.")

@router.message(F.text.in_(['Подобрать фильм 🎞']))
async def film_selection(message: Message):
    # Сохраняем сообщение для редактирования
    selection_message = await message.answer(
        f'{message.from_user.first_name}, давай проведем экспресс подборку, чтобы настроить алгоритм под тебя. Как только ты выберешь 5 фильмов, бот начнет работать в стандартном режиме. Выбери фильмы, которые ты смотрел или хотел бы посмотреть',
        reply_markup=await kb.inline_film()
    )
    
    # Сохраняем идентификатор сообщения
    user_films[message.from_user.id] = {
        'selection_message_id': selection_message.message_id,
        'films': []
    }

@router.callback_query(lambda callback: callback.data in kb.films_for_selection)
async def handle_film_selection(callback: CallbackQuery):
    user_id = callback.from_user.id
    selected_film = callback.data
    
    # Инициализация списка фильмов для пользователя, если его еще нет
    if user_id not in user_films:
        user_films[user_id] = {
            'selection_message_id': None,
            'films': []
        }

    # Добавляем фильм в список, если он еще не был выбран
    if selected_film not in user_films[user_id]['films']:
        user_films[user_id]['films'].append(selected_film)

    # Проверяем, выбрано ли 5 фильмов
    films_count = len(user_films[user_id]['films'])
    films_list = ', '.join(user_films[user_id]['films'])  # Формируем строку со списком фильмов
    message_text = f'Выбрал: {selected_film}. Всего выбрано фильмов: {films_count}.\nТы выбрал: {films_list}'

    if films_count >= 5:
        message_text += '\nТеперь бот начнет работать в стандартном режиме.'
        # Здесь можно добавить логику для перехода к следующему этапу

        # Убираем клавиатуру
        await callback.message.edit_text(message_text, reply_markup=None)
    else:
        # Обновляем сообщение и оставляем клавиатуру
        await callback.message.edit_text(message_text, reply_markup=await kb.inline_film())



