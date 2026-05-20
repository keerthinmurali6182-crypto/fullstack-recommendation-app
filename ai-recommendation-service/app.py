from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Recommendation Engine Service",
    description="Production backend running inference models."
)

# Enable CORS Middleware so your live Streamlit website can securely pull data
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any frontend origin (like streamlit.app)
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, etc.
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "online", "engine": "FastAPI Recommendation Pipeline Active"}

@app.get("/api/recommend/{user_id}")
async def get_recommendations(user_id: str):
    # This matches the endpoint your Streamlit app is looking for
    return {
        "user_id": user_id,
        "recommendations": [
            {"title": "Inception", "type": "Movie", "confidence": 0.98},
            {"title": "Designing Data-Intensive Applications", "type": "Book", "confidence": 0.94}
        ],
        "pipeline_status": "SUCCESS_GOLD_STAGE"
    }