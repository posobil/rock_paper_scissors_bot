from aiogram import Router

from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер будет срабатывать на любые ваши сообщения
@router.message()
async def send_echo(message: Message):
        await message.reply(text=LEXICON_RU['other_answer'])
