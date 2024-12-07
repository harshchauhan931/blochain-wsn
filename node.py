# from ecc_utils import generate_key_pair, sign_challenge
from node.ecc_utils import generate_key_pair, sign_challenge

# Example usage
private_key, public_key = generate_key_pair()
challenge = "example_challenge"
signature = sign_challenge(private_key, challenge)
