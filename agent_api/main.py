from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent_api.k8s import deploy_agent

app = FastAPI(title="AIgentOps Controller")

class AgentConfig(BaseModel):
    name: str
    image: str
    replicas: int = 1
    vector_db: bool = False
    minio: bool = False
    postgres: bool = False

@app.post("/deploy")
def deploy(config: AgentConfig):
    try:
        status = deploy_agent(config)
        return {"status": "success", "details": status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
