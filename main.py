"""
Main entry point: Runs the end-to-end RAG pipeline.
Connects all the dots of the Project: 
"""

from modules.ingestion import load_documents
from modules.chunking import chunk_documents
from modules.embedding_store import create_faiss_index
from modules.retriever import get_relevant_chunks
from modules.generator import FlanT5Generator
from modules.utils import pretty_print

def run_rag_pipeline():
    # 1. Load data
    docs = load_documents("./data")

    # 2. Split into chunks
    chunks = chunk_documents(docs)

    # 3. Create FAISS DB
    vector_db = create_faiss_index(chunks)

    # 4. Query phase
    query = input("Enter your query: ")
    context = get_relevant_chunks(query)

    # 5. Generate answer
    generator = FlanT5Generator()
    answer = generator.generate_answer(query, context)

    # 6. Show result
    pretty_print("Final Answer:", answer)

if __name__ == "__main__":
    run_rag_pipeline()
