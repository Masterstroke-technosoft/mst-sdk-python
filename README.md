# MST Blockchain SDK (Python)

A modular and lightweight blockchain development kit for interacting with any MST-compatible network. This is a Python port of the [MST Blockchain SDK](../basic-bc-sdk) (JS), built on `web3.py` and `eth-account`, providing the same easy-to-use abstractions for providers, signers, and contract interactions.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Setup](#setup)
- [Quick Start](#quick-start)
  - [1. Initialize the Client](#1-initialize-the-client)
  - [2. Generate a Random Wallet](#2-generate-a-random-wallet)
  - [3. Check Account Balance (via Provider)](#3-check-account-balance-via-provider)
  - [4. Estimate Gas & Send Transactions](#4-estimate-gas--send-transactions)
  - [5. Deploy Contract & Get Address](#5-deploy-contract--get-address)
- [Core Modules](#core-modules)
  - [1. Client](#1-client)
  - [2. Provider](#2-provider-read-only)
  - [3. Signer](#3-signer-identity--writing)
  - [4. Errors](#4-errors)
- [Testing](#testing)
- [License](#license)

## Features

- **Client Orchestration**: Universal entry point for all SDK features.
- **Provider Management**: Simple JSON-RPC provider (via `web3.py`) for fetching block data and account state.
- **Secure Signing**: Integrated `Signer` using `eth-account` for secure transaction signing and address management.
- **Balances**: Built-in utilities for checking native token balances.

## Installation

```bash
pip install -r requirements.txt
```

For local development (so the `blockchain_sdk` package resolves from `src/`), install it in editable mode:

```bash
pip install -e .
```

*(Recommended: do this inside a virtual environment — `python -m venv .venv` then activate it — before installing.)*

## Setup

Copy the example environment file and fill in your details:

```bash
cp .env.example .env
```

```
RPC_URL=https://testnetrpc.mstblockchain.com
PRIVATE_KEY=
```

- `RPC_URL`: the JSON-RPC endpoint to connect to (defaults to the MST testnet).
- `PRIVATE_KEY`: your wallet's private key, only required for signing/sending transactions. Leave blank for read-only usage or when generating a random wallet.

Never commit a filled-in `.env` file — it's git-ignored by default.

## Quick Start

### 1. Initialize the Client

```python
from blockchain_sdk import Client

rpc_url = "https://testnetrpc.mstblockchain.com"
private_key = "0x..."

client = Client(rpc_url, private_key)
```

### 2. Generate a Random Wallet

```python
# Creates a new client with a fresh random private key
client = Client.create_random(rpc_url)
print(f"Generated Address: {client.signer.address}")
print(f"Private Key: {client.signer.get_private_key()}")
```

### 3. Check Account Balance (via Provider)

```python
address = "0x..."
# Access balance through the provider
balance = client.provider.get_balance(address)
print(f"Address Balance: {balance} wei")
```

### 4. Estimate Gas & Send Transactions

```python
to_address = "0x..."
amount = "1000000000000000000"  # 1 TOKEN

# 1. Estimate gas first
gas_limit = client.signer.estimate_gas("sendNative", [to_address, amount])
print(f"Estimated Gas: {gas_limit}")

# 2. Send the transaction
tx_hash = client.signer.send_native(to_address, amount)
print(f"Transaction Hash: {tx_hash}")
```

### 5. Deploy Contract & Get Address

```python
abi = [...]
bytecode = "0x..."
args = ["InitialValue"]

# 1. Start deployment
tx_hash = client.signer.deploy(abi, bytecode, args)
print(f"Deployment Hash: {tx_hash}")

# 2. Wait for it to be mined
receipt = client.provider.wait_for_transaction(tx_hash)

# 3. Get the new contract address
print(f"Contract Deployed at: {receipt.contractAddress}")
```

## Core Modules

### 1. `Client`
The root container and main entry point.
- `Client.create_random(rpc_url)`: Returns a new `Client` instance with a random signer.
- `provider`: Instance of `Provider`.
- `signer`: Instance of `Signer` (if `private_key` provided).

### 2. `Provider` (Read-only)
Accessed via `client.provider`.
- `get_block_number()`: Returns the latest block.
- `get_balance(address)`: Fetches raw balance.
- `get_transaction_receipt(tx_hash)`: Fetches the receipt of a mined txn.
- `wait_for_transaction(tx_hash)`: Waits for a txn to be mined.
- `estimate_gas(transaction)`: Estimates gas for a raw transaction object.

### 3. `Signer` (Identity & Writing)
Accessed via `client.signer`.
- `Signer.create_random(provider)`: Generates a new random `Signer` attached to a provider.
- `get_private_key()`: Returns the private key of the current wallet.
- `estimate_gas(method, args)`: Estimates gas for Signer methods (`sendNative`, `sendToken`, `deploy`).
- `send_transaction(tx)`: Signs and broadcasts any transaction.
- `send_native(to, amount)`: Shortcut for sending native tokens.
- `send_token(token_address, to, amount)`: Sends ERC20 tokens.
- `deploy(abi, bytecode, args=None)`: Deploys smart contracts.
- `get_address()`: Returns the signer's public address.

### 4. `Errors`
Custom error classes for better debugging (`blockchain_sdk.Errors`).
- `ProviderError`: Network or RPC issues.
- `TransactionError`: Validation or on-chain submission failures.
- `WalletError`: Private key or signer initialization issues.

## Testing

Run the test suite to ensure everything is configured correctly:

```bash
pytest
```

## License

ISC
