import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from blockchain_sdk import Client
from blockchain_sdk.utils.constants import DEFAULT_RPC_URL


def test_create_random_has_provider_and_signer():
    client = Client.create_random(DEFAULT_RPC_URL)
    assert client.provider is not None
    assert client.signer is not None
    assert client.signer.address is not None


def test_two_random_clients_have_different_addresses():
    a = Client.create_random(DEFAULT_RPC_URL)
    b = Client.create_random(DEFAULT_RPC_URL)
    assert a.signer.address != b.signer.address


def test_get_private_key_round_trip():
    client = Client.create_random(DEFAULT_RPC_URL)
    pk = client.signer.get_private_key()
    assert pk.startswith("0x")

    client2 = Client(DEFAULT_RPC_URL, pk)
    assert client2.signer.address == client.signer.address


def test_get_block_number_live_rpc():
    client = Client.create_random(DEFAULT_RPC_URL)
    block_number = client.provider.get_block_number()
    assert isinstance(block_number, int)


def test_get_balance_of_fresh_wallet_is_zero():
    client = Client.create_random(DEFAULT_RPC_URL)
    balance = client.provider.get_balance(client.signer.address)
    assert balance == 0
