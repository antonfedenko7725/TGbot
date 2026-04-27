import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineQuery, InlineQueryResultCachedVoice

# Краще використовувати змінні оточення для безпеки, але залишаю твій варіант для зручності
TOKEN = os.getenv("BOT_TOKEN") or '8751226762:AAG0h7nFQHfs1FKt6k8hK4fxyrF2CyQiyYU'

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
    {"id": "10", "file_id": "AwACAgIAAxkBAAMXae9B4Lc80CBSGyWCFFY4QfluUpwAApWLAAKM3FBJWYAhvYGkkjY7BA", "title": "мєн ю кен"},
    {"id": "11", "file_id": "AwACAgIAAxkBAAMbae9E00TnIfge5yKlmAlztvMsoAQAAq6LAAKM3FBJIgS4yDjaf807BA", "title": "ти сука дебіл"},
    {"id": "12", "file_id": "AwACAgIAAxkBAAMdae9FIz1t5kVM8adPBVKHDRfJJoAAAoADAAK8mylLF7APgtQAAYgAATsE", "title": "Я блять питаю"},
    {"id": "13", "file_id": "AwACAgIAAxkBAAMgae9FjnWou4GL_W9Oa_5R1hGaUF8AAnQEAALBv3hI5Ynw8fcgwcU7BA", "title": "Го бухать нахуй"},
    {"id": "14", "file_id": "AwACAgIAAxkBAAMiae9Fug39a6jQiVqA8bbN2PDsHYoAAtgDAAJPHNhIMz1-S0pO6cA7BA", "title": "Забув як ти водку жрав"},
    {"id": "15", "file_id": "AwACAgIAAxkBAAMkae9F3r0QDMjbMdwK_rxczIzstDEAAqgDAALsjZhJpPUDYqXwlFU7BA", "title": "Вадім підар"},
    {"id": "16", "file_id": "AwACAgIAAxkBAAMmae9F_lJY9PaG-dVkHBkoL_WVfP4AAvICAALlJ_hLZeV9bxEtzoI7BA", "title": "Пососи грєбєнь"},
    {"id": "10", "file_id": "AwACAgIAAxkBAAMoae9GZMoehSj0Z6F3qfAMfPpDSDoAAjMCAALaPAhJccr1IjGxWaI7BA", "title": "Пачка сігарєт"},
    
]

# --- НОВИЙ БЛОК: СЛУХАЄМО НОВІ ГОЛОСОВІ ---
@dp.message(F.voice | F.audio)
async def handle_new_audio(message: types.Message):
    file_id = message.voice.file_id if message.voice else message.audio.file_id
    next_id = len(VOICES) + 1
    
    # Формуємо текст, який зручно скопіювати в код
    response_text = (
        f"✅ **Отримано нове аудіо!**\n\n"
        f"Скопіюй цей рядок і додай у список VOICES:\n\n"
        f"`{{\"id\": \"{next_id}\", \"file_id\": \"{file_id}\", \"title\": \"НОВА_НАЗВА\"}},`"
    )
    await message.reply(response_text, parse_mode="Markdown")

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
    await inline_query.answer(results, cache_time=1)

async def main():
    print("Бот запущений! Надсилайте голосові в чат для отримання ID.")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
