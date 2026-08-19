"""Main SDK Client Class."""

from .provider import Provider
from .signer import Signer


class Client:
    def __init__(self, rpc_url, private_key=None):
        self.provider = Provider(rpc_url)
        self.signer = None
        if private_key:
            self.signer = Signer(private_key, self.provider)

    @staticmethod
    def create_random(rpc_url):
        client = Client(rpc_url)
        client.signer = Signer.create_random(client.provider)
        return client
