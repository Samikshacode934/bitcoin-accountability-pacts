# bitcoin_pact.py - Core functionality
from bitcoinutils.setup import setup
setup('testnet')

def create_pact(goal: str, burn_sats: int):
    print(f"Bitcoin Pact: '{goal}' or burn {burn_sats} sats!")
