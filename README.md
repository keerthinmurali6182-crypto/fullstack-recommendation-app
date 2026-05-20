# Full-Stack AI Product Recommendation Application (MERN + Python)

This repository serves as a foundational blueprint for a decoupled, full-stack predictive marketplace feed built using an elastic microservices matrix architecture.

## ⚙️ Technical Highlights & Infrastructure
* **AI Engine (Python / FastAPI):** Performs vector matrix calculations, mapping profile records over catalog features using continuous multi-dimensional **Cosine Similarity** equations.
* **Gateway Layer (Node.js / Express):** Manages connection channels, authenticates downstream routes, and abstracts away core data-layer footprints.
* **Viewport Interface (React.js):** Responsive front-end dashboard that updates recommendations dynamically as active user state profile changes are dispatched.

## 🚀 Orchestration Deployment Steps

To run the entire system concurrently on a single machine, open three separate terminal windows and run the following execution blocks:

```bash
# Terminal 1: Spin up the Python AI Service Core
cd ai-recommendation-service
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000 --reload

# Terminal 2: Boot the Gateway Integration Server
cd node-backend
npm install
node server.js

# Terminal 3: Build and run the User Interface Viewport
cd react-frontend
npm install
npm run dev