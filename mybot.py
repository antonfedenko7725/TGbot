
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineQuery, InlineQueryResultCachedVoice

# ВСТАВ СВІЙ ТОКЕН ТУТ
TOKEN = '8751226762:AAG0h7nFQHfs1FKt6k8hK4fxyrF2CyQiyYU'

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Словник твоїх голосових: ID файлу та заголовок
VOICES = [
    {"id": "1", "file_id": "AwACAgIAAxkBAAMFaesou7exlEXsdZu0XLcJprde-_IAAp4FAAIGrSlIF8XC58oX28U7BA", "title": "Вкрали брілки"},
    {"id": "2", "file_id": "AwACAgIAAxkBAAMHaeso1CDabXc2Uiqs0p8kNeGhBoEAAhYHAAKJSWFKcLZu2p014e47BA", "title": "Антон набухався"},
    {"id": "3", "file_id": "AwACAgIAAxkBAAMJaeso3Lz5wr_uMPrU4ssEIL6kFf4AAqkFAALaM4hKyj751T-i3Xw7BA", "title": "де я"},
    {"id": "4", "file_id": "AwACAgIAAxkBAAMLaeso6ZNTNvVfgmJ54wv_OFX5csIAAh4KAAJg9ShLWnH3OcIAAf-LOwQ", "title": "Меклеш"},
    {"id": "5", "file_id": "AwACAgIAAxkBAAMNaespCtZUjh4eF7j-o0YWepaNj6sAAkIJAAIQ3ZhJAiMQ5cjjN8A7BA", "title": "Діма на пізда"},
    {"id": "6", "file_id": "AwACAgIAAxkBAAMPaespG_E1X9LIwNCYcoqDTVqN45sAAkUJAAIQ3ZhJpVII0FP5hRc7BA", "title": "Діма тут така срака"},
    {"id": "7", "file_id": "AwACAgIAAxkBAAMRaespJ6_pj9OrgEe3fkbUJQcssMAAAgUHAAKJSWFKx0HP2AdoI1o7BA", "title": "Антон прийшов чи нє"},
    {"id": "8", "file_id": "AwACAgIAAxkBAAMTaespMafhRZ0bhnXwGt13t9XjJdQAAhoHAAKJSWFKRplM3SRq5f47BA", "title": "Я п'яний в щі"},
    {"id": "9", "file_id": "AwACAgIAAxkBAAMVaespQzXQ8vWM9bbx_P2m106kVyIAAmMGAAL9l7hLz9BsJt4s6MY7BA", "title": "Шева тут пізда"},
]

# Обробник Inline-запитів
@dp.inline_query()
async def inline_voice_handler(inline_query: InlineQuery):
    results = []
    
    for voice in VOICES:
        results.append(
            InlineQueryResultCachedVoice(
                id=voice["id"],
                voice_file_id=voice["file_id"],
                title=voice["title"]
            )
        )
    
    # Відправляємо результати (максимум 50 за раз за правилами Telegram)
    await inline_query.answer(results, cache_time=1)

async def main():
    print("Бот запущений у Inline-режимі! Можна тестувати в чатах.")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())