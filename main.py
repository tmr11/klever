import os
import random
from web3 import Web3
import requests
from dotenv import load_dotenv
from settings import TOKENS_TO, MAX_AMOUNT, MIN_AMOUNT, MAX_GAS_PRICE, CHAIN_ID, TOKEN_FROM, MAX_GAS_LIMIT

# Load environment variables (e.g., private key and node URL)
load_dotenv()

# Connect to the Base network
RPC_URL = os.getenv('BASE_RPC_URL')  # URL of the Base node
PRIVATE_KEY = os.getenv('PRIVATE_KEY')  # Private key for signing transactions
ADDRESS = os.getenv('ADDRESS')  # Your wallet address

web3 = Web3(Web3.HTTPProvider(RPC_URL))

if not web3.isConnected():
    print("Connection error to the network")
    exit()

JUMPER_EXCHANGE_API = "https://li.quest/v1/quote/"

def get_random_eth_amount(min_eth, max_eth):
    """Generate a random amount of ETH and convert it to wei."""
    amount = random.uniform(min_eth, max_eth)
    amount_in_wei = web3.toWei(amount, 'ether')
    return amount_in_wei

def get_random_token(tokens):
    """Select a random token from the list."""
    return random.choice(tokens)

def get_gas_price():
    """Get the current gas price and check if it exceeds the limit."""
    gas_price = web3.eth.gas_price
    gas_price_in_gwei = web3.fromWei(gas_price, 'gwei')
    if gas_price_in_gwei > MAX_GAS_PRICE:
        raise Exception(f"Current gas price {gas_price_in_gwei} Gwei exceeds the limit.")
    return gas_price

def send_raw_data(raw_data):
    """Sign and send a raw transaction."""
    nonce = web3.eth.getTransactionCount(ADDRESS)

    tx = {
        'nonce': nonce,
        'to': None,
        'value': 0,
        'gas': MAX_GAS_LIMIT,
        'gasPrice': get_gas_price(),
        'data': raw_data,
        'chainId': CHAIN_ID
    }

    signed_tx = web3.eth.account.signTransaction(tx, PRIVATE_KEY)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

    return web3.toHex(tx_hash)

def perform_swap(to_token, amount):
    """Perform a swap using the Jumper Exchange API."""
    dat = {
        "fromChain": CHAIN_ID,
        "toChain": CHAIN_ID,
        "fromToken": TOKEN_FROM,
        "toToken": to_token,
        "fromAmount": amount,
        "fromAddress": ADDRESS
    }

    response = requests.get(JUMPER_EXCHANGE_API, params=dat)

    if response.status_code == 200:
        data = response.json()

        try:
            tx_hash = send_raw_data(data['transactionRequest']['data'])
            print(f"Transaction sent. Hash: {tx_hash}")

        except Exception as e:
            print(f"Error: {e}")

    else:
        print(f"Error executing swap: {response.text}")

def main():
    try:
        amount = get_random_eth_amount(MIN_AMOUNT, MAX_AMOUNT)
        amount_eth = web3.fromWei(amount, 'ether')
        print(f"Random token amount for swap: {amount_eth}")

        to_token = get_random_token(TOKENS_TO)
        print(f"Swapping from {TOKEN_FROM} to {to_token}")

        gas_price = get_gas_price()
        print(f"Current gas price: {web3.fromWei(gas_price, 'gwei')} Gwei")

        # Execute the swap
        perform_swap(to_token, amount)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

