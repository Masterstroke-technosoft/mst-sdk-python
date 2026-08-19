from blockchain_sdk import Client
from blockchain_sdk.utils.constants import DEFAULT_RPC_URL

# Generate a random wallet
client = Client.create_random(DEFAULT_RPC_URL)
print("Address:", client.signer.address)
print("Private key:", client.signer.get_private_key())

# Balance (requires network access to the RPC)
balance = client.provider.get_balance(client.signer.address)
print("Balance:", balance)
