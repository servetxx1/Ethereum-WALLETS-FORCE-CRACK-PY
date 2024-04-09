# ETHERUM-WALLETS-FORCE-CRACK-PY
# Ethereum Address Checker

This Python script generates Ethereum addresses and checks their balances using the Etherscan API. If the balance of an address is non-zero, it sends a notification to a specified Telegram chat using a Telegram bot.

## Requirements

- Python 3.x
- `mnemonic` library
- `eth_account` library
- `requests` library

Install the required libraries using pip:


pip install mnemonic eth-account requests

Open the main.py file and replace the placeholder values with your actual Ethereum API key, Telegram bot token, and chat ID.

Run the script:

bash
Copy code
```bash
python main.py

Usage
The script continuously generates Ethereum addresses, checks their balances, and sends notifications to the specified Telegram chat if the balance is non-zero.

Customization
Adjust the number of addresses to be checked by modifying the process_eth_address() function.
Customize the message format or notification logic as needed.
License
