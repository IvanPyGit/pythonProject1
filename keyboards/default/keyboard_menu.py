from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Первая'),
            KeyboardButton(text='Вторая'),
        ],
        [
            KeyboardButton(text='Строка')
        ],
        [
            KeyboardButton(text='Inline!'),
            KeyboardButton(text='Я НОВАЯ')
        ]
    ],
    resize_keyboard=True
)