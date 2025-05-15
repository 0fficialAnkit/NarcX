# #http://127.0.0.1:5000/
# from flask import Flask, request, render_template
# import requests
# import json
# from datetime import datetime
# import socket

# app = Flask(__name__)

# TOKEN = "7279484881:AAHQN-E1AAhZZyVVfPhG4U40-rWrvc6Aewk"
# POLICE_GROUP_CHAT_ID = "1187069468"

# narcotics_words =  {
#     "english":[
#         "💊","weed" "drugs","drug", "cocaine", "heroin", "meth", "ecstasy", "weed", "maruana", "mayuana", "hash", "hashes", "yaba", "yava", 
#         "marijuana", "maal", "buy", "narco", "drug", "lsd", "pills", "methamphetamine", "morphine", "afim", "afeem", "affem", "affeem", "ufim",
#         "ufeem", "methamine", "delivery", "mdma", "speed", "ketamin", "pudiya", "reggi", "dro", "top shelf", "sour D", "greens", "joint", "paper", 
#         "high", "Crystal", "Opium", "steroids", "powder", "pooriya", "buttfunk", "fluff", "crank", "coke", "blotter", "ludes", 
#         "boomers", "Lady Bubbles", "stuff", "stuffs", "crack", "pot", "pott" , "deal", "hemp", "opium poppy", "coca leaf", "coca",
#         "dealer", "trafficking", "shipment", "distribution", "smuggle", "blackmarket", "calmpose", "bong", 
#         "Addict" , "burnout" , "dopehead" , "dope" , "druggie" , "fiend" , "hophead" , 
#         "junkie" , "stoner" , "user" , "zombie", "white powder", "grass", "chitta", "chita", "charas", "doda", "phukki",
#         "satta", "babu", "kali", "tadi", "desi", "ghas", "bhang", "cannabis", "gard", "molly", "party drug", "love drug", "acid", "blotter", 
#         "hahish", "husk", "stash", "cash", "crystal", " Scooby Snacks", "dope", "herb", "candy", "grass tree", "wack"
#     ],
#     "hindi":[
#         "ड्रग्स", "कोकीन", "हेरोइन", "मेथ", "एक्स्टसी", "गांजा", "मारुआना", "मायुना",
#     "चरस", "चरस", "याबा", "यावा", "मारिजुआना", "माल", "खरीद", "नारको", "नशा", 
#     "एलएसडी", "गोलियां", "मेथामफेटामाइन", "मॉर्फिन", "मेथामिन", "डिलीवरी", "एमडीएमए", 
#     "स्पीड", "केटामिन", "पुड़िया", "रेग्गी", "ड्रॉ", "टॉप शेल्फ", "सॉर डी", "हरी पत्तियां", 
#     "जॉइंट", "पेपर", "नशे में", "क्रिस्टल", "अफीम", "स्टेरॉयड", "पाउडर", "पुड़िया", "बटफंक", 
#     "बूमर्स", "लेडी बबल्स", "सामान", "सामान", "क्रैक", "पॉट", "पॉट", "सौदा", 
#     "डीलर", "तस्करी", "शिपमेंट", "वितरण", "तस्करी करना", "काला बाजार", 
#     "नशेड़ी", "बर्नआउट", "डोपहेड", "डोपर", "ड्रगी", "शैतान", "हॉपहेड", 
#     "जंकी", "स्टोनर", "उपभोक्ता", "ज़ोंबी", "सफेद पाउडर", "घास", "चिट्टा", "चिता", "चरस", 
#     "डोडा", "फुक्की", "सट्टा", "बाबू", "काली", "ताड़ी", "देसी", "घास", "भांग", 
#     "गांजा", "गार्ड", "माली", "पार्टी ड्रग", "लव ड्रग", "एसिड", "ब्लॉटर", 
#     "हशीश", "भूसी", "माल", "नकद", "क्रिस्टल", "स्कूबी स्नैक्स", "डोप", "जड़ी-बूटी", 
#     "कैंडी", "घास का पेड़", "जूस", "वैक", "बर्फ"
#     ],
#     "portugues": [
#         "drogas", "cocaína", "heroína", "metanfetamina", "ecstasy", "maconha", "marijuna", "marijuana", "haxixe", "haxixes", 
#     "yaba", "yava", "marijuana", "maal", "comprar", "narco", "droga", "lsd", "comprimidos", "metanfetamina", "morfina", 
#     "metamina", "entrega", "mdma", "speed", "cetamina", "pudiya", "reggi", "dro", "top shelf", "sour d", "verdes", 
#     "cigarro de maconha", "papel", "alta", "cristal", "opio", "esteroides", "pó", "pooriya", "buttfunk", 
#     "boomers", "lady bubbles", "coisas", "coisas", "crack", "erva", "erva", "negocio", 
#     "dealer", "trafico", "envio", "distribuição", "contrabando", "mercado negro", 
#     "viciado", "esgotado", "cabeca de dope", "usador de dope", "drogado", "dependente", "viciado", 
#     "junkie", "maconheiro", "usuario", "zumbi", "po branco", "erva", "chitta", "chita", "charas", "doda", "phukki",
#     "satta", "babu", "kali", "tadi", "desi", "ghas", "bhang", "cannabis", "gard", "molly", "droga de festa", 
#     "droga do amor", "acido", "blotter", "haxixe", "casca", "estoque", "dinheiro", "cristal", "scooby snacks", "dope", 
#     "erva", "doce", "arvore de erva", "suco", "ruim", "neve"
#     ]
#         }
# 9
# def get_server_ip():
#     hostname = socket.gethostname()
#     return socket.gethostbyname(hostname)

