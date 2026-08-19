# MST Blockchain SDK (Python)

Python port of the [MST Blockchain SDK](../basic-bc-sdk) JS package, built on `web3.py` and `eth-account`.

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from blockchain_sdk import Client
from blockchain_sdk.utils.constants import DEFAULT_RPC_URL

client = Client(DEFAULT_RPC_URL, "0x...")

# Or generate a random wallet
client = Client.create_random(DEFAULT_RPC_URL)
print(client.signer.address)
print(client.signer.get_private_key())

# Balance
balance = client.provider.get_balance(client.signer.address)

# Send native tokens
tx_hash = client.signer.send_native("0x...", 1000000000000000000)

# Deploy a contract
tx_hash = client.signer.deploy(abi, bytecode, ["InitialValue"])
receipt = client.provider.wait_for_transaction(tx_hash)
print(receipt.contractAddress)
```

## Testing

```bash
pytest
```

## License

ISC
