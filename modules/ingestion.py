"""
This is the functionality of this particular file;
Module: ingestion.py
Purpose: Load and clean raw documents from the data folder.
"""

import os

def load_documents(data_path="./data"):
    docs = []
    for file in os.listdir(data_path):
        if file.endswith(".txt"):
            with open(os.path.join(data_path, file), "r", encoding="utf-8") as f:
                text = f.read().strip()
                docs.append(text)
    print(f"[INFO] Loaded {len(docs)} documents from {data_path}")
    return docs
