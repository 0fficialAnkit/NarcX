# # without using GUI
# from telegram import Update
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
# from datetime import datetime, timedelta 
# import requests  

# TOKEN = "7279484881:AAHQN-E1AAhZZyVVfPhG4U40-rWrvc6Aewk"
# POLICE_GROUP_CHAT_ID = "your telegram id"  

# narcotics_words = ["💊", "drugs", "cocaine", "heroin", "meth", "ecstasy", "weed", "marijuana","maal", "buy", "sell", "drug", "lsd"]

# user_phone_numbers = {}

# def detect_narcotics(message: str) -> bool:
#     message_words = message.lower().split()
#     for word in narcotics_words:
#         if word.lower() in message_words: 
#             return True
#     return False

# def convert_to_ist(utc_dt):
#     ist_dt = utc_dt + timedelta(hours=5, minutes=30)
#     return ist_dt.strftime('%Y-%m-%d %H:%M:%S IST')

# def get_current_location() -> str:
#     try:
#         response = requests.get('http://ip-api.com/json/').json()
#         location = f"{response['city']}, {response['country']} (Lat: {response['lat']}, Lon: {response['lon']})"
#     except:
#         location = "Location not available"
#     return location

# def get_server_ip() -> str:
#     try:
#         response = requests.get('https://api.ipify.org?format=json').json()
#         return response['ip']
#     except:
#         return "IP not available"

# async def handle_message(update: Update, context: CallbackContext) -> None:
#     message_text = update.message.text
#     user_full_name = update.effective_user.full_name
#     user_username = update.effective_user.username or "No username"
#     group_name = update.effective_chat.title
#     user_id = update.effective_user.id  # Unique user ID
#     message_time = convert_to_ist(update.message.date)

#     if detect_narcotics(message_text):
#         location = get_current_location()
#         user_phone_number = user_phone_numbers.get(user_id, "No phone number provided")
#         server_ip = get_server_ip()

#         alert_message = (
#             f"🚨 Alert: Narcotics-related activity detected!\n\n"
#             f"User: {user_full_name} (@{user_username})\n"
#             f"User ID: {user_id}\n"
#             f"Phone Number: {user_phone_number}\n"
#             f"Group: {group_name}\n"
#             f"Time: {message_time}\n"
#             f"Message: '{message_text}'\n"
#             f"Location: {location}\n"
#             f"Server IP: {server_ip}"
#         )
#         await context.bot.send_message(chat_id=POLICE_GROUP_CHAT_ID, text=alert_message)

# async def start(update: Update, context: CallbackContext) -> None:
#     await update.message.reply_text('Bot has started monitoring for narcotics-related words!')

# def main() -> None:
#     application = Application.builder().token(TOKEN).build()

#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

#     application.run_polling(timeout=30)

# if __name__ == "__main__":
#     main()


# with GUI



# import tkinter as tk
# import threading
# import asyncio
# from telegram import Update
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
# from datetime import timedelta
# import requests
# TOKEN = "7279484881:AAHQN-E1AAhZZyVVfPhG4U40-rWrvc6Aewk"
# POLICE_GROUP_CHAT_ID = "1187069468"

