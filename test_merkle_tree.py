import pytest
from node.merkle_tree import MerkleTree

# Test building the Merkle tree and getting the root
def test_merkle_tree():
    transactions = ["tx1", "tx2", "tx3", "tx4"]
    merkle_tree = MerkleTree(transactions)

    # Test if Merkle root is correctly computed
    assert merkle_tree.root is not None  # The Merkle root should not be None

# Test hashing function for Merkle tree
def test_hash_pair():
    left = "tx1"
    right = "tx2"
    hashed_pair = "f07c5c7e46cfd52a89d6b0e8edb13cc597efb7cfb5915b94f166bbad881c87de"
    assert merkle_tree.hash_pair(left, right) == hashed_pair
