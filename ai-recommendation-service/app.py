from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Production AI Recommendation Engine")

# Configure CORS so your Streamlit site isn't blocked by the browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route 1: Root status check
@app.get("/")
async def read_root():
    return {"status": "online", "message": "FastAPI AI Engine is running perfectly!"}

# Route 2: Primary route matching your exact Streamlit URL path
@app.get("/api/recommend/{user_id}")
async def get_recommend_v1(user_id: str):
    return {
        "user_id": user_id,
        "status": "SUCCESS",
        "recommendations": [
            {"title": "Inception", "type": "Movie"},
            {"title": "Designing Data-Intensive Applications", "type": "Book"}
        ]
    }

# Route 3: Fallback route in case the router strips the '/api' prefix
@app.get("/recommend/{user_id}")
async def get_recommend_v2(user_id: str):
    return {
        "user_id": user_id,
        "status": "SUCCESS_FALLBACK",
        "recommendations": [
            {"title": "Inception", "type": "Movie"},
            {"title": "Designing Data-Intensive Applications", "type": "Book"}
        ]
    }