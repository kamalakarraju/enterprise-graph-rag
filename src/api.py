from fastapi import FastAPI
from pydantic import BaseModel
from src.graph_rag import EnterpriseGraphRAG

app = FastAPI(title="Enterprise Graph RAG API")
rag = EnterpriseGraphRAG()

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query(request: QueryRequest):
    response = rag.query(request.question)
    return {"answer": response, "status": "success"}

@app.post("/build-graph")
async def build_graph(docs: list):
    rag.build_knowledge_graph(docs)
    return {"status": "Graph built successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)