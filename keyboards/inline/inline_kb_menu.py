from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Текст', callback_data='Ага, он'),
                                        InlineKeyboardButton(text='Ссылка', url='https://qna.habr.com/q/1016134')
                                    ]
                                ])