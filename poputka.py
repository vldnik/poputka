import requests
from time import sleep
import telebot
from telebot import types
from hashie import *
from way import *
from other_towns import *


token = '839300514:AAG83SoOTMk7crKoYKmWwL6_OGRVaqsAot8'

bot = telebot.TeleBot(token)

table = HashTable(10000)
name = ''
age = 0
link = ''
carNum = ''
telNum = ''
currentCity = ''
destinationCity = ''
pricePerKilometer = 0


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/drive':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
    elif message.text == '/go':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name_go)
    else:
        bot.send_message(message.from_user.id, 'Напиши /drive, если хочешь зарегестрироваться как водитель или /go, чтобы поехать пассажиром')


def get_name(message):
    global name
    name = message.text
    User.name = name
    bot.send_message(message.from_user.id, 'Введи свой ник в телеграме через @:')
    bot.register_next_step_handler(message, get_link)


def get_link(message):
    global link
    link = message.text
    User.link = link
    bot.send_message(message.from_user.id, 'Введи номер машины:')
    bot.register_next_step_handler(message, get_carNum)


def get_carNum(message):
    global carNum
    carNum = message.text
    User.carNum = carNum
    bot.register_next_step_handler(message, get_telnum)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(message.from_user.id, 'Введи номер телефона:', reply_markup=keyboard)


def get_telnum(message):
    global telNum
    telNum = message.text
    User.telNum = telNum

    bot.send_message(message.from_user.id, """Введи номер города, в котором ты находишься:
1. Киев
2. Харьков
3. Львов
4. Днепр
5. Запорожье
6. Одесса
7. Донецк
8. Кривой Рог
9. Николаев
10. Мариуполь
11. Винница
12. Полтава
13. Чернигов
14. Сумы
15. Ровно
16. Ивано-Франковск""")
    bot.register_next_step_handler(message, get_currentCity)


def get_currentCity(message):
    global currentCity

    if (message.text == '1'):
        currentCity = 'Kyiv'
    elif (message.text == '2'):
        currentCity = 'Kharkiv'
    elif (message.text == '3'):
        currentCity = 'Lviv'
    elif (message.text == '4'):
        currentCity = 'Dnipro'
    elif (message.text == '5'):
        currentCity = 'Zaporizhia'
    elif (message.text == '6'):
        currentCity = 'Odessa'
    elif (message.text == '7'):
        currentCity = 'Donetsk'
    elif (message.text == '8'):
        currentCity = 'KryvyiRih'
    elif (message.text == '9'):
        currentCity = 'Mykolaiv'
    elif (message.text == '10'):
        currentCity = 'Mariupol'
    elif (message.text == '11'):
        currentCity = 'Vinnytsia'
    elif (message.text == '12'):
        currentCity = 'Poltava'
    elif (message.text == '13'):
        currentCity = 'Chernihiv'
    elif (message.text == '14'):
        currentCity = 'Sumy'
    elif (message.text == '15'):
        currentCity = 'Rivne'
    elif (message.text == '16'):
        currentCity = 'IvanoFrankivsk'
    else:
        bot.send_message(message.from_user.id, 'Правда хочешь в Нововолынск?')
        currentCity = 'Kyiv'
    User.currentCity = currentCity
    bot.send_message(message.from_user.id, """Введи номер города, в который ты едешь:
1. Киев
2. Харьков
3. Львов
4. Днепр
5. Запорожье
6. Одесса
7. Донецк
8. Кривой Рог
9. Николаев
10. Мариуполь
11. Винница
12. Полтава
13. Чернигов
14. Сумы
15. Ровно
16. Ивано-Франковск""")
    bot.register_next_step_handler(message, get_destinationCity)


def get_destinationCity(message):
    global destinationCity

    if (message.text == '1'):
        destinationCity = 'Kyiv'
    elif (message.text == '2'):
        destinationCity = 'Kharkiv'
    elif (message.text == '3'):
        destinationCity = 'Lviv'
    elif (message.text == '4'):
        destinationCity = 'Dnipro'
    elif (message.text == '5'):
        destinationCity = 'Zaporizhia'
    elif (message.text == '6'):
        destinationCity = 'Odessa'
    elif (message.text == '7'):
        destinationCity = 'Donetsk'
    elif (message.text == '8'):
        destinationCity = 'KryvyiRih'
    elif (message.text == '9'):
        destinationCity = 'Mykolaiv'
    elif (message.text == '10'):
        destinationCity = 'Mariupol'
    elif (message.text == '11'):
        destinationCity = 'Vinnytsia'
    elif (message.text == '12'):
        destinationCity = 'Poltava'
    elif (message.text == '13'):
        destinationCity = 'Chernihiv'
    elif (message.text == '14'):
        destinationCity = 'Sumy'
    elif (message.text == '15'):
        destinationCity = 'Rivne'
    elif (message.text == '16'):
        destinationCity = 'IvanoFrankivsk'
    else:
        bot.send_message(message.from_user.id, 'Правда хочешь в Нововолынск?')
        destinationCity = 'Kyiv'
    User.destinationCity = destinationCity

    bot.send_message(message.from_user.id, "Вот такой маршрут будет удобный: " + ", → ".join(graph.dijkstra(currentCity, destinationCity))+  ". Введите цену за киллометр пути")
    bot.register_next_step_handler(message, get_price)


