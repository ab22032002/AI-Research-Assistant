"""
Module: embedding_store.py
Purpose: Create embeddings and store them in FAISS vector DB.
"""

from sentence_transformers import SentenceTransformer
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def create_faiss_index(chunks, db_path="./faiss_index"):
    print("[INFO] Generating embeddings using all-MiniLM-L6-v2 ...")
    embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = FAISS.from_texts(chunks, embedding=embedder)
    vector_db.save_local(db_path)
    print(f"[INFO] FAISS index saved at {db_path}")
    return vector_db
