from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Production AI Recommendation Engine")

# Enable CORS so your live Streamlit website can securely pull data
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route to test if the backend server is live
@app.get("/")
async def read_root():
    return {"status": "online", "message": "FastAPI AI Engine is running perfectly!"}

# The explicit route matching your Streamlit request
@app.get("/api/recommend/{user_id}")
async def get_recommendations(user_id: str):
    return {
        "user_id": user_id,
        "status": "SUCCESS",
        "recommendations": [
            {"title": "Inception", "type": "Movie"},
            {"title": "Designing Data-Intensive Applications", "type": "Book"}
        ]
    }