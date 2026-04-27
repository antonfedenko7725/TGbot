
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineQuery, InlineQueryResultVoice

# Railway підтягне токен з Variables
API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Цей блок коду буде надсилати тобі ID, коли ти кидаєш боту голосове або файл
@dp.message_handler(content_types=['voice', 'audio', 'document'])
async def get_file_id(message: types.Message):
    file_id = None
    if message.voice:
        file_id = message.voice.file_id
    elif message.audio:
        file_id = message.audio.file_id
    
    if file_id:
        await message.reply(f"Ось ID твого файлу:\n`{file_id}`", parse_mode="Markdown")

# Твоє Inline-меню (додавай нові ID сюди)
@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):
    results = [
        # ПЕРШЕ ГОЛОСОВЕ
        InlineQueryResultVoice(
            id='1',
            voice_file_id='AwACAgIAAxkBAAMTae...', # Встав старий ID сюди
            title='Назва 1'
        ),
        # ДРУГЕ ГОЛОСОВЕ (від Єгора)
        InlineQueryResultVoice(
            id='2',
            voice_file_id='AwACAgIAAxkBAAMVae...', # Встав ID Єгора зі скриншоту сюди
            title='Від Єгора'
        ),
    ]
    await bot.answer_inline_query(inline_query.id, results=results, cache_time=1)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
