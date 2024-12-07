import time
import hashlib

class ProofOfWork:
    def __init__(self, difficulty):
        self.difficulty = difficulty  # Number of leading zeros required in the hash

    def mine(self, block):
        """
        Mines a block by finding a nonce that satisfies the difficulty condition.
        """
        start_time = time.time()
        while not block.hash.startswith('0' * self.difficulty):
            block.nonce += 1
            block.hash = block.compute_hash()
        end_time = time.time()
        print(f"Block mined: {block.hash} (Nonce: {block.nonce}, Time: {end_time - start_time:.2f}s)")
        return block.hash

    def validate(self, block):
        """
        Validates a block by checking its hash against the difficulty.
        """
        return block.hash.startswith('0' * self.difficulty) and block.hash == block.compute_hash()
