"""
Module: retriever.py
Purpose: Retrieve top-k relevant chunks from FAISS based on query similarity.
"""

from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def get_relevant_chunks(query, db_path="./faiss_index", top_k=5):
    embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = FAISS.load_local(db_path, embeddings=embedder, allow_dangerous_deserialization=True)
    results = vector_db.similarity_search(query, k=top_k)
    context = "\n".join([r.page_content for r in results])
    print(f"[INFO] Retrieved {len(results)} relevant chunks for query: {query}")
    return context
