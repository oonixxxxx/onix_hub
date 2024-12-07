from aiogram import F, Router

from aiogram.filters import CommandStart
from aiogram.types import Message
from app.other.buttons import Buttons

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello! Я бот длля продажи предметов в локальном магазине \n что бы перейти к выполнению заказа напиши 'Корзина 🛒'", 
                         reply_markup=Buttons.menu_button)

@router.message(F.text == 'В меню🧑🏿‍💻🗂')
async def get_menu(message: Message):
    await message.answer(str(main_page_text), reply_markup=Buttons.menu_button)