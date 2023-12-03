import aiogram
from aiogram import Bot, Dispatcher, types,executor



API_TOKEN = '6487764885:AAHfG_A4geA7k5thcG_UmIQXDseoL2gitDk'



bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])

async def start_comand(message: types.Message):
    
    await bot.send_message(message.chat.id,text="Цей бот допомагає згадати дати\n днів народжень ")
    sticker_id = 'CAACAgIAAxkBAAEK4iplbECZn3NpKxkfgUfR_6vwpRvUtgACwzoAAm6osEm29Xj72bQUCjME'
    await bot.send_sticker(message.chat.id,sticker_id)


@dp.message_handler(commands=['birthday'])
async def send_commands(message: types.Message):
    commands_list = [
        'Серий - 18 липня',
        'Паша - 12 липня',
        'Валя - 3 квітня',
        'Бодя - 10 жовтня',
        'Славік - 14 лютого',
        'Леша - 31 березня' 
    ]
    formatted_list = "\n".join(commands_list)
   
    await bot.send_message(message.chat.id,text=f'Дні народження\n {formatted_list}')



    
executor.start_polling(dp, skip_updates=True)
