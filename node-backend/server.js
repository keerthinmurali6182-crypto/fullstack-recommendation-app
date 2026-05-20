import express from 'express';
import cors from 'cors';

const app = express();
const PORT = 5001;

app.use(cors({ origin: '*' }));
app.use(express.json());

const recommendationsData = [
  { 
    "id": 1,
    "title": "Inception", 
    "category": "Movie", 
    "description": "A thief steals corporate secrets through use of dream-sharing technology.", 
    "score": 0.95 
  },
  { 
    "id": 2,
    "title": "Designing Data-Intensive Applications", 
    "category": "Book", 
    "description": "A deep-dive into system architectures, processing engines, and storage patterns.", 
    "score": 0.89 
  },
  {
    "id": 3,
    "title": "Sony WH-1000XM5 Headphones",
    "category": "Product",
    "description": "Industry-leading wireless noise-canceling headphones with exceptional audio purity.",
    "score": 0.92
  }
];

// Explicit data route
app.get('/api/recommendations', (req, res) => {
  console.log('📥 Frontend requested data pipeline metrics...');
  res.json(recommendationsData);
});

// Simple server health check
app.get('/', (req, res) => {
  res.send('Backend Server Status: ACTIVE on Port 5001');
});

app.listen(PORT, () => {
  console.log(`🚀 Backend active on http://localhost:5001`);
});