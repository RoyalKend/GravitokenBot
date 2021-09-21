import json
import Constans as keys
from telegram.ext import *
import cmc

print("Bot started...")

def data():
    with open("coindata.json") as json_file:
        coindata = json.load(json_file)

    text = f"""1 $GRV ➡️ {coindata['peronetoken']}

Total supply {coindata['supply']} GRV

 ▫️ USD: {coindata['singleprice']}

 ▫️ BTC: {coindata['btcprice']}

 ▫️ ETH: {coindata['ethprice']}

 ▫️ 24HR volume: ${coindata['volume24h']} (<a href='{coindata['source']}/'>source</a>)"""
    return text


def start_command(update, context):
    update.message.reply_text('Type /help to find out all commands')


def help_command(update, context):
    update.message.reply_text("""⚙️ You can run the following commands:
/rebasing - How does rebasing work?
/invest - Why Invest in GRV
/FEATURE1 - Gravitoken SOLAR SAIL """)


def rebasing_command(update, context):
    update.message.reply_text("""As an Elastic Supply token, GRAVITOKEN uses a negative rebasing to reduce the total supply of tokens in order to increase the value of each token over time. This means the amount of tokens in your wallet will decrease over time, but the value of each token will increase. 

Imagine you bought 25% of the market cap. Rebasing means your token amount goes down, but the % of the total is the same.

The value of your investment is not measured by the amount of tokens you possess. Please see the FAQ section here to understand how to track the value of your investment.""")


def invest_command(update, context):
    update.message.reply_text("""GRAVITOKEN (GRV) is a project born out of the need for reliable price rises amongst a sea of volatility and red candles. We've created a token and a community you can join with confidence. Gravitoken is mathematically designed to increase in price every hour, allowing you to be worry-free knowing your investment is protected through a constantly increasing liquidity pool solidifying the price floor.""")

def FEATURE1_command(update, context):
    update.message.reply_text("""GRAVITOKEN SOLAR SAIL is the increasing price peg pre-built into Gravitoken, meaning it's been mathematically designed to rise in price every hour through rebasing, with a minimum rise of 9.81% every 8 hours - until each token reaches a guaranteed $1,337,000""")


def error(update, context):
    print(f"update {update} cause error {context.error}")

def main():
    updater = Updater(keys.BOT_API_KEY, use_context=True)
    dp = updater.dispatcher

    cmc.startup()

    dp.add_handler(CommandHandler("rebasing", rebasing_command))
    dp.add_handler(CommandHandler("investing", invest_command))
    dp.add_handler(CommandHandler("FEATURE1", FEATURE1_command))




    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()