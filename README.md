# AI Research Assistant — Lightweight RAG with Flan-T5 & FAISS

### Overview
This project demonstrates a lightweight Retrieval-Augmented Generation (RAG) pipeline 
built using open-source models. It uses Hugging Face’s `Flan-T5` for generation and 
`FAISS` for semantic search, allowing local private document querying without APIs.

###  Tech Stack
- **LLM:** Flan-T5 (open-source)
- **Embeddings:** Sentence Transformers (all-MiniLM-L6-v2)
- **Vector DB:** FAISS
- **Framework:** LangChain (for orchestration)
- **Fine-tuning:** LoRA (optional module)

### File Structure: 
```graphql
📦 ai_research_assistant/
│
├── 📁 data/                         
│   ├── sample_1.txt
│   └── sample_2.txt
│
├── 📁 modules/                      
│   ├── ingestion.py                 
│   ├── chunking.py                  
│   ├── embedding_store.py           
│   ├── retriever.py                 
│   ├── generator.py                 
│   └── utils.py                     
├── main.py                          
├── requirements.txt                 
├── README.md                        
└── .gitignore                       
```


###  Modules
- `ingestion.py` — Load and clean raw documents
- `chunking.py` — Split long text into semantic chunks
- `embedding_store.py` — Convert chunks to embeddings and store in FAISS
- `retriever.py` — Retrieve top-k chunks per query
- `generator.py` — Generate context-aware answers with Flan-T5
- `main.py` — Runs the end-to-end RAG pipeline

###  Design Choices
- Chunk size: 500 tokens
- Overlap: 100
- Top-k retrieval: 5
- Embedding model: `all-MiniLM-L6-v2`
- Temperature: 0.2
- Model: `google/flan-t5-base`

### How to run
```bash
pip install -r requirements.txt
python main.py
```
``` 
Upload Your Text Documents into /data/, run the pipeline, and aks the Query!
```