# def send_alert(user_info, message):
#     alert_message = (
#         f"🚨 Alert: Narcotics-related activity detected!\n\n"
#         f"User Info:\n"
#         f" - IP: {user_info['ip']}\n"
#         f" - Location: {user_info['location']}\n"
#         f" - User-Agent: {user_info['user_agent']}\n"
#         f" - OS: {user_info['os']}\n"
#         f" - Server IP: {get_server_ip()}\n"
#         f" - Time (IST): {user_info['time']}\n"
#         f"Message: '{message}'\n"
#     )
#     requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={
#         'chat_id': POLICE_GROUP_CHAT_ID,
#         'text': alert_message
#     })

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/check', methods=['POST'])
# def check():
#     user_message = request.form['message']
#     user_info = {
#         'ip': request.remote_addr,
#         'location': "User's Location", 
#         'user_agent': request.user_agent.string,
#         'os': request.user_agent.platform,
#         'time': datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')
#     }

#     if any(word in user_message for word in narcotics_words):
#         send_alert(user_info, user_message)
#         return "checking for your requirements"
#     else:
#         return "No narcotics-related words detected."

# if __name__ == '__main__':
#     app.run(debug=True)










# from flask import Flask, request, render_template
# import requests
# import json
# from datetime import datetime
# import socket

# app = Flask(__name__)

# TOKEN = "7279484881:AAHQN-E1AAhZZyVVfPhG4U40-rWrvc6Aewk"
# POLICE_GROUP_CHAT_ID = "1187069468"

# narcotics_words =  {
#     "english": [
#         "💊", "weed", "drugs", "drug", "cocaine", "heroin", "meth", "ecstasy", "marijuana", 
#         "hash", "yaba", "narco", "lsd", "pills", "mdma", "speed", "ketamine", "crystal", 
#         "opium", "steroids", "cocaine", "crack", "hemp", "dealer", "shipment", "smuggle", 
#         "bong", "junkie", "stoner", "cannabis", "molly", "party drug", "acid", "stash", 
#         "cash", "dope", "grass", "scooby snacks", "powder"
#     ],
#     "hindi": [
#         "ड्रग्स", "कोकीन", "हेरोइन", "मेथ", "गांजा", "मारुआना", "चरस", "याबा", "एलएसडी", 
#         "गोलियां", "मेथामफेटामाइन", "मॉर्फिन", "डिलीवरी", "स्पीड", "केटामिन", "पुड़िया", 
#         "रेग्गी", "जॉइंट", "अफीम", "स्टेरॉयड", "पाउडर", "सफेद पाउडर", "घास", "सौदा", 
#         "काला बाजार", "नशेड़ी", "डोपहेड", "ड्रगी", "शैतान", "जंकी", "स्टोनर", "ज़ोंबी", 
#         "क्रिस्टल", "अफीम"
#     ],
#     "portugues": [
#         "drogas", "cocaína", "heroína", "metanfetamina", "ecstasy", "maconha", "haxixe", 
#         "lsd", "comprimidos", "mdma", "speed", "ketamina", "cristal", "opium", "esteroides", 
#         "pó", "trafico", "mercado negro", "viciado", "junkie", "cannabis", "droga de festa", 
#         "ácido", "erva", "dope", "erva"
#     ]
# }

