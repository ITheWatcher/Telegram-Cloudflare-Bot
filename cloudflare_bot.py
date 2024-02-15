import telebot
import requests
from telebot import types

bot = telebot.TeleBot('YourBotToken')

class CloudflareCheck:
    def __init__(self, url='https://example.com', timeout=5):
        self.url = url
        self.timeout = timeout

    def check_website(self):
        try:
            response = requests.get(self.url, timeout=self.timeout)
            
            cloudflare_headers = [
                'Server',
                'CF-RAY',
                'CF-Cache-Status',
                'CF-Request-ID'
            ]

            for header in cloudflare_headers:
                if header in response.headers:
                    if 'cloudflare' in response.headers[header].lower():
                        return True
                
            return False

        except Exception as e:
            print("Error occurred:", e)
            return False

@bot.message_handler(commands=['cloudflare'])
def send(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    cloudflare = types.InlineKeyboardButton('Yes', callback_data='cloudflare')
    exit = types.InlineKeyboardButton('No Exit..', callback_data='exit')
    markup.add(cloudflare, exit)
    bot.send_message(message.chat.id, 'Do You Want To Run Cloudflare Detector Bot?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def recive(callback):
    if callback.message:
        if callback.data == 'cloudflare':
            bot.send_message(callback.message.chat.id, 'Enter The Website URL (e.g., https://example.com): ')
            bot.register_next_step_handler(callback.message, check_website_callback)
        else:
            bot.send_message(callback.message.chat.id, 'Fuck You Don\'t Miss With Me')

def check_website_callback(message):
    url = message.text.strip()
    checker = CloudflareCheck(url=url)
    cloudflare_detected = checker.check_website()
    if cloudflare_detected:
        bot.send_message(message.chat.id, f"✅ Cloudflare Is Used In This Website. [{message.text.strip('htps:/w.com').upper()}]", parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, f"⛔ Cloudflare Is Not Used In This Website. [{message.text.strip('htps:/w.com').upper()}]", parse_mode='Markdown')

bot.polling()

#TheWatcher