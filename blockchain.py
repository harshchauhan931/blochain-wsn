from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.difficulty = 4
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0")
        self.chain.append(genesis_block)

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), data, previous_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def get_chain(self):
        return [block.__dict__ for block in self.chain]
