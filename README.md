# Enterprise Graph RAG

**Production-ready Graph Retrieval-Augmented Generation** system combining Knowledge Graphs and Vector Search for enterprise use cases.

## Key Features
- Automated entity & relationship extraction
- Hybrid retrieval (Vector similarity + Graph traversal)
- Multi-hop reasoning support
- Scalable architecture (Neo4j + Vector DB)
- FastAPI REST API
- Logging, monitoring & evaluation
- Support for multiple LLMs (OpenAI, Grok, local)

## Architecture
```
Documents → Chunking → Entity Extraction → Knowledge Graph (Neo4j)
                    ↓
               Vector Embeddings
                    ↓
User Query → Hybrid Retriever → Context → LLM → Response
```

## Tech Stack
- **Graph DB**: Neo4j
- **Vector DB**: FAISS / Chroma
- **Framework**: LangChain + LlamaIndex
- **Backend**: FastAPI
- **LLM**: OpenAI / Grok / Ollama

## Installation
```bash
pip install -r requirements.txt

# Start Neo4j (Docker)
docker run --name neo4j-graphrag -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/password -d neo4j:latest
```

## Quick Start
See `examples/` and `src/` folders.