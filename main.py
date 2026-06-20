from fastapi import FastAPI

app = FastAPI()

# =========================
# ROOT
# =========================
@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "chanchobi AI server running"
    }

# =========================
# HEALTH CHECK
# =========================
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

# =========================
# MAIN RUN (Render 안정용)
# =========================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
