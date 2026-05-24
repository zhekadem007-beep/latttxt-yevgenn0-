import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Твій токен (залишаємо як є)
TOKEN = '8973832261:AAEpZ9QuxdKHCXvaj_48r-iWl9BTLAP8bnc'

# Налаштування логування
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()


# Головне меню
def get_main_keyboard():
    builder = InlineKeyboardBuilder()

    # ВИПРАВЛЕНО: Прибрано фігурні дужки та знак @ з URL-посилань
    builder.row(types.InlineKeyboardButton(text="🤖 Замовити бота (Python)", url="https://t.me/latttxt"))
    builder.row(types.InlineKeyboardButton(text="🎨 Замовити дизайн / Монтаж відео", url="https://t.me/yevgenn0"))

    # Інформаційні кнопки
    builder.row(types.InlineKeyboardButton(text="📋 Що саме я роблю? (Послуги)", callback_data="my_services"))
    builder.row(types.InlineKeyboardButton(text="📁 Приклади робіт (Портфоліо)", callback_data="portfolio"))
    builder.row(types.InlineKeyboardButton(text="⭐ Відгуки клієнтів", callback_data="reviews"))
    return builder.as_markup()


# Кнопка "Назад"
def get_back_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="main_menu"))
    return builder.as_markup()


# Хендлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = (
        f"👋 Привіт, {message.from_user.full_name}!\n\n"
        "Цей бот — моє особисте портфоліо та візитка.\n"
        "Тут ти можеш переглянути мої роботи, дізнатися про послуги або відразу замовити розробку чи дизайн.\n\n"
        "📌 Обирай потрібний розділ меню нижче 👇"
    )
    await message.answer(text=welcome_text, reply_markup=get_main_keyboard())


# Обробка натискань на кнопки меню
@dp.callback_query()
async def callback_handler(callback: types.CallbackQuery):
    await callback.answer()

    if callback.data == "main_menu":
        welcome_text = (
            "📌 Головне меню.\nОбирай потрібний розділ нижче 👇"
        )
        await callback.message.edit_text(text=welcome_text, reply_markup=get_main_keyboard())

    elif callback.data == "my_services":
        text = (
            "✨ **Перелік моїх послуг:**\n\n"
            "🤖 **Розробка Telegram-ботів:**\n"
            "• Створюю надійних ботів на Python.\n"
            "• Боти-магазини, анкети, інтеграція з ШІ (Gemini/ChatGPT), адмін-панелі та автоматизація.\n\n"
            "🎨 **Професійний дизайн та відеомонтаж:**\n"
            "• **After Effects:** Складна анімація, круті ефекти та моушн-дизайн.\n"
            "• **Premiere Pro:** Якісний монтаж відео (для YouTube, Reels, Shorts, ТікТок).\n"
            "• **Photoshop:** Яскраві прев'ю (обкладинки) для відео, банери, оформлення соцмереж.\n\n"
            "💡 _Щоб зробити замовлення, просто натисни відповідну кнопку в головному меню!_"
        )
        await callback.message.edit_text(text=text, reply_markup=get_back_keyboard(), parse_mode="Markdown")

    elif callback.data == "portfolio":
        text = (
            "📁 **Моє портфоліо та приклади робіт**\n\n"
            "Всі мої готові проєкти, приклади монтажу, дизайну та коду зібрані тут:\n"
            "👉 [Портфоліо](https://t.me/zhekaportfolio)\n\n"
            "Якщо хочеш побачити більше специфічних прикладів — запитуй прямо в особистих повідомленнях!"
        )
        await callback.message.edit_text(text=text, reply_markup=get_back_keyboard(), parse_mode="Markdown",
                                         disable_web_page_preview=True)

    elif callback.data == "reviews":
        text = (
            "⭐ **Відгуки клієнтів**\n\n"
            "Почитати відгуки людей, які вже працювали зі мною та замовляли послуги, можна в окремому канале:\n\n"
            "👉 [ДИВИТИСЬ ВІДГУКИ](https://t.me/zhekabio00)\n\n"
            "Кожен відгук реальний! Буду вдячний, якщо після нашої співпраці ти теж залишиш свій фідбек."
        )
        await callback.message.edit_text(text=text, reply_markup=get_back_keyboard(), parse_mode="Markdown",
                                         disable_web_page_preview=True)


# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
