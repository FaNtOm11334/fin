from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_1,get_keyboard_2
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

keyboard_inline = InlineKeyboardMarkup(row_width=1)
but_inline = InlineKeyboardButton('Посмотреть',url='https://www.tennis24.com/')
but_inline2 = InlineKeyboardButton('Посмотреть',url='https://www.tennis24.com/')
keyboard_inline.add(but_inline,but_inline2)
async def set_commands(bot:Bot):
    commands = [
        types.BotCommand(command='/start', description= 'Команда для того чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того чтобы Санек стал не скуфом')
    ]

    await bot.set_my_commands(commands)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я твой первый ЭХО бот', reply_markup= get_keyboard_1)

@dp.message_handler(lambda message: message.text == 'Отправь фото Рублева')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://airbet.ru/wp-content/uploads/2021/04/20-min-3.jpg',  caption= 'Вот Андрей', )


@dp.message_handler(lambda message: message.text == 'Перейти на некст клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото Алькараса', reply_markup=get_keyboard_2)

@dp.message_handler(lambda message: message.text == 'Отправь фото Алькараса')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://pbs.twimg.com/media/FSFW5s5XsAAz-v_?format=jpg&name=4096x4096', caption= 'Карлитос')

@dp.message_handler(lambda message: message.text == 'Вернутся на первую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото Алькараса', reply_markup=get_keyboard_1)

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
