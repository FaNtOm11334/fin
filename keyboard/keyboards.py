from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton
def get_keyboard_1():
 keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
 button_1 = KeyboardButton('Отправь фото Рублева')
 button_2 = KeyboardButton('Перейти на некст клавиатуру')
 keyboard.add( button_1, button_2)
 return keyboard



def get_keyboard_2():
 keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
 button_3 = KeyboardButton('Отправь фото Алькараса')
 button_4 = KeyboardButton('Вернутся на первую клавиатуру')
 keyboard_2.add( button_3, button_4)
 return_keyboard_2