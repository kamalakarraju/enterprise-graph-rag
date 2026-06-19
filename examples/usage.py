from src.graph_rag import EnterpriseGraphRAG

# Example documents
sample_docs = [
    "Enterprise Graph RAG combines knowledge graphs with vector search for better reasoning.",
    "Neo4j is the leading graph database for enterprise applications."
]

rag = EnterpriseGraphRAG()
rag.build_knowledge_graph(sample_docs)

result = rag.query("What is Graph RAG?")
print(result)