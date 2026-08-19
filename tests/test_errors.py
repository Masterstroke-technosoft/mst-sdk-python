import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from blockchain_sdk import Client, Provider, Errors


def test_wallet_error_on_invalid_key():
    with pytest.raises(Errors.WalletError):
        Client("testnet", "invalid-key")


def test_transaction_error_on_missing_destination():
    client = Client.create_random("testnet")
    with pytest.raises(Errors.TransactionError):
        client.signer.send_native(None, "1000")


def test_provider_error_on_invalid_rpc():
    provider = Provider("https://invalid-rpc-url-123.com")
    with pytest.raises(Errors.ProviderError):
        provider.get_block_number()


def test_value_error_on_unknown_network():
    with pytest.raises(ValueError):
        Client("nonexistent-network")
