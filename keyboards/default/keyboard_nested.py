from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='А'),
            KeyboardButton(text='Б'),
        ],
        [
            KeyboardButton(text='В')
        ],
        [
            KeyboardButton(text='/help'),
            KeyboardButton(text='/menu')
        ]
    ],
    resize_keyboard=True
)