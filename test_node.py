import pytest
from node.ecc_utils import generate_key_pair, sign_challenge, serialize_public_key
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

# Test key generation
def test_generate_key_pair():
    private_key, public_key = generate_key_pair()
    assert private_key is not None
    assert public_key is not None
    assert isinstance(private_key, ec.PrivateKey)
    assert isinstance(public_key, ec.PublicKey)

# Test signature creation and verification
def test_sign_challenge():
    private_key, public_key = generate_key_pair()
    challenge = "test_challenge"
    signature = sign_challenge(private_key, challenge)

    # Verify that the signature is valid
    public_key.verify(signature, challenge.encode(), ec.ECDSA(hashes.SHA256()))

# Test public key serialization
def test_serialize_public_key():
    private_key, public_key = generate_key_pair()
    serialized_key = serialize_public_key(public_key)
    assert isinstance(serialized_key, bytes)
    assert serialized_key.startswith(b"-----BEGIN PUBLIC KEY-----")  # Check for PEM format header
