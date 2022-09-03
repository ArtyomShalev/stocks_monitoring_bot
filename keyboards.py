from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


inline_btn_hi = InlineKeyboardButton('Hello! 👋', callback_data='btn_hi')
inline_kb1_hi = InlineKeyboardMarkup().add(inline_btn_hi)


inline_kb_stocks = InlineKeyboardMarkup(row_width=2)
inline_btn_sber = InlineKeyboardButton('Cбер', callback_data='btn_sber')
inline_btn_vtb = InlineKeyboardButton('ВТБ', callback_data='btn_vtb')
inline_btn_mosexch = InlineKeyboardButton('Московская биржа', callback_data='btn_mosexch')
inline_kb_stocks.add(inline_btn_sber, inline_btn_vtb)
inline_kb_stocks.row(inline_btn_mosexch)
# inline_kb_full.row(inline_btn_sber, inline_btn_vtb)
