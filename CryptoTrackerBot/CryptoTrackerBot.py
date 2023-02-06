import requests
import time

# Set the symbol, bot_token, and chat_id
symbol = '[SYMBOL]' #ex 'ETH'
bot_token = '[BOT_TOKEN]'  #ex  '564208165570:BBFaXsfsgfDKjchrvd_TtR3sdfs4k-WDsdacE'
chat_id = '[CHAT_ID]' #ex "1552154523"  you can add id for group or channel or just for your self
url = f"https://api.coinbase.com/v2/prices/{symbol}-USD/spot"

# The number of coins the user bought at the purchase price
num_of_coins = [NUM_OF_COINS]  #ex 1.5
purchase_price = [PURCHASE_PRICE] #ex 1,628.73

def get_price():
    # Get the latest price of the coin
    response = requests.get(url)
    data = response.json()
    price = float(data['data']['amount'])
    return price

def send_message(price, profit_loss):
    message = f"The latest price of {symbol} is ${price:.2f}. Your profit/loss is ${profit_loss:.2f}"
    requests.get(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}")

while True:
    price = get_price()
    current_value = price * num_of_coins
    profit_loss = current_value - (purchase_price * num_of_coins)
    send_message(price, profit_loss)
    print(price, profit_loss)
    
    time.sleep(60) #ex for 20min 60*20