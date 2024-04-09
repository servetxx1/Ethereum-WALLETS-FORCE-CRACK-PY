import random
import requests
from mnemonic import Mnemonic
from eth_account import Account

TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

def generate_eth_address():
    mnemo = Mnemonic("english")
    wordlist = mnemo.wordlist
    mnemonic = " ".join(random.sample(wordlist, 12))
    seed = mnemo.to_seed(mnemonic)
    private_key = Account.from_key(seed[:32])._key_obj
    eth_address = private_key.public_key.to_checksum_address()
    return mnemonic, eth_address

def check_eth_balance(api_key, address):
    api_url = "https://api.etherscan.io/api"
    module = "account"
    action = "balance"
    tag = "latest"

    params = {
        "module": module,
        "action": action,
        "address": address,
        "tag": tag,
        "apikey": api_key
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        data = response.json()

        if data["status"] == "1" and "result" in data:
            balance_wei = int(data["result"])
            balance_eth = balance_wei / 1e18
            return balance_eth
        else:
            return None
    except requests.exceptions.RequestException as err:
        print(f"Hata oluştu: {err}")
        return None

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Telegram mesajı gönderme hatası: {err}")
        return None

def process_eth_address(api_key):
    mnemonic, eth_address = generate_eth_address()
    balance = check_eth_balance(api_key, eth_address)

    message = f"Mnemonic: {mnemonic}\nETH Adresi: {eth_address}\nBakiye: {balance} ETH\n"

    print(message)

    # Bakiye 0.0'dan farklı ise bildirim gönder
    if balance != 0.0:
        send_telegram_message(message)

def main():
        api_key = "YOUR_ETHERSCAN_API_KEY"

        while True:
            process_eth_address(api_key)


if __name__ == "__main__":
    main()
