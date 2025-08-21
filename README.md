# SUPPLY CHAIN TRACKER USING BLOCKCHAIN
A simple Python blockchain project for supply chain tracking. Each product step from manufacturer to customer is securely stored in an immutable blockchain using SHA-256, ensuring transparency, authenticity, and tamper-proof records.

# 📌 Overview

This project is a simple blockchain-based Supply Chain Tracker built using Python. It simulates how a product moves across the supply chain (manufacturer → distributor → retailer → customer). Each transaction is securely added to a blockchain using SHA-256 hashing, ensuring immutability, transparency, and trust.

# 🏗 System Architecture

# Block

Stores product information (stage, owner, timestamp).

Each block has its own hash and the previous block’s hash for linkage.

# Blockchain

A chain of blocks ensuring immutability.

Uses SHA-256 for hash generation.

Validates integrity by checking hash links.

# Transactions (Supply Chain Steps)

Each product step (like "Manufactured", "Packed", "Shipped", "Delivered") is recorded as a transaction.

# User Interaction

Currently via Python script (console-based).

Users can add supply chain steps and view the blockchain.

# 🌟 Features

✅ Immutable records – once a step is added, it cannot be altered.

✅ SHA-256 hashing for block integrity.

✅ Transparency – every supply chain step is visible.

✅ Simple, extendable Python implementation – easy to expand into a full project.

# 🔧 Improvements to be Done (Future Scope)

🔹 Add a Web UI / Dashboard for visualization.

🔹 Integrate QR Codes for scanning product info.

🔹 Use Flask/Django API to simulate real-time blockchain transactions.

🔹 IoT Integration (sensors automatically update shipment status).

🔹 Consensus Mechanism (PoW/PoS) for distributed validation.

🔹 Database integration (MongoDB/SQL) for storing blockchain snapshots.

# 💡 Usefulness

Builds customer trust by showing product authenticity.

Helps in detecting counterfeit products.

Provides traceability from production to consumer.

Ensures tamper-proof data for auditing and compliance.

Real-world companies like Walmart, IBM, Maersk already use similar solutions.
