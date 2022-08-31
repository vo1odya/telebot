import telebot
import random

token ="5725173866:AAGuseJn9EpWJZP-BeuDzGQJKCWauHY0PbM"

my_name = 'Вова'

bot = telebot.TeleBot(token)

RANDOM_TASKS = ["Записаться на курс", "Покорить вершину", "Помыть машину", "Написать письмо"]

HELP = """
/help - показать список доступных команд.
/add - добавить команду.
/show - напечатать все добавленные задачи.
/exit - выход из раздела комманд.
/random - добавить случайную задачу на дату Сегодня."""

tasks ={}

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)

@bot.message_handler(commands=["help"])
def help(message):
     bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add(message):
    print(message.text)
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача: " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегодня"
    task = task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    text = "Задача: " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message): #message.text = /print <date>
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[]" + task + "\n" # <- символ перевода строки (добавляется через +)
    else:
        text = "Задач на эту даты нет"
    bot.send_message(message.chat.id, text)


bot.polling(non_stop=True)

