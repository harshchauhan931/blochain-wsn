from base_station.base_station import app  # Flask app for the base station
from blockchain.blockchain import Blockchain
from config.settings import FLASK_PORT, DEBUG_MODE

# Initialize the blockchain
blockchain = Blockchain()

def start_base_station():
    """
    Start the Flask server for the base station.
    """
    print(f"Starting the base station on port {FLASK_PORT}...")
    app.run(port=FLASK_PORT, debug=DEBUG_MODE)

if __name__ == "__main__":
    # Display startup message
    print("=== Blockchain-Enhanced Wireless Sensor Network (WSN) ===")
    print("1. Initializing Blockchain...")
    print(f"   - Genesis block hash: {blockchain.chain[0].hash}")
    print("2. Starting Base Station...")

    # Start the base station
    start_base_station()
