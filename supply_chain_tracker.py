import hashlib
import time

# 🔹 Block structure
class Block:
    def __init__(self, index, timestamp, product_data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.product_data = product_data  # supply chain details
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.product_data) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()


# 🔹 Blockchain structure
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block - Product Created", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, product_data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), product_data, latest_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True


# 🔹 Demo: Supply Chain Tracking
supply_chain = Blockchain()

# Adding supply chain transactions
supply_chain.add_block("Step 1: Product manufactured at Factory A")
supply_chain.add_block("Step 2: Shipped to Warehouse B")
supply_chain.add_block("Step 3: Delivered to Retail Store C")
supply_chain.add_block("Step 4: Purchased by Customer X")

# Print the blockchain
for block in supply_chain.chain:
    print("Index:", block.index)
    print("Timestamp:", time.ctime(block.timestamp))
    print("Data:", block.product_data)
    print("Hash:", block.hash)
    print("Previous Hash:", block.previous_hash)
    print("-" * 50)

# Validate blockchain
print("Blockchain valid?", supply_chain.is_chain_valid())
