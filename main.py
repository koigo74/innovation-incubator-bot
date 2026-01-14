import os
import telebot
import google.generativeai as genai

# API Keys များကို GitHub Secrets မှ ယူခြင်း
TOKEN = os.environ.get('TELEGRAM_TOKEN')
GEMINI_KEY = os.environ.get('GEMINI_API_KEY')

bot = telebot.TeleBot(TOKEN)
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Innovation Incubator မှ ကြိုဆိုပါတယ်! 🚀\nကျွန်တော့်ကို STEM (နည်းပညာ၊ အင်ဂျင်နီယာ) idea တွေ မေးမြန်းနိုင်ပါတယ်။")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Expert Prompt Logic
    expert_prompt = f"Act as a Senior Innovation Analyst. Analyze this STEM idea: {message.text}. Provide a feasibility report and local cost estimation."
    response = model.generate_content(expert_prompt)
    bot.reply_to(message, response.text)

bot.polling()
