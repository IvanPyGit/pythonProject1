from loader import dp
from aiogram import types

from keyboards.inline import ikb_menu

@dp.message_handler(text='Inline!')
async def show_inline_menu(message: types.Message):
    await message.answer('Инлайн кнопки ниже', reply_markup=ikb_menu)