from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexic.lexicon import LEXICON_RU


buttons_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
buttons_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(buttons_yes, buttons_no)

yes_no_kb = yes_no_kb_builder.as_markup(one_time_keyboard=True,
                                        resize_keyboard=True)

button_rock: KeyboardButton = KeyboardButton(text=LEXICON_RU["rock"])
button_paper: KeyboardButton = KeyboardButton(text=LEXICON_RU["paper"])
button_scissors: KeyboardButton = KeyboardButton(text=LEXICON_RU["scissors"])

game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_rock],
                                                             [button_paper],
                                                             [button_scissors]],
                                                   resize_keyboard=True)
