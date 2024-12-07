from hashlib import sha256

def hash_pair(left, right):
    return sha256((left + right).encode()).hexdigest()

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions
        self.root = self.build_tree(transactions)

    def build_tree(self, transactions):
        if len(transactions) == 1:
            return transactions[0]
        new_level = []
        for i in range(0, len(transactions), 2):
            left = transactions[i]
            right = transactions[i + 1] if i + 1 < len(transactions) else transactions[i]
            new_level.append(hash_pair(left, right))
        return self.build_tree(new_level)
