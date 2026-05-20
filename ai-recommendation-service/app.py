from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = FastAPI(title="Recommendation Engine Pipeline")

# Enable Cross-Origin Resource Sharing (CORS) for Node backend routing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock Item Catalog Matrix: [Tech, Fashion, Home] Profile dimensions
item_catalog = [
    {"item_id": "item_101", "title": "Wireless Mechanical Keyboard", "features": [0.9, 0.1, 0.0]},
    {"item_id": "item_102", "title": "Ergonomic Office Chair", "features": [0.7, 0.2, 0.9]},
    {"item_id": "item_103", "title": "Minimalist Leather Wallet", "features": [0.0, 0.9, 0.1]},
    {"item_id": "item_104", "title": "Smart Home LED Strip Light", "features": [0.8, 0.0, 0.7]},
]

# Historical user interaction matrix matching profile biases
user_history = {
    "user_A": [0.8, 0.1, 0.3], # Prefers tech and home items
    "user_B": [0.1, 0.8, 0.2]  # Prefers fashion items
}

@get("/api/recommend/{user_id}")
def generate_recommendations(user_id: str):
    # Fallback profiling vector if user doesn't exist
    user_vector = np.array(user_history.get(user_id, [0.5, 0.5, 0.5])).reshape(1, -1)
    
    scored_recommendations = []
    
    for item in item_catalog:
        item_vector = np.array(item["features"]).reshape(1, -1)
        # Compute dynamic matching score (Cosine Similarity)
        similarity_score = float(cosine_similarity(user_vector, item_vector)[0][0])
        
        scored_recommendations.append({
            "item_id": item["item_id"],
            "title": item["title"],
            "score": round(similarity_score, 4)
        })
        
    # Sort from highest relevance score down to lowest
    scored_recommendations.sort(key=lambda x: x["score"], reverse=True)
    return scored_recommendations