# narcotics_words = ["💊","drugs", "cocaine", "heroin", "meth", "ecstasy", "weed", "marijuana", "maal", "buy", "narco", "drug", "lsd", "pills", "methamine", "delivery", "mdma", "speed", "ketamin", "pudiya", "high", "Crystal" , "Opium", "steroids", "powder", "pooriya", "boomers", "Lady Bubbles", "stuff", "stuffs", "crack" , "pot", "pott"]
# user_phone_numbers = {}
# def detect_narcotics(message: str) -> bool:
#     message_words = message.lower().split()
#     for word in narcotics_words:
#         if word in message_words:
#             return True
#     return False
# def convert_to_ist(utc_dt):
#     ist_dt = utc_dt + timedelta(hours=5, minutes=30)
#     return ist_dt.strftime('%Y-%m-%d %H:%M:%S IST')
# def get_current_location() -> str:
#     try:
#         response = requests.get('http://ip-api.com/json/').json()
#         location = f"{response['city']}, {response['country']} (Lat: {response['lat']}, Lon: {response['lon']})"
#     except:
#         location = "Location not available"
#     return location
# def get_server_ip() -> str:
#     try:
#         response = requests.get('https://api.ipify.org?format=json').json()
#         return response['ip']
#     except:
#         return "IP not available"
# async def handle_message(update: Update, context: CallbackContext) -> None:
#     message_text = update.message.text
#     user_full_name = update.effective_user.full_name
#     user_username = update.effective_user.username or "private username"
#     group_name = update.effective_chat.title
#     user_id = update.effective_user.id
#     message_time = convert_to_ist(update.message.date)
#     if detect_narcotics(message_text):
#         location = get_current_location()
#         user_phone_number = user_phone_numbers.get(user_id, "No phone number provided")
#         server_ip = get_server_ip()
#         alert_message = (
#             f"🚨 Alert: Narcotics-related activity detected!\n\n"
#             f"User: {user_full_name} (@{user_username})\n"
#             f"User ID: {user_id}\n"      
#             f"Phone Number: {user_phone_number}\n"
#             f"Group: {group_name}\n"
#             f"Time: {message_time}\n"         
#             f"Message: '{message_text}'\n"
#             f"Location: {location}\n"     
#             f"Server IP: {server_ip}"    
#         )
#         await context.bot.send_message(chat_id=POLICE_GROUP_CHAT_ID, text=alert_message)
# async def start(update: Update, context: CallbackContext) -> None:
#     await update.message.reply_text('Bot has started monitoring for narcotics-related words!')
# def run_bot():
#     application = Application.builder().token(TOKEN).build()
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
#     application.run_polling(timeout=30)
#     #////////////////////////////////////////////////////////////////////////////////////////
# def stop_bot():
#     global bot_running
#     bot_running = False
#     print("Bot is stopping...")
#     # Here you should implement logic to stop the bot properly
#     # Currently, it just closes the GUI
#     root.quit()
#     #///////////////////////////////////////////////////////////////////////////////////////
# def start_bot():
#     bot_thread = threading.Thread(target=asyncio.run, args=(run_bot(),))
#     bot_thread.start()
# root = tk.Tk()
# root.title("Narcotics Detection Bot")
# root.geometry("400x300")
# root.configure(bg="#1e1e2d")
# title_label = tk.Label(root, text="Narcotics Detection Bot", font=("Helvetica", 20, "bold"), fg="white", bg="#1e1e2d")
# title_label.pack(pady=20)
# def create_round_button(master, text, command):
#     button = tk.Button(master, text=text, command=command, font=("Helvetica", 14), fg="white", bg="#3a3a4f", bd=0,
#                        activebackground="#5a5a7f", highlightthickness=0, relief="flat")
#     button.pack(pady=10)
#     button.configure(height=2, width=20)
#     def on_enter(e):
#         button['background'] = '#5a5a7f'
#     def on_leave(e):
#         button['background'] = '#3a3a4f'
#     button.bind("<Enter>", on_enter)
#     button.bind("<Leave>", on_leave)
#     return button
# start_button = create_round_button(root, "Start NarcX", start_bot)
# stop_button = create_round_button(root, "Stop NarcX", root.quit)
# root.mainloop()








#///////////////////




# TOKEN = "7279484881:AAHQN-E1AAhZZyVVfPhG4U40-rWrvc6Aewk"
# POLICE_GROUP_CHAT_ID = "1187069468" #ankit
# POLICE_GROUP_CHAT_ID = "5205657737" #kavya
# POLICE_GROUP_CHAT_ID = "7512827887" #sumit
# POLICE_GROUP_CHAT_ID = "1212425128" #ruchika
# POLICE_GROUP_CHAT_ID = "6061184898" #anshu
# POLICE_GROUP_CHAT_ID = "6718957128" #vishnu


     
import tkinter as tk
import threading
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from datetime import timedelta
import requests

TOKEN = "7279484881:AAHQN-E1AAhZZyVVfPhG4U40-rWrvc6Aewk"
POLICE_GROUP_CHAT_ID = "1187069468" #ankit
# POLICE_GROUP_CHAT_ID = "5205657737" #kavya
# POLICE_GROUP_CHAT_ID = "7512827887" #sumit
# POLICE_GROUP_CHAT_ID = "1212425128" #ruchika
# POLICE_GROUP_CHAT_ID = "6061184898" #anshu
# POLICE_GROUP_CHAT_ID = "6718957128" #vishnu

