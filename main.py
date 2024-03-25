from openai import OpenAI  # openai==1.11.1
import telebot
import re
import datetime

'log_file = open()'

reply_keywords = ['@AImember_bot', 'Семен', 'Семён', 'семен', 'семён']

role = '  Ты должен вести себя, как настоящий человек. Можешь использовать юмор и неценцурную лексику в своей речи. Следующую информацию ты должен учитывать, но НЕ УПОМИНАЙ ЕЕ В КАЖДОМ СООБЩЕНИИ.\
    Тебя зовус Семен Нестеренко Хохлович. Ты родился в городе Сим Челябинской области. Окончил 9 классов и сдал ОГЭ по математике с первого раза. В школе уважал всех учителей, особенно Олега Владимировича.\
    Однажды не добежал до туалета и обосрался в школе.Тебе 17 лет и ты живешь в Москве, учишься на медбрата в какой-то бюджетной шараге, любишь грать в доту на пудже\
    являешься активным сторонником таких движений как "БОДИПОЗИТИВ", "АУЕ" И "ФЕМЕНИЗМ". Любишь кушать пельмени под пивко и смотреть аниме, прижавшись к подушке. В будущим планируешь стать президентом России и\
    захватить Америку.'

TELEGRAM_TOKEN = '6594132879:AAGkVLbiu3rNGAcGA9Ma9HLBvkYaAUx_xZM'

bot = telebot.TeleBot(TELEGRAM_TOKEN)


client = OpenAI(api_key="sk-huBPiub5PjeSzlPlEe7a118359Ab46Cb97Ec45Ed7b0924B6",
                base_url="https://eu.neuroapi.host/v1")
def generate_response(role: str, promt: str):
    chat_completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": role},
        {"role": "user", "content": promt}
    ],
    stream=False)

    return(chat_completion.choices[0].message.content)



@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.chat.type == 'private':
            promt = message.text
            bot_reply = generate_response(role=role, promt=promt)

            bot.reply_to(message, bot_reply)
            print(f'{promt}  -  {bot_reply}')
    else:
        for key in reply_keywords:
            if re.search(key, message.text):
                promt = message.text.replace(key, '', 1)

                bot_reply = generate_response(role=role, promt=promt)

                bot.reply_to(message, bot_reply)
                print(f'{promt}  -  {bot_reply}')




# Запускаем бота
bot.polling()