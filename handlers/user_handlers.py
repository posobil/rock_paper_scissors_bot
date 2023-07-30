from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import game_kb, yes_no_kb
from lexicon.lexicon import LEXICON_RU
from services.services import get_bot_choice, get_winner

# Инициализируем роутер уровня модуля
router: Router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=f'<b>Привет, </b> <b>{message.from_user.username}!</b>{LEXICON_RU["/start"]}', reply_markup=yes_no_kb)

# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)

# Этот хэндлер срабатывает на команду yes_button
@router.message(F.text==LEXICON_RU['yes_button'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)

# Этот хэндлер срабатывает на команду no_button
@router.message(F.text==LEXICON_RU['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'], reply_markup=yes_no_kb)

# Этот хэндлер срабатывает на любую из игровых кнопок
@router.message(F.text.in_([LEXICON_RU['rock'], LEXICON_RU['paper'], LEXICON_RU['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                              f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)