# def get_server_ip():
#     hostname = socket.gethostname()
#     return socket.gethostbyname(hostname)

# def send_alert(user_info, message):
#     alert_message = (
#         f"🚨 Alert: Narcotics-related activity detected!\n\n"
#         f"User Info:\n"
#         f" - IP: {user_info['ip']}\n"
#         f" - Location: {user_info['location']}\n"
#         f" - User-Agent: {user_info['user_agent']}\n"
#         f" - OS: {user_info['os']}\n"
#         f" - Server IP: {get_server_ip()}\n"
#         f" - Time (IST): {user_info['time']}\n"
#         f"Message: '{message}'\n"
#     )
#     requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={
#         'chat_id': POLICE_GROUP_CHAT_ID,
#         'text': alert_message
#     })

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/check', methods=['POST'])
# def check():
#     user_message = request.form['message'].lower()  # Make the message case-insensitive
#     user_info = {
#         'ip': request.remote_addr,
#         'location': "User's Location",  # Replace with actual location logic if needed
#         'user_agent': request.user_agent.string,
#         'os': request.user_agent.platform,
#         'time': datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')
#     }

#     # Flatten the narcotics words list across all languages
#     all_narcotics_words = []
#     for language in narcotics_words:
#         all_narcotics_words.extend(narcotics_words[language])
    
#     # Check if any narcotic word is present in the user's message
#     if any(word in user_message for word in all_narcotics_words):
#         send_alert(user_info, user_message)
#         return "Narcotics-related content detected."
#     else:
#         return "No narcotics-related words detected."

# if __name__ == '__main__':
#     app.run(debug=True)





#  #working file 
import re
from flask import Flask, request, render_template
import requests
from datetime import datetime
import socket

app = Flask(__name__)

TOKEN = "7279484881:AAHQN-E1AAhZZyVVfPhG4U40-rWrvc6Aewk"
POLICE_GROUP_CHAT_ID = "1187069468" #ankit
# POLICE_GROUP_CHAT_ID = "5205657737" #kavya
# POLICE_GROUP_CHAT_ID = "7512827887" #sumit
# POLICE_GROUP_CHAT_ID = "1212425128" #ruchika
# POLICE_GROUP_CHAT_ID = "6061184898" #anshu
# POLICE_GROUP_CHAT_ID = "6718957128" #vishnu

