import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.data = data
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.data}{self.timestamp}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        while not self.hash.startswith('0' * difficulty):
            self.nonce += 1
            self.hash = self.compute_hash()
