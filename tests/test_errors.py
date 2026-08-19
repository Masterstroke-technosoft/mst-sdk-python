import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from blockchain_sdk import Client, Errors


def test_wallet_error_on_invalid_key():
    with pytest.raises(Errors.WalletError):
        Client("http://localhost:8545", "invalid-key")


def test_transaction_error_on_missing_destination():
    client = Client.create_random("https://testnetrpc.mstblockchain.com")
    with pytest.raises(Errors.TransactionError):
        client.signer.send_native(None, "1000")


def test_provider_error_on_invalid_rpc():
    client = Client("https://invalid-rpc-url-123.com")
    with pytest.raises(Errors.ProviderError):
        client.provider.get_block_number()
