import telegram
from key_buttons import tele_buttons, timetable_buttons, teachers_buttons


def main_menu_keyboard():
    keyboard=([
        [
        telegram.KeyboardButton(tele_buttons[0]),
        ],
        [telegram.KeyboardButton(tele_buttons[1]),],
        [telegram.KeyboardButton(tele_buttons[2]),],
        [
        telegram.KeyboardButton(tele_buttons[3]),],
    ])
    return telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)

def timetable_menu_keyboard():
    keyboard=([
        [
        telegram.KeyboardButton(timetable_buttons[0]),
        telegram.KeyboardButton(timetable_buttons[1]),
        telegram.KeyboardButton(timetable_buttons[2]),
        telegram.KeyboardButton(timetable_buttons[3]),
        ]
    ])
    return telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)

def teachers_menu_keyboard():
    keyboard=([
        [
        telegram.KeyboardButton(teachers_buttons[0]),
        telegram.KeyboardButton(teachers_buttons[1]),
        telegram.KeyboardButton(teachers_buttons[2]),
        telegram.KeyboardButton(teachers_buttons[3]),
        ]
    ])
    return telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)