narcotics_words =  {
    "english": [
        "💊", "drugs","drug","junk", "junc", "cocaine", "heroin", "meth", "ecstasy", "weed", "maruana", "mayuana", "hash", "hashes", "yaba", "yava", 
        "marijuana", "maal", "buy", "narco", "drug", "lsd", "pills", "methamphetamine", "morphine", "afim", "afeem", "affem", "affeem", "ufim",
        "ufeem","saman", "methamine", "delivery", "mdma", "speed", "ketamin", "pudiya", "reggi", "dro", "top shelf", "sour D", "greens", "joint", "paper", 
        "high", "Crystal", "Opium", "steroids", "powder", "pooriya", "buttfunk", "fluff", "crank", "coke", "blotter", "ludes", 
        "boomers", "Lady Bubbles", "stuff", "stuffs", "crack", "pot", "pott" , "deal", "hemp", "opium poppy", "coca leaf", "coca",
        "dealer", "trafficking", "shipment", "distribution", "smuggle", "blackmarket", "calmpose", "bong", 
        "Addict" , "burnout" , "dopehead" , "dope" , "druggie" , "fiend" , "hophead" , 
        "junkie" , "stoner" , "user" , "zombie", "white powder", "grass", "chitta", "chita", "charas", "doda", "phukki",
        "satta", "babu", "kali", "tadi", "desi", "ghas", "bhang", "cannabis", "gard", "molly", "party drug", "love drug", "acid", "blotter", 
        "hahish", "husk", "stash", "cash", "crystal", " Scooby Snacks", "dope", "herb", "candy", "grass tree", "wack","ankit"  
        ],
    "hindi": [ 
        "ड्रग्स", "कोकीन", "हेरोइन", "मेथ", "एक्स्टसी", "गांजा", "मारुआना", "मायुना",
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
    ],
    "portugues": [
        "drogas", "cocaína", "heroína", "metanfetamina", "ecstasy", "maconha", "marijuna", "marijuana", "haxixe", "haxixes", 
"yaba", "yava", "marijuana", "maal", "comprar", "narco", "droga", "lsd", "comprimidos", "metanfetamina", "morfina", 
"metamina", "entrega", "mdma", "speed", "cetamina", "pudiya", "reggi", "dro", "top shelf", "sour d", "verdes", 
"cigarro de maconha", "papel", "alta", "cristal", "opio", "esteroides", "pó", "pooriya", "buttfunk", 
"boomers", "lady bubbles", "coisas", "coisas", "crack", "erva", "erva", "negocio", 
"dealer", "trafico", "envio", "distribuição", "contrabando", "mercado negro", 
"viciado", "esgotado", "cabeca de dope", "usador de dope", "drogado", "dependente", "viciado", 
"junkie", "maconheiro", "usuario", "zumbi", "po branco", "erva", "chitta", "chita", "charas", "doda", "phukki",
"satta", "babu", "kali", "tadi", "desi", "ghas", "bhang", "cannabis", "gard", "molly", "droga de festa", 
"droga do amor", "acido", "blotter", "haxixe", "casca", "estoque", "dinheiro", "cristal", "scooby snacks", "dope", 
"erva", "doce", "arvore de erva", "suco", "ruim", "neve"
    ]
}

def get_server_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)
# 
def get_location_from_ip(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        location = data['loc'].split(',') 
        return {
            'latitude': location[0],
            'longitude': location[1]
        }
    except Exception as e:
        print(f"Error getting location: {e}")
        return {
            'latitude': 'Unknown',
            'longitude': 'Unknown'
        }
# 

def send_alert(user_info, message):
    alert_message = (
        f"🚨 Alert: Narcotics-related activity detected!\n\n"
        f"User Info:\n"
        f" - IP: {user_info['ip']}\n"
        f" - Location: {user_info['location']}\n"
        f" - User-Agent: {user_info['user_agent']}\n"
        f" - OS: {user_info['os']}\n"
        f" - Server IP: {get_server_ip()}\n"
        f" - Time (IST): {user_info['time']}\n"
        f"Message: '{message}'\n"
    )
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={
        'chat_id': POLICE_GROUP_CHAT_ID,
        'text': alert_message
    })

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    user_message = request.form['message'].lower()  
    user_info = {
        'ip': request.remote_addr,
        'location': "User's Location",  
        'user_agent': request.user_agent.string,
        'os': request.user_agent.platform,
        'time': datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')
    }


    all_narcotics_words = []
    for language in narcotics_words:
        all_narcotics_words.extend(narcotics_words[language])


    narcotics_pattern = r'\b(?:' + '|'.join(map(re.escape, all_narcotics_words)) + r')\b'

    if re.search(narcotics_pattern, user_message):
        send_alert(user_info, user_message)
        return "Checking your requirements."
    else:
        return "Your requirements can't be fulfilled."

if __name__ == '__main__':
    app.run(debug=True)


#  #ms file 


# import re
# from flask import Flask, request, render_template
# import requests
# from datetime import datetime
# import socket
# import pandas as pd
# import os

# app = Flask(__name__)

# TOKEN = "7279484881:AAHQN-E1AAhZZyVVfPhG4U40-rWrvc6Aewk"
# POLICE_GROUP_CHAT_ID = "1187069468"

