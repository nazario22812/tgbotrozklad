
from email import message
import telebot
from telebot import types


API_TOKEN = '5618986589:AAG9ejk6Uwgktg2bRsp0LoeWH_pIaxJIiv4'
bot = telebot.TeleBot(API_TOKEN)
# Configure logging

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, text="Привіт, я @Rozklad1bot ,\nДопомагаю дізнаватися розклад занять в ліцеї №4.\n\nЗліва в меню список всіх команд.")


bot.set_my_commands([types.BotCommand("/start", "перезапуск бота"), types.BotCommand("/rozklad", "Розклад уроків"), types.BotCommand("/trozklad","Розклад дзвінків")])

@bot.message_handler()
def msgrozklad(message):
    if message.text == "розклад" or message.text == "Розклад":
        # rozklad = types.InlineKeyboardMarkup()
        # day1 = types.InlineKeyboardButton("Понеділок", callback_data='monday')
        # day2 = types.InlineKeyboardButton("Вівторок", callback_data='tuesday')
        # day3 = types.InlineKeyboardButton("Середа", callback_data="wednesday")
        # day4 = types.InlineKeyboardButton("Четвер", callback_data="thursday")
        # day5 = types.InlineKeyboardButton("П'ятниця", callback_data="friday")

        # rozklad.add(day1, day2, day3, day4, day5)
    
        # bot.send_message(message.chat.id, text='Вибери день тиждня:', reply_markup=rozklad)
        klass = types.InlineKeyboardMarkup()
        elevena = types.InlineKeyboardButton("11-A", callback_data='elA')
        elevenb = types.InlineKeyboardButton("11-Б", callback_data='elB')
        klass.add(elevena,elevenb)
        bot.send_message(message.chat.id, text='Вибери свій клас:', reply_markup=klass)

    elif message.text == "/rozklad":
        klass = types.InlineKeyboardMarkup()
        elevena = types.InlineKeyboardButton("11-A", callback_data='elA')
        elevenb = types.InlineKeyboardButton("11-Б", callback_data='elB')
        klass.add(elevena,elevenb)
        bot.send_message(message.chat.id, text='Вибери свій клас:', reply_markup=klass)
    elif message.text == "/trozklad":
        bot.send_message(message.chat.id, "1. 8:00 - 8:45\n2. 8:55 - 9:40\n3. 9:50 - 10:35\n4. 10:55 - 11:40\n5. 11:50 - 12:35\n6. 12:45 - 13:30\n7. 13:35 - 14:20")      

@bot.message_handler(commands=["trozklad"])
def trozk(message):
    pass

@bot.message_handler(commands=["rozklad"])
def rozk(message):
    if message.text == "/rozklad":
        rozklad = types.InlineKeyboardMarkup()
        day1 = types.InlineKeyboardButton("Понеділок", callback_data='monday')
        day2 = types.InlineKeyboardButton("Вівторок", callback_data='tuesday')
        day3 = types.InlineKeyboardButton("Середа", callback_data="wednesday")
        day4 = types.InlineKeyboardButton("Четвер", callback_data="thursday")
        day5 = types.InlineKeyboardButton("П'ятниця", callback_data="friday")

        rozklad.add(day1, day2, day3, day4, day5)

        bot.send_message(message.chat.id, text='Вибери день тиждня:', reply_markup=rozklad)

@bot.callback_query_handler(func=lambda call: True)
def answers(call):
    if call.data == "elA":
        rozklad = types.InlineKeyboardMarkup()
        day1 = types.InlineKeyboardButton("Понеділок", callback_data='mondayA')
        day2 = types.InlineKeyboardButton("Вівторок", callback_data='tuesdayA')
        day3 = types.InlineKeyboardButton("Середа", callback_data="wednesdayA")
        day4 = types.InlineKeyboardButton("Четвер", callback_data="thursdayA")
        day5 = types.InlineKeyboardButton("П'ятниця", callback_data="fridayA")

        rozklad.add(day1, day2, day3, day4, day5)

        bot.send_message(call.message.chat.id, text='Вибери день тиждня:', reply_markup=rozklad)
    elif call.data == "elB":
        rozklad = types.InlineKeyboardMarkup()
        day1 = types.InlineKeyboardButton("Понеділок", callback_data='mondayB')
        day2 = types.InlineKeyboardButton("Вівторок", callback_data='tuesdayB')
        day3 = types.InlineKeyboardButton("Середа", callback_data="wednesdayB")
        day4 = types.InlineKeyboardButton("Четвер", callback_data="thursdayB")
        day5 = types.InlineKeyboardButton("П'ятниця", callback_data="fridayB")

        rozklad.add(day1, day2, day3, day4, day5)

        bot.send_message(call.message.chat.id, text='Вибери день тиждня:', reply_markup=rozklad)


    elif call.data == "mondayB":
        bot.send_message(call.message.chat.id, "1. Українська мова\n2. Українська мова\n3. Хімія\n4. Хімія\n5. Іноземна мова\n6. Іноземна мова\n7. Мистецтво")
    elif call.data == "tuesdayB":
        bot.send_message(call.message.chat.id, "1. Українська література\n2. Українська література\n3. Історія України\n4. Історія України\n5. Друга іноз.\n6. Друга іноз.\n7. Всесвітня історія")
    elif call.data == "wednesdayB":
        bot.send_message(call.message.chat.id, "1. Географія\n2. Іноземна мова\n3. Фізика\n4. Фізика\n5. Зарубіжна література\n6. Захист України\n7.(A:Захист України B: Інформатика гр2)")
    elif call.data == "thursdayB":
        bot.send_message(call.message.chat.id, "1. Астрономія\n2. Фізика\n3. Алгебра\n4. Алгебра\n5. Іноземна мова\n6. Іноземна мова\n7. Інформатика гр2")
    elif call.data == "fridayB":
        bot.send_message(call.message.chat.id, "1. Біологія\n2. Біологія\n3. Геометрія\n4. Геометрія\n5. Історія України\n6. Інформатика гр1\n7. Інформатика гр1")
    
    
    elif call.data == "mondayA":
        bot.send_message(call.message.chat.id, "1. Хімія\n2. Хімія\n3. Українська мова\n4. Українська мова\n5. Алгебра\n6. Інформатика\n7. Географія")
    elif call.data == "tuesdayA":
        bot.send_message(call.message.chat.id, "1. Хімія\n2. Хімія\n3. Українська література\n4. Українська література\n5. Історія України\n6. Історія України\n7. --")
    elif call.data == "wednesdayA":
        bot.send_message(call.message.chat.id, "1. Фізика\n2. Фізика\n3. Іноземна мова\n4. Іноземна мова\n5. (А:Географія B:Інформатика)\n6. Захист України\n7. (А:Захист України B:Біологія)")
    elif call.data == "thursdayA":
        bot.send_message(call.message.chat.id, "1. Алгебра\n2. Алгебра\n3. Фізика\n4. Фізика\n5. Хімія\n6. ХІмія\n7. --")
    elif call.data == "fridayA":
        bot.send_message(call.message.chat.id, "1. Геометрія\n2. Геометрія\n3. Біологія\n4. Біологія\n5. Зарубіжна література\n6. Всесвітня історія\n7. Техн./Обсл.пр.")



if __name__ == '__main__':
    print("Bot started")
    bot.polling(non_stop=True)