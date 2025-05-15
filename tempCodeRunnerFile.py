import re
from flask import Flask, request, render_template
import requests
from datetime import datetime
import socket
import pandas as pd
import os

app = Flask(__name__)

TOKEN = "7279484881:AAHQN-E1AAhZZyVVfPhG4U40-rWrvc6Aewk"
POLICE_GROUP_CHAT_ID = "1187069468"

# Narcotics keywords in multiple languages
narcotics_words = {
    "english": [
        "💊", "drugs", "drug", "junk", "cocaine", "heroin", "meth", "ecstasy",
        "weed", "marijuana", "hash", "delivery", "mdma", "speed", "pills", "pot"
    ],
    "hindi": [
        "ड्रग्स", "कोकीन", "हेरोइन", "मेथ", "गांजा", "मारिजुआना", "नशा"
    ],
    "portugues": [
        "drogas", "cocaína", "heroína", "metanfetamina", "maconha", "marijuana"
    ]
}

# Function to get server IP address
def get_location_from_ip(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        if 'loc' in data:
            location = data['loc'].split(',')
            return {
                'latitude': location[0],
                'longitude': location[1]
            }
        else:
            return {
                'latitude': 'Unknown',
                'longitude': 'Unknown'
            }
    except Exception as e:
        print(f"Error getting location: {e}")
        return {
            'latitude': 'Unknown',
            'longitude': 'Unknown'
        }
def get_server_ip():
    try:
        hostname = socket.gethostname()
        server_ip = socket.gethostbyname(hostname)
        return server_ip
    except Exception as e:
        print(f"Error getting server IP: {e}")
        return 'Unknown'


# Function to send alert message
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
    # Store alert in Excel
    store_alert_in_excel(user_info, message)

# Function to store alert messages in Excel  r'D:\Python files\SIH\narcotics_detection'
def store_alert_in_excel(user_info, message):
    # Define the full path for the Excel file
    file_path = os.path.join(os.getcwd(), 'alerts.xlsx')
    
    # Create DataFrame for new alert
    new_alert = {
        'IP': user_info['ip'],
        'Location': user_info['location'],
        'User-Agent': user_info['user_agent'],
        'OS': user_info['os'],
        'Server IP': get_server_ip(),
        'Time': user_info['time'],
        'Message': message
    }
    
    # Check if the Excel file exists
    if os.path.exists(file_path):
        # If it exists, append the new alert to it
        df = pd.read_excel(file_path)
        new_alert_df = pd.DataFrame([new_alert])  # Create DataFrame for the new alert
        df = pd.concat([df, new_alert_df], ignore_index=True)  # Use pd.concat instead of append
    else:
        # If it doesn't exist, create a new DataFrame
        df = pd.DataFrame([new_alert])
    
    # Save DataFrame to Excel file
    df.to_excel(file_path, index=False)

 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    user_message = request.form['message'].lower()
    user_info = {
        'ip': request.remote_addr,
        'location': get_location_from_ip(request.remote_addr),
        'user_agent': request.user_agent.string,
        'os': request.user_agent.platform,
        'time': datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')
    }

    # Combine all narcotics words for regex search
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