# # Narcotics keywords in multiple languages
# narcotics_words = {
#     "english": [
#         "💊", "drugs", "drug", "junk", "cocaine", "heroin", "meth", "ecstasy",
#         "weed", "marijuana", "hash", "delivery", "mdma", "speed", "pills", "pot"
#     ],
#     "hindi": [
#         "ड्रग्स", "कोकीन", "हेरोइन", "मेथ", "गांजा", "मारिजुआना", "नशा"
#     ],
#     "portugues": [
#         "drogas", "cocaína", "heroína", "metanfetamina", "maconha", "marijuana"
#     ]
# }

# # Function to get server IP address
# def get_location_from_ip(ip):
#     try:
#         response = requests.get(f"https://ipinfo.io/{ip}/json")
#         data = response.json()
#         if 'loc' in data:
#             location = data['loc'].split(',')
#             return {
#                 'latitude': location[0],
#                 'longitude': location[1]
#             }
#         else:
#             return {
#                 'latitude': 'Unknown',
#                 'longitude': 'Unknown'
#             }
#     except Exception as e:
#         print(f"Error getting location: {e}")
#         return {
#             'latitude': 'Unknown',
#             'longitude': 'Unknown'
#         }
# def get_server_ip():
#     try:
#         hostname = socket.gethostname()
#         server_ip = socket.gethostbyname(hostname)
#         return server_ip
#     except Exception as e:
#         print(f"Error getting server IP: {e}")
#         return 'Unknown'


# # Function to send alert message
# def send_alert(user_info, message):
#     alert_message = (
#         f"🚨 Alert: Narcotics-related activity detected!\n\n"
#         f"User Info:\n"
#         f" - IP: {user_info['ip']}\n"
#         f" - Location: {user_info['location']}\n"
#         f" - User-Agent: {user_info['user_agent']}\n"
#         f" - OS: {user_info['os']}\n"
#         f" - Server IP: {get_server_ip()}\n"
#         f" - Time (IST): {user_info['time']}\n"
#         f"Message: '{message}'\n"
#     )
#     requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={
#         'chat_id': POLICE_GROUP_CHAT_ID,
#         'text': alert_message
#     })
#     # Store alert in Excel
#     store_alert_in_excel(user_info, message)

# # Function to store alert messages in Excel  r'D:\Python files\SIH\narcotics_detection'
# def store_alert_in_excel(user_info, message):
#     # Define the full path for the Excel file
#     file_path = os.path.join(os.getcwd(), 'alerts.xlsx')
    
#     # Create DataFrame for new alert
#     new_alert = {
#         'IP': user_info['ip'],
#         'Location': user_info['location'],
#         'User-Agent': user_info['user_agent'],
#         'OS': user_info['os'],
#         'Server IP': get_server_ip(),
#         'Time': user_info['time'],
#         'Message': message
#     }
    
#     # Check if the Excel file exists
#     if os.path.exists(file_path):
#         # If it exists, append the new alert to it
#         df = pd.read_excel(file_path)
#         new_alert_df = pd.DataFrame([new_alert])  # Create DataFrame for the new alert
#         df = pd.concat([df, new_alert_df], ignore_index=True)  # Use pd.concat instead of append
#     else:
#         # If it doesn't exist, create a new DataFrame
#         df = pd.DataFrame([new_alert])
    
#     # Save DataFrame to Excel file
#     df.to_excel(file_path, index=False)

 

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/check', methods=['POST'])
# def check():
#     user_message = request.form['message'].lower()
#     user_info = {
#         'ip': request.remote_addr,
#         'location': get_location_from_ip(request.remote_addr),
#         'user_agent': request.user_agent.string,
#         'os': request.user_agent.platform,
#         'time': datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')
#     }

#     # Combine all narcotics words for regex search
#     all_narcotics_words = []
#     for language in narcotics_words:
#         all_narcotics_words.extend(narcotics_words[language])

#     narcotics_pattern = r'\b(?:' + '|'.join(map(re.escape, all_narcotics_words)) + r')\b'

#     if re.search(narcotics_pattern, user_message):
#         send_alert(user_info, user_message)
#         return "Checking your requirements."
#     else:
#         return "Your requirements can't be fulfilled."

# if __name__ == '__main__':
#     app.run(debug=True)