narcotics_words = {
    "english": [
        "💊", "drugs", "cocaine", "heroin", "meth", "ecstasy", "weed",
        "marijuana", "maal", "buy", "narco", "drug", "lsd", "pills",
        "methamine", "delivery", "mdma", "speed", "ketamin", "pudiya",
        "high", "Crystal", "Opium", "steroids", "powder", "pooriya",
        "boomers", "Lady Bubbles", "stuff", "stuffs", "crack", "pot", "pott" , "deal", 
        "dealer", "trafficking", "shipment", "distribution", "smuggle", "blackmarket", 
        "Addict" , "burnout" , "dopehead" , "doper" , "druggie" , "fiend" , "hophead" , 
        "junkie" , "stoner" , "user" , "zombie" , "drogas", "cocaína", "heroína", "metanfetamina", 
        "ecstasy", "maconha", "marijuna", "marijuana", "haxixe", "haxixes", 
        "yaba", "yava", "marijuana", "maal", "comprar", "narco", "droga", "lsd", "comprimidos", "metanfetamina", "morfina", 
        "metamina", "entrega", "mdma", "cetamina", "pudiya", "reggi", "dro", "top shelf", "sour d", "verdes", 
        "cigarro de maconha", "papel", "alta", "cristal", "opio", "esteroides", "pó", "pooriya", "buttfunk", 
        "boomers", "lady bubbles", "coisas", "coisas", "crack", "erva", "erva", "negocio", 
        "dealer", "trafico", "envio", "distribuição", "contrabando", "mercado negro", 
        "viciado", "esgotado", "cabeca de dope", "usador de dope", "drogado", "dependente", "viciado", 
        "junkie", "maconheiro", "usuario", "zumbi", "po branco", "erva", "chitta", "chita", "charas", "doda", "phukki",
        "satta", "babu", "kali", "tadi", "desi", "ghas", "bhang", "cannabis", "gard", "molly", "droga de festa", 
        "droga do amor", "acido", "blotter", "haxixe", "casca", "estoque", "dinheiro", "cristal", "scooby snacks", "dope", 
        "erva", "doce", "arvore de erva", "suco", "ruim", "neve", "💊", "drugs","drug", "cocaine", "heroin", "meth", "ecstasy", 
        "weed", "maruana", "mayuana", "hash", "hashes", "yaba", "yava", 
        "marijuana", "maal", "buy", "narco", "drug", "lsd", "pills", "methamphetamine", "morphine", "afim", "afeem", "affem", "affeem", 
        "ufim","ufeem", "methamine", "delivery", "mdma", "speed", "ketamin", "pudiya", "reggi", "dro", "top shelf", "sour D", "greens", "joint", "paper", 
        "high", "Crystal", "Opium", "steroids", "powder", "pooriya", "buttfunk", "fluff", "crank", "coke", "blotter", "ludes", 
        "boomers", "Lady Bubbles", "stuff", "stuffs", "crack", "pot", "pott" , "deal", "hemp", "opium poppy", "coca leaf", "coca",
        "dealer", "trafficking", "shipment", "distribution", "smuggle", "blackmarket", "calmpose", "bong", 
        "Addict" , "burnout" , "dopehead" , "dope" , "druggie" , "fiend" , "hophead" , 
        "junkie" , "stoner" , "user" , "zombie", "white powder", "grass", "chitta", "chita", "charas", "doda", "phukki",
        "satta", "babu", "kali", "tadi", "desi", "ghas", "bhang", "cannabis", "gard", "molly", "party drug", "love drug", "acid", "blotter", 
        "hahish", "husk", "stash", "cash", "crystal", " Scooby Snacks", "dope", "herb", "candy", "grass tree", "wack"
    ],
    "hindi": [        "नशा", "ड्रग्स", "कोकीन", "हेरोइन", "मेथ", "एक्स्टसी", "गांजा",
        "भांग", "खरीद", "नार्को", "नशे", "गोलियाँ", "मेड्स", "ड्रग", 
        "सप्लाई", "उच्च", "स्टीरॉयड", "पाउडर", "उच्चता", "हशिश" , "सौदा", "डीलर", 
        "ट्रैफिकिंग", "शिपमेंट", "वितरण", "स्मगलिंग", "ब्लैकमार्केट", "ड्रग्स", "कोकीन", "हेरोइन", 
        "मेथ", "एक्स्टसी", "गांजा", "मारुआना", "मायुना",
        "चरस", "चरस", "याबा", "यावा", "मारिजुआना", "माल", "खरीद", "नारको", "नशा", 
        "एलएसडी", "गोलियां", "मेथामफेटामाइन", "मॉर्फिन", "मेथामिन", "डिलीवरी", "एमडीएमए", 
        "स्पीड", "केटामिन", "पुड़िया", "रेग्गी", "ड्रॉ", "टॉप शेल्फ", "सॉर डी", "हरी पत्तियां", 
        "जॉइंट", "पेपर", "नशे में", "क्रिस्टल", "अफीम", "स्टेरॉयड", "पाउडर", "पुड़िया", "बटफंक", 
        "बूमर्स", "लेडी बबल्स", "सामान", "सामान", "क्रैक", "पॉट", "पॉट", "सौदा", 
        "डीलर", "तस्करी", "शिपमेंट", "वितरण", "तस्करी करना", "काला बाजार", 
        "नशेड़ी", "बर्नआउट", "डोपहेड", "डोपर", "ड्रगी", "शैतान", "हॉपहेड", 
        "जंकी", "स्टोनर", "उपभोक्ता", "ज़ोंबी", "सफेद पाउडर", "घास", "चिट्टा", "चिता", "चरस", 
        "डोडा", "फुक्की", "सट्टा", "बाबू", "काली", "ताड़ी", "देसी", "घास", "भांग", 
        "गांजा", "गार्ड", "माली", "पार्टी ड्रग", "लव ड्रग", "एसिड", "ब्लॉटर", 
        "हशीश", "भूसी", "माल", "नकद", "क्रिस्टल", "स्कूबी स्नैक्स", "डोप", "जड़ी-बूटी", 
        "कैंडी", "घास का पेड़", "जूस", "वैक", "बर्फ"
    ]
}

