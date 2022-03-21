from aiogram import types
from loader import dp
from keyboards.default import kb_test

@dp.message_handler(text='Я НОВАЯ')
async def command_start(message: types.Message):
    await message.answer('Новая открыта', reply_markup=kb_test)

