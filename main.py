from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "chanchobi AI server running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
