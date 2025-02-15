from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, \
    KeyboardButtonPollType, KeyboardButtonRequestUser
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiohttp import request

BOT_API_TOKEN = "7318261107:AAFfftEzl1ULuOHibcR_BCIGbzCDRLV9YBc"

bot = Bot(token=BOT_API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()

@router.message(Command("start"))
async def cmd_start_2(message: Message):
    await message.answer('Запуск сообщения по команде \start используя фильтр Command()')
    keyboard = InlineKeyboardMarkup(keyboard=[
        [InlineKeyboardMarkup(text="каталог товаров", callback_data="catalog")],
        [InlineKeyboardMarkup(text="партнерство", callback_data="reviews")],
        ])

    await message.answer('daddsd', reply_markup=keyboard)

@router.callback_query(lambda c: c.data in ['contact'])
async def handle_callback_query(callback_query: types.CallbackQuery):
    data = callback_query.data
    if data=='contact':
        await callback_query.message.answer('sssss')


@dp.message(Command('start'))
async def hello(message: Message):
    kb = [
        [
            KeyboardButton(text="С пюрешкой"),
            KeyboardButton(text="Без пюрешки")
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    await message.answer("как подавать котлеты?", reply_markup=keyboard)

@dp.message(F.text.lower() == "с пюрешкой")
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!")

@dp.message(F.text.lower() == "Без пюрешки")
async def without_puree(message: Message):
    await message.reply("Так невкусно!")
@dp.message(Command("reply_builder"))
async def reply_builder(message: Message):
    builder = ReplyKeyboardBuilder()
    for i in range(1, 17):
        builder.add(KeyboardButton(text=str(i)))
    builder.adjust(4)
    await message.answer(
        "Выберите число:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )

@dp.message(Command("special_buttons"))
async def cmd_special_buttons(message: Message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Запросить геолокацию", request_location=True),
        KeyboardButton(text="запросить контакт", request_contact=True),
    )
    builder.row(KeyboardButton(
        text="создать викторину",
        request_poll=KeyboardButtonPollType(type="quiz"))
    )
    builder.row(
        KeyboardButton(
        text="Выбрать премиум пользователя",
        request_user=KeyboardButtonRequestUser(
            request_id=1,
            user_is_premium=True
        )
        ),
    KeyboardButton(
        text="Выбрать супергруппу с форумами",
        request_chat=types.KeyboardButtonRequestChat(
            request_id=2,
            chat_is_channel=False,
            chat_is_forum=True
        )
    )
    )



    await message.answer(
        "Выберите:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )



dp.include_router(router)


async def main():
    await bot.delete_webhook()
    await dp.start_polling(bot)

if __name__ == "__main_-":
    asyncio.run(main())


