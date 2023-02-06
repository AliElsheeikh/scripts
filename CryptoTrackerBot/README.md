# CryptoTrackerBot
A script that tracks the price of a cryptocurrency and sends updates to a Telegram bot.

## Requirements
- requests library
```
pip install requests
```
## Setup
- Create a Telegram bot by talking to the BotFather. You'll receive a bot_token.
- Create a new group on Telegram and add the bot to it. Take note of the group's `chat_id`.
- Clone this repository or download the script.
- Open the script in your favorite text editor and replace the placeholders in the following variables:
   - `symbol`: The `symbol` of the cryptocurrency you want to track (e.g. ADA, BTC).
   - `bot_token`: The token received from BotFather.
   - `chat_id`: The chat ID of the group you created.
   - `num_of_coins`: The number of coins you have.
   - `purchase_price`: The price you bought the coins at.
   - Run the script with `python CryptoTrackerBot.py`.  
   
The bot will now send updates to the Telegram group every 60 seconds with the latest price of the cryptocurrency and the profit/loss based on the purchase price.

## Note
- The price of the cryptocurrency is fetched from the Coinbase API. 
- The script is set to update every 60 seconds, but you can adjust the time.sleep duration to your preference.
