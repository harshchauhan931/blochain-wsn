# General Settings
FLASK_PORT = 5000  # Port for the Flask server
DEBUG_MODE = True  # Debug mode for development

# Blockchain Settings
DIFFICULTY = 4  # Mining difficulty (number of leading zeros in hash)
BLOCK_CREATION_INTERVAL = 30  # Expected block creation time in seconds

# Node Settings
MAX_NODES = 100  # Maximum number of nodes in the network

# Security Settings
ECC_CURVE = "SECP256R1"  # ECC curve to use
JWT_SECRET = "your-secure-key"  # Secret key for token generation
JWT_EXPIRATION = 3600  # Token expiration time in seconds
