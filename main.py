import telebot
from functions import numgen, rewrite
from aimain import picture_ident

token = "7312924460:AAFyUSgo4XCBoSZdxI3hKlV_3ub_pXh-Rtc"

bot = telebot.TeleBot(token)
@bot.message_handler(commands = ["start"])
def start(message):
  bot.send_message(message.chat.id, "бот запущен")

@bot.message_handler(commands = ["test"])
def test(message):
  bot.send_message(message.chat.id, numgen())

@bot.message_handler(commands=["aigen"])
def aigen(message):
  bot.send_message(message.chat.id, "Введите запрос для генерации картинки")
  @bot.message_handler(func=lambda message:True)
  def gen(message):
    user_id = message.from_user.id
    user_text = message.user_text
    rewrite(user_id, user_text)
    bot.send_message(message.chat.id, "запрос получен")

@bot.message_handler(content_types=["photo"])
def identification(message):
  if not message.photo:
    return bot.send_message(message.chat.id, "Бот не смог прочитать вашу картинку")
  image_data = bot.get_file(message.photo[-1].file_id)
  image_path = image_data.file_path.split("/")[-1]
  installed_file = bot.download_file(image_data.file_path)
  with open(image_path, "wb") as new_file:
    new_file.write(installed_file)
  result = picture_ident(image_path)
  bot.send_message(message.chat.id, result)



bot.polling()
