from blockchain_sdk import Client

# Generate a random wallet on testnet
client = Client.create_random("testnet")
print("Address:", client.signer.address)
print("Private key:", client.signer.get_private_key())

# Balance (requires network access to the RPC)
balance = client.provider.get_balance(client.signer.address)
print("Balance:", balance)