def get_price(message):
    pricePerKilometer = message.text
    user1 = User(name, link, carNum, telNum, currentCity, destinationCity, pricePerKilometer)
    table.addUser(user1)
    bot.send_message(message.from_user.id, "Спасибо, ваша заявка принята!")


def check_if_way_ok(message):
    listOfDrivers = ""
    arr = table.findDrivers(currentCity_go, destinationCity_go)
    for i in range(len(arr)):
        listOfDrivers += str("Name: " + arr[i].name + "\nTelegram link: " + arr[i].link + "\nTelephone number: " + arr[
            i].telNum + "\nCar number: " + arr[i].carNum + "\nPrice per kilometer: " + str(
            arr[i].pricePerKilometer) + "\n" + "\n")

    if (message.text == '/yes'):
        bot.send_message(message.from_user.id, """Отлично, вот кто туда едет:
""" + listOfDrivers)
    elif (message.text == '/no'):
        myStartCity = currentCity_go
        variants_of_tows = ", ".join(GetBestAvailableCities(myStartCity, myAvailableCities, myBestCitiesAmount))
        bot.send_message(message.from_user.id, """Тогда попробуйте поехать из этих городов: """ + variants_of_tows)


def get_name_go(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Введи свой ник в телеграме через @:')
    bot.register_next_step_handler(message, get_link_go)


def get_link_go(message):
    global link
    link = message.text
    bot.send_message(message.from_user.id, """Введи номер города, в котором ты находишься:
1. Киев
2. Харьков
3. Львов
4. Днепр
5. Запорожье
6. Одесса
7. Донецк
8. Кривой Рог
9. Николаев
10. Мариуполь
11. Винница
12. Полтава
13. Чернигов
14. Сумы
15. Ровно
16. Ивано-Франковск""")
    bot.register_next_step_handler(message, get_currentCity_go)


def get_currentCity_go(message):
    global currentCity_go

    if (message.text == '1'):
        currentCity_go = 'Kyiv'
    elif (message.text == '2'):
        currentCity_go = 'Kharkiv'
    elif (message.text == '3'):
        currentCity_go = 'Lviv'
    elif (message.text == '4'):
        currentCity_go = 'Dnipro'
    elif (message.text == '5'):
        currentCity_go = 'Zaporizhia'
    elif (message.text == '6'):
        currentCity_go = 'Odessa'
    elif (message.text == '7'):
        currentCity_go = 'Donetsk'
    elif (message.text == '8'):
        currentCity_go = 'KryvyiRih'
    elif (message.text == '9'):
        currentCity_go = 'Mykolaiv'
    elif (message.text == '10'):
        currentCity_go = 'Mariupol'
    elif (message.text == '11'):
        currentCity_go = 'Vinnytsia'
    elif (message.text == '12'):
        currentCity_go = 'Poltava'
    elif (message.text == '13'):
        currentCity_go = 'Chernihiv'
    elif (message.text == '14'):
        currentCity_go = 'Sumy'
    elif (message.text == '15'):
        currentCity_go = 'Rivne'
    elif (message.text == '16'):
        currentCity_go = 'IvanoFrankivsk'
    else:
        bot.send_message(message.from_user.id, 'Правда хочешь в Нововолынск?')
        currentCity_go = 'Kyiv'

    bot.send_message(message.from_user.id, """Введи номер города, в который ты едешь:
1. Киев
2. Харьков
3. Львов
4. Днепр
5. Запорожье
6. Одесса
7. Донецк
8. Кривой Рог
9. Николаев
10. Мариуполь
11. Винница
12. Полтава
13. Чернигов
14. Сумы
15. Ровно
16. Ивано-Франковск""")
    bot.register_next_step_handler(message, get_destinationCity_go)


def get_destinationCity_go(message):
    global destinationCity_go

    if (message.text == '1'):
        destinationCity_go = 'Kyiv'
    elif (message.text == '2'):
        destinationCity_go = 'Kharkiv'
    elif (message.text == '3'):
        destinationCity_go = 'Lviv'
    elif (message.text == '4'):
        destinationCity_go = 'Dnipro'
    elif (message.text == '5'):
        destinationCity_go = 'Zaporizhia'
    elif (message.text == '6'):
        destinationCity_go = 'Odessa'
    elif (message.text == '7'):
        destinationCity_go = 'Donetsk'
    elif (message.text == '8'):
        destinationCity_go = 'KryvyiRih'
    elif (message.text == '9'):
        destinationCity_go = 'Mykolaiv'
    elif (message.text == '10'):
        destinationCity_go = 'Mariupol'
    elif (message.text == '11'):
        destinationCity_go = 'Vinnytsia'
    elif (message.text == '12'):
        destinationCity_go = 'Poltava'
    elif (message.text == '13'):
        destinationCity_go = 'Chernihiv'
    elif (message.text == '14'):
        destinationCity_go = 'Sumy'
    elif (message.text == '15'):
        destinationCity_go = 'Rivne'
    elif (message.text == '16'):
        destinationCity_go = 'IvanoFrankivsk'
    else:
        bot.send_message(message.from_user.id, 'Правда хочешь в Нововолынск?')
        destinationCity_go = 'Kyiv'
    wayofpass = "Едешь из " + currentCity_go + " в " + destinationCity_go + '?' + """
Если да - нажми /yes , если нет - /no"""
    bot.send_message(message.from_user.id, wayofpass)
    bot.register_next_step_handler(message, check_if_way_ok)


@bot.message_handler(commands=["register"])
def register(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id,
                     "Гони телефон и местоположение, быра!",
                     reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)


