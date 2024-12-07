import pytest
from blockchain.blockchain import Blockchain
from blockchain.block import Block

# Test blockchain creation and initial state
def test_create_blockchain():
    blockchain = Blockchain()
    assert len(blockchain.chain) == 1  # Should contain the genesis block
    assert blockchain.chain[0].data == "Genesis Block"  # Genesis block data
    assert blockchain.chain[0].previous_hash == "0"  # Genesis block has no previous hash

# Test adding a block
def test_add_block():
    blockchain = Blockchain()
    blockchain.add_block("Sensor Data Block 1")
    assert len(blockchain.chain) == 2  # Blockchain should now have 2 blocks
    assert blockchain.chain[1].data == "Sensor Data Block 1"
    assert blockchain.chain[1].previous_hash == blockchain.chain[0].hash  # Previous block should be correctly linked

# Test blockchain validation
def test_validate_chain():
    blockchain = Blockchain()
    blockchain.add_block("Sensor Data Block 1")
    assert blockchain.validate_chain()  # Blockchain should be valid

    # Manually tamper with the blockchain and check validity
    blockchain.chain[1].data = "Tampered Data"
    assert not blockchain.validate_chain()  # Blockchain should be invalid due to tampering
