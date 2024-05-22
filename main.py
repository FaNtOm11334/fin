from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton('Отправь фото Рублева')
button_2 = KeyboardButton('Перейти на некст клавиатуру')
keyboard.add( button_1, button_2)

keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
button_3 = KeyboardButton('Отправь фото Алькараса')
button_4 = KeyboardButton('Вернутся на первую клавиатуру')
keyboard_2.add( button_3, button_4)

async def set_commands(bot:Bot):
    commands = [
        types.BotCommand(command='/start', description= 'Команда для того чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того чтобы Санек стал не скуфом')
    ]

    await bot.set_my_commands(commands)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я твой первый ЭХО бот', reply_markup= keyboard)

@dp.message_handler(lambda message: message.text == 'Отправь фото Рублева')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://airbet.ru/wp-content/uploads/2021/04/20-min-3.jpg',  caption= 'Вот Андрей')


@dp.message_handler(lambda message: message.text == 'Перейти на некст клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото Алькараса', reply_markup=keyboard_2)

@dp.message_handler(lambda message: message.text == 'Отправь фото Алькараса')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://pbs.twimg.com/media/FSFW5s5XsAAz-v_?format=jpg&name=4096x4096', caption= 'Карлитос')

@dp.message_handler(lambda message: message.text == 'Вернутся на первую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото Алькараса', reply_markup=keyboard)

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Я могу помочь тебе')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup=on_startup)
