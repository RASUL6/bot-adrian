import logging
from aiogram import Bot, types, executor, Dispatcher
from aiogram.dispatcher.filters import Text
bot = Bot(token='5418995392:AAEJ98Pv1FdTYQKrxd7lhax8Zm0vhIPiCy0')
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    await message.reply("Здравствуйте вас приветсвует поисковой бот,как вас зовут?")
    
'''@dp.message_handler()
async def any_text_message2(message: types.Message):
    await message.answer(f"Привет, <b>{fmt.quote_html(message.text)}</b>", parse_mode=types.ParseMode.HTML)
    await message.answer(fmt.text("Привет,", fmt.hbold(message.text)), parse_mode=types.ParseMode.HTML)'''

    
@dp.message_handler(commands=["help"])
async def start(message:types.Message):
    await message.reply("чем могу помочь?")
    
@dp.message_handler(commands="next1")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="продажи на нефтяном рынке")
    keyboard.add(button_1)
    await message.answer("чем могу помочь?", reply_markup=keyboard)
    
@dp.message_handler(Text(equals="продажи на нефтяном рынке"))
async def with_puree(message: types.Message):
    await message.reply("хорошо")
    
@dp.message_handler(commands=["next2"])
async def start(message:types.Message):
    await message.reply("могу предложить пару сайтов")
    
@dp.message_handler(commands="inline_url")
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="BRANT", url="https://broker.ru/quotes/brent"),
        types.InlineKeyboardButton(text="WTI", url="https://index.minfin.com.ua/markets/oil/wti/")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Кнопки-ссылки", reply_markup=keyboard)
    
@dp.message_handler(commands=["work"])
async def start1(message:types.Message):
    await message.reply("хотите ли вы получать информацию с этих сайтов на цену нефти?")
if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)
    

