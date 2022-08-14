#импортируем нужные библиотеки
import telebot
import requests
from bs4 import BeautifulSoup as BS

bot = telebot.TeleBot('5566843506:AAHDkUsYz5EwmPQNV4V_r70CC10E25WtV9s')
#ссылка на страницу с погодой
url = 'https://retrofm.ru/index.php?go=goroskop'
#получаем текст со страницы
r = requests.get(url)
#применяем парсер
html = BS(r.content, 'html.parser')

text = html.find_all('div', class_='text_box')
#print(text)

cl_text = []
for i in text:
    cl_text.append(i.text)
clear_text = '\n'.join(cl_text)

#описываем декоратор
@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>! \nВведите слово "гороскоп"'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_scorp(message):
    if message.text == 'гороскоп' or message.text == 'Гороскоп':
        bot.send_message(message.chat.id, clear_text)
    else:
        bot.send_message(message.chat.id, 'Что-то пошло не так... Попробуйте еще раз')

#зацикливаем бота, запускаем на постоянное выполнение
bot.polling(none_stop=True)
