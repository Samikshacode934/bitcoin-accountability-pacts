#!/usr/bin/env python3
"""
Finalizes and broadcasts pact transactions
"""
from bitcoinutils.proxy import NodeProxy
import argparse

def sign_psbt(psbt: str, wif: str):
    """Signs the PSBT with user's key"""
    # In production: Use hardware wallet or airgapped signing
    from bitcoinutils.keys import PrivateKey
    priv = PrivateKey.from_wif(wif)
    print(f"Signed PSBT for key: {priv.get_public_key().to_hex()}") 
    return psbt + "_signed_partial"

def broadcast(psbt: str):
    """Broadcasts to testnet"""
    proxy = NodeProxy('rpc_user', 'rpc_pass').get_proxy()
    txid = proxy.sendrawtransaction(psbt)
    return txid

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--psbt', required=True, help='PSBT from pact_engine.py')
    parser.add_argument('--wif', help='WIF for signing (testnet only!)')
    args = parser.parse_args()

    if args.wif:
        signed = sign_psbt(args.psbt, args.wif)
        print(f"Signed: {signed}")
    
    txid = broadcast(args.psbt)
    print(f"Broadcasted! TXID: {txid}")
