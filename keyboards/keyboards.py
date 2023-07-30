from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON_RU

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

# Инициализация билдера кнопок
yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# Добавим кнопки в билдер
yes_no_kb_builder.row(button_yes, button_no, width=2)
# создаю клавиатуру с этими кнопками
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

# Создаем кнопки
buttons: list[KeyboardButton] = [KeyboardButton(text=LEXICON_RU['rock']), KeyboardButton(text=LEXICON_RU['scissors']), KeyboardButton(text=LEXICON_RU['paper'])]
# Инициализация билдера кнопок
game_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
game_kb_builder.row(*buttons, width=1)
# создаю клавиатуру
game_kb: ReplyKeyboardMarkup = game_kb_builder.as_markup(resize_keyboard=True)