from aiogram import F, Router

from aiogram.filters import CommandStart
from aiogram.types import Message

from app.other.buttons import Buttons
from app.other.functions import Functions
from app.other.database import Promo
from app.texts.basic_text import Texts

router = Router()

promos = Promo.promos

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello! Я бот длля продажи предметов в локальном магазине \n что бы перейти к выполнению заказа напиши 'Корзина 🛒'", 
                         reply_markup=Buttons.menu_button)

@router.message(F.text == 'В меню🧑🏿‍💻🗂')
async def get_menu(message: Message):
    await message.answer(str(Texts.main_page_text), reply_markup=Buttons.menu_button)

@router.message(F.text == 'Конткты')
async def get_contact(message: Message):
    await message.answer(str(Texts.contact_text), reply_markup=Buttons.contact_button)

@router.message(F.text == 'Ввести промокод')
async def input_promocode(message: Message):
    await message.answer('Введите промокод')

@router.message(F.text == 'Получить реферальную ссылку')
async def get_referral_link(message: Message):
    await message.answer(str(Functions.get_referal()))