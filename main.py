import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
TON_WALLET = os.getenv("TON_WALLET")
LOG_CHAT_ID = int(os.getenv("LOG_CHAT_ID", 0))

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("🤖 IronTONBot активен. Ожидаем задания...")

@dp.message_handler(commands=["task"])
async def task(message: types.Message):
    task_description = "🔍 Задача найдена: выполнить действие X\n📤 Отправка решения..."
    await message.answer(task_description)

    if LOG_CHAT_ID:
        await bot.send_message(LOG_CHAT_ID, f"📥 Пользователь @{message.from_user.username} запустил задачу.")

    await message.answer("✅ Выполнено! Ожидаем оплату в TON.")

if __name__ == "__main__":
    executor.start_polling(dp)
