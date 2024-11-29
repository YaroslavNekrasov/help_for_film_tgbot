Документация Telegram-бота по подбору фильмов
Общая информация
Бот создан для помощи пользователям в подборе фильмов на основе их предпочтений. Пользователь вводит свои данные (пол, возраст) и выбирает фильмы, которые он уже смотрел или хотел бы посмотреть. На основании этих данных нейросеть рекомендует фильмы, подходящие для просмотра.

Основные функции
Приветственное сообщение
При вводе команды /start бот приветствует пользователя и предлагает выбрать пол.

Сбор данных о пользователе

Пол: Пользователь выбирает между "Мужской" или "Женский".
Возраст: Бот запрашивает возраст пользователя числом.
Выбор фильмов
Пользователь выбирает 5 фильмов из предложенного списка. Эти данные используются для настройки алгоритма рекомендаций.

Формирование рекомендаций
После выбора фильмов бот переходит к стандартному режиму, в котором формирует рекомендации на основе введенных данных.

Структура проекта
1. Модуль handlers.py
Содержит обработчики событий, такие как команды и взаимодействие с пользователем.

Основные обработчики:
cmd_start: Приветствие и запрос пола.
ask_male: Сохранение пола пользователя и запрос возраста.
save_age: Проверка и сохранение возраста.
film_selection: Начало выбора фильмов и создание инлайн-клавиатуры.
handle_film_selection: Обработка выбора фильмов, проверка количества выбранных фильмов.
Переменные:
user_ages: Хранит возраст пользователей.
user_male: Хранит информацию о поле пользователей.
age_asked: Следит за тем, кому задавался вопрос о возрасте.
user_films: Хранит список выбранных фильмов для каждого пользователя.
2. Модуль keyboards.py
Содержит функции и переменные для создания клавиатур.

Основные клавиатуры:
kb_male: Клавиатура для выбора пола (Мужской/Женский).
main: Главное меню с выбором действий ("Подобрать фильм", "Понравившиеся фильмы").
inline_film(): Инлайн-клавиатура с фильмами для выбора.
Переменные:
films_for_selection: Список фильмов, доступных для выбора.
Используемые технологии
Python: Основной язык программирования.
aiogram: Фреймворк для работы с Telegram Bot API.
Инлайн-клавиатуры: Для выбора фильмов и взаимодействия с ботом.
