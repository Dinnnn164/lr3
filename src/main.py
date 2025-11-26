from fastapi import FastAPI
from src.core.router import router as common_routes

app = FastAPI(
    title="Lab3 FastAPI Project",
    description="Lab project with FastAPI and Swagger UI",
    version="0.1.0"
)

app.include_router(common_routes)

@app.get("/")
def root():
    return {"status": "ok", "message": "FastAPI is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)