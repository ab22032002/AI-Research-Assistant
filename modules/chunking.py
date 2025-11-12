"""
Thisis how this file contributes;
Module: chunking.py
Purpose: Split large text documents into manageable chunks for embedding.
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_documents(docs, chunk_size=500, overlap=100):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    chunks = []
    for doc in docs:
        chunks.extend(splitter.split_text(doc))
    print(f"[INFO] Created {len(chunks)} chunks from {len(docs)} documents")
    return chunks