user_phone_numbers = {}
user_languages = {} 

def detect_narcotics(message: str) -> bool:
    message_words = message.lower().split()
    for language, words in narcotics_words.items():
        for word in words:
            if word in message_words:
                return True
    return False

def convert_to_ist(utc_dt):
    ist_dt = utc_dt + timedelta(hours=5, minutes=30)
    return ist_dt.strftime('%Y-%m-%d %H:%M:%S IST')

def get_current_location() -> str:
    try:
        response = requests.get('http://ip-api.com/json/').json()
        location = f"{response['city']}, {response['country']} (Lat: {response['lat']}, Lon: {response['lon']})"
    except:
        location = "Location not available"
    return location

def get_server_ip() -> str:
    try:
        response = requests.get('https://api.ipify.org?format=json').json()
        return response['ip']
    except:
        return "IP not available"

async def handle_message(update: Update, context: CallbackContext) -> None:
    message_text = update.message.text
    user_full_name = update.effective_user.full_name
    user_username = update.effective_user.username or "private username"
    group_name = update.effective_chat.title
    user_id = update.effective_user.id
    message_time = convert_to_ist(update.message.date)
    user_phone_number = user_phone_numbers.get(user_id, "No phone number provided")
    location = get_current_location()
    server_ip = get_server_ip()

    if detect_narcotics(message_text):

        alert_message = (
            f"🚨 Alert: Narcotics-related activity detected!\n\n"
            f"User: {user_full_name} (@{user_username})\n"
            f"User ID: {user_id}\n"
            f"Phone Number: {user_phone_number}\n"
            f"Group: {group_name}\n"
            f"Time: {message_time}\n"
            f"Message: '{message_text}'\n"
            f"Location: {location}\n"
            f"Server IP: {server_ip}\n"
            f"🚨 अलर्ट: नशे से संबंधित गतिविधि का पता चला!\n\n"
            f"उपयोगकर्ता: {user_full_name} (@{user_username})\n"
            f"उपयोगकर्ता आईडी: {user_id}\n"
            f"फोन नंबर: {user_phone_number}\n"
            f"समूह: {group_name}\n"
            f"समय: {message_time}\n"
            f"संदेश: '{message_text}'\n"
            f"स्थान: {location}\n"
            f"सर्वर आईपी: {server_ip}"
        )

        await context.bot.send_message(chat_id=POLICE_GROUP_CHAT_ID, text=alert_message)

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Bot has started monitoring for narcotics-related words!')

async def set_language(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if context.args and context.args[0] in narcotics_words.keys():
        user_languages[user_id] = context.args[0]
        await update.message.reply_text(f"Language set to {context.args[0].capitalize()}.")
    else:
        await update.message.reply_text("Please specify a valid language: 'english' or 'hindi'.")

def run_bot():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("setlanguage", set_language))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling(timeout=30)

def start_bot():
    bot_thread = threading.Thread(target=asyncio.run, args=(run_bot(),))
    bot_thread.start()

root = tk.Tk()
root.title("Narcotics Detection Bot")
root.geometry("400x300")
root.configure(bg="#1e1e2d")

title_label = tk.Label(root, text="Narcotics Detection Bot", font=("Helvetica", 20, "bold"), fg="white", bg="#1e1e2d")
title_label.pack(pady=20)

def create_round_button(master, text, command):
    button = tk.Button(master, text=text, command=command, font=("Helvetica", 14), fg="white", bg="#3a3a4f", bd=0,
                       activebackground="#5a5a7f", highlightthickness=0, relief="flat")
    button.pack(pady=10)
    button.configure(height=2, width=20)
    
    def on_enter(e):
        button['background'] = '#5a5a7f'
    def on_leave(e):
        button['background'] = '#3a3a4f'
    
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    return button

start_button = create_round_button(root, "Start NarcX", start_bot)
stop_button = create_round_button(root, "Stop NarcX", root.quit)

root.mainloop()
