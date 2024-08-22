import requests
import telebot
from bs4 import BeautifulSoup
from colorama import Fore
import colorama
from telebot import types
import re
import time
import os
import random

token = "7505490355:AAHOvedZ8D1BliTkrA7l1mnuHXYFhKJX8Rk"  
admin = ['2134456129','6590159614']  
bot=telebot.TeleBot(token,parse_mode="HTML")

keyboard = types.InlineKeyboardMarkup()
s3 = types.InlineKeyboardButton(text=f'𝗕𝗢𝗗𝗬',url = 'https://t.me/x8xt8')
a3 = types.InlineKeyboardButton(text=f'𝗠𝗘𝗥𝗢',url = 'https://t.me/mero_221')
keyboard.row(a3,s3)
@bot.message_handler(commands=["start"])
def start(message):

	name = message.from_user.first_name
	n = message.chat.first_name
	bot.reply_to(message,f'''<b> 𝐇𝐄𝐋𝐋𝐎  (  {name}  ) 
𝐈 𝐀𝐌 𝐀 𝐁𝐎𝐓 𝐂𝐇𝐄𝐂𝐊𝐈𝐍𝐆 𝐏𝐀𝐘𝐌𝐄𝐍𝐓 𝐆𝐀𝐓𝐄𝐖𝐀𝐘𝐒 𝐌𝐀𝐍𝐔𝐀𝐋 𝐂𝐇𝐄𝐂𝐊 𝐀𝐍𝐃 𝐅𝐈𝐋𝐄𝐒
CMD ➜ /m + url </b>''',
reply_markup=keyboard)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.m') or message.text.lower().startswith('/m')) 

def respond_to_vbv(message):
	if str(message.chat.id) not in admin:
		bot.reply_to(message, "𝐘𝐎𝐔 𝐀𝐑𝐄 𝐍𝐎𝐓 𝐒𝐔𝐁𝐒𝐂𝐑𝐈𝐁𝐄𝐃 𝐓𝐎 𝐓𝐇𝐄 𝐁𝐎𝐓 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 🔥")
		return
	iy = message.text
	match = ''.join(iy)
	mm = match[4:]
	bot.reply_to(message, f'LODIND...⏳')
	a = requests.get(f"http://157.10.53.104:8080/gatev2?url={mm}").json()
	if 'error' in a:
		bot.reply_to(message,"ERROR SITE ")
	else:
		p = a['payment_methods']
		c = a['captcha']
		cl = a['cloudflare']
		au = a['auth_gate']
		vbv = a['vbv']
		
		bot.reply_to(message, f'''<b>
[☆]𝗦𝗜𝗧𝗘 : {cc}
[☆]𝗣𝗔𝗬𝗠𝗘𝗡𝗧 : {p}
[☆]𝗖𝗔𝗣𝗧𝗖𝗛𝗔 : {c}
[☆]𝗖𝗟𝗢𝗨𝗗𝗙𝗟𝗔𝗥𝗘 : {cl}
[☆]𝗔𝗨𝗧𝗛 : {au}
[☆]𝗩𝗕𝗩 : {vbv}
[♡]𝗕𝗬 :『@Mero_221』
[♡]𝗕𝗬 :『@x8xt8』
</b> - - - - - - - - - - - - - - - - - ''')


@bot.message_handler(content_types=["document"])
def main(message):
	if str(message.chat.id) not in admin:
		bot.reply_to(message, "𝐘𝐎𝐔 𝐀𝐑𝐄 𝐍𝐎𝐓 𝐒𝐔𝐁𝐒𝐂𝐑𝐈𝐁𝐄𝐃 𝐓𝐎 𝐓𝐇𝐄 𝐁𝐎𝐓 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑")
		return
#	print("خخخخخخخخخخ")
	ko = (bot.reply_to(message, "LODING ...⌛").message_id)
	time.sleep(7)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
			w.write(ee)
	with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				a = requests.get(f"http://157.10.53.104:8080/gatev2?url={cc}").json()
				if 'error' in a:
					print("ERROR SITE")
				else:
					print("OK")
					p = a['payment_methods']
					c = a['captcha']
					cl = a['cloudflare']
					au = a['auth_gate']
					vbv = a['vbv']
					bot.reply_to(message, f'''<b>
[☆]𝗦𝗜𝗧𝗘 : {cc}
[☆]𝗣𝗔𝗬𝗠𝗘𝗡𝗧 : {p}
[☆]𝗖𝗔𝗣𝗧𝗖𝗛𝗔 : {c}
[☆]𝗖𝗟𝗢𝗨𝗗𝗙𝗟𝗔𝗥𝗘 : {cl}
[☆]𝗔𝗨𝗧𝗛 : {au}
[☆]𝗩𝗕𝗩 : {vbv}
[♡]𝗕𝗬 :『@Mero_221』
[♡]𝗕𝗬 :『@x8xt8』
</b> - - - - - - - - - - - - - - - - - ''')
				
print("BOT IS ON")
#while True:
#	try:
#		bot.polling(none_stop=True)
#	except Exception as e:
#		print("")
bot.infinity_polling()