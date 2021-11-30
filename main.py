from logging import info
import re
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import  CallbackContext, Updater, CommandHandler, PicklePersistence, MessageHandler, Filters, CallbackQueryHandler
from menu import main_menu_keyboard, timetable_menu_keyboard, teachers_menu_keyboard
from credentials import TOKEN
from key_buttons import tele_buttons, timetable_buttons, teachers_buttons
from text import monday1, tuesday1, wendsday1, thursday1, friday1, saturday1, math1, mechanic1, paht1, organic1, economy1, complain1, question1

def start(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEDTJhhk5s7eZ3S9-cs1Zz0x6_iIcrS7wACjQgAAnlc4gk0y_uYceajxCIE'
        )
   
    update.message.reply_text(
        """Добро пожаловать, {username},меня зовут Элли. Я облегчаю студентческую жизнь , ниже вы можете ознакомиться моими функциями: """.format(
            username=update.effective_user.first_name \
                if update.effective_user.first_name is not None \
                else update.effective_user.username),
        reply_markup=main_menu_keyboard()
    )

    
def back(update: Update, context: CallbackContext):
    update.message.reply_text(
        " {username},вы вернулись в главное меню: "
    
    )


TIMETABLE_REGEX = r"(?=("+(tele_buttons[0])+r"))"
EXAMS_REGEX = r"(?=("+(tele_buttons[1])+r"))"
TEACHERS_REGEX = r"(?=("+(tele_buttons[2])+r"))"
CONTACT_REGEX = r"(?=("+(tele_buttons[3])+r"))"

# def zhaloba(update: Update, context: CallbackContext):
#     z = update.message.text
#     print(z[:6])
#     if z[:6] =='Вопрос:':
#         context.bot.send_message(
#             chat_id = '@eduKg123',
#             text = z
#         )

def timetable_inline_menu(update: Update, context: CallbackContext):
    info = re.match(TIMETABLE_REGEX, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Понедельник", callback_data='monday')],
        [InlineKeyboardButton("Вторник", callback_data='tuesday')],
        [InlineKeyboardButton("Среда", callback_data='wendsday')],
        [InlineKeyboardButton("Четверг", callback_data='thursday')],
        [InlineKeyboardButton("Пятница", callback_data='friday')],
        [InlineKeyboardButton("Суббота", callback_data='saturday')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите день:',
        reply_markup=reply_markup
    )


def exams_inline_menu(update: Update, context: CallbackContext):
    info = re.match(EXAMS_REGEX, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Математика", callback_data='math')],
        [InlineKeyboardButton("ФХМА", callback_data='mechanic')],
        [InlineKeyboardButton("ПАХТ", callback_data='paht')],
        [InlineKeyboardButton("Органика", callback_data='organic')],
        [InlineKeyboardButton("Экономика", callback_data='economy')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите предмет:',
        reply_markup=reply_markup
    )

def teachers_inline_menu(update: Update, context: CallbackContext):
    info = re.match(TEACHERS_REGEX, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Белекова Г.Ш", callback_data='t1_info')],
        [InlineKeyboardButton("Исаева Д.Т", callback_data='t2_info')],
        [InlineKeyboardButton("Ли С.П", callback_data='t3_info')],
        [InlineKeyboardButton("Копошева Э.И", callback_data='t4_info')],
        [InlineKeyboardButton("Гудимова А.Н", callback_data='t5_info')],
        [InlineKeyboardButton("Айсулуу Эсенкулова", callback_data='t5_info')]
        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите преподавателя:',
        reply_markup=reply_markup
    )


def contact_inline_menu(update: Update, context: CallbackContext):
    info = re.match(CONTACT_REGEX, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Задайте свой вопрос", callback_data='question')],
        [InlineKeyboardButton("Оставьте свою жалобу", callback_data='complain')]
        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите опцию:',
        reply_markup=reply_markup
    )

def group_chat(update: Update, context: CallbackContext):
    info = update.message.text
    if info[:6] == 'Вопрос':
        context.bot.send_message(
            # chat_id='-1001068367339',
            chat_id='@eduKg123',
            text=info
        )
    if info[:6] == 'Жалоба':
        context.bot.send_message(
            # chat_id='-1001068367339',
            chat_id='@complainforedu',
            text=info
        )
    
# def chat1(update: Update, context: CallbackContext):
#     info = update.message.text
#     # print(info[:6])
#     print('asd')
#     print(info[:6] == 'Жалоба')
#     if info[:6] == 'Жалоба':
#         print('hello')
#         context.bot.send_message(
#             # chat_id='-1001068367339',
#             chat_id='@eduKg123',
#             text=info
#         )

def inline_buttons(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    if query.data == 'monday':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=monday1)
    
    if query.data == 'tuesday':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=tuesday1)
    
    if query.data == 'wendsday':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=wendsday1)
   
    if query.data == 'thursday':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=thursday1)
    
    
    
    if query.data == 'friday':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=friday1)
      
    

    if query.data == 'saturday':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=saturday1)
   
          
    

    if query.data == 'math':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=math1)
    
    if query.data == 'mechanic':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=mechanic1)     

    if query.data == 'paht':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=paht1)      
    
    if query.data == 'organic':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=organic1) 

    if query.data == 'economy':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=economy1)  
 
    if query.data == 'question':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=question1)
    


    if query.data == 'complain':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=complain1)

    
        
    
    
updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data') )

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('back', start))
updater.dispatcher.add_handler(CallbackQueryHandler(inline_buttons))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(TIMETABLE_REGEX),
    timetable_inline_menu
    
))


updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(EXAMS_REGEX),
    exams_inline_menu
    
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(TEACHERS_REGEX),
    teachers_inline_menu
    
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CONTACT_REGEX),
    contact_inline_menu
    
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    group_chat
    
))

# updater.dispatcher.add_handler(MessageHandler(
#     Filters.text,
#     chat1
    
# ))





updater.start_polling()
updater.idle()

