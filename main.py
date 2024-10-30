from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = 'Enter your key from botfather'

bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text = ['Привет'])
async def all_message(message):
    print("Мы получили сообщение")
    await message.answer('Введите команду /start, чтобы начать общение.')


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! я Бот помогающий твоему здоровью.')
    await message.answer('Привет! я Бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_message(message):
    await message.answer(text=message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)