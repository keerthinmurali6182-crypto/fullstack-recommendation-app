import React, { useEffect, useState } from 'react';

function App() {
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filter, setFilter] = useState('All');

  useEffect(() => {
    // Calling the exact proxied API route
    fetch('/api/recommendations')
      .then((res) => {
        if (!res.ok) {
          throw new Error(`Server status error: ${res.status}`);
        }
        return res.json();
      })
      .then((data) => {
        console.log("📥 Dashboard received clean data payload:", data);
        setRecommendations(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error('API Error:', err);
        setError('Could not connect to the recommendation engine backend.');
        setLoading(false);
      });
  }, []);

  const filteredItems = filter === 'All' 
    ? recommendations 
    : recommendations.filter(item => item.category === filter);

  return (
    <div style={styles.container}>
      <header style={styles.header}>
        <h1 style={styles.title}>🎬 Personal Inference & Recommendation Engine</h1>
        <p style={styles.subtitle}>Real-time data warehouse pipeline analytics interface</p>
      </header>

      <div style={styles.tabContainer}>
        {['All', 'Movie', 'Book', 'Product'].map((category) => (
          <button
            key={category}
            onClick={() => setFilter(category)}
            style={{
              ...styles.tabButton,
              backgroundColor: filter === category ? '#007bff' : '#f8f9fa',
              color: filter === category ? '#ffffff' : '#333333',
            }}
          >
            {category === 'All' ? 'All' : `${category}s`}
          </button>
        ))}
      </div>

      {loading && <div style={styles.statusText}>🔄 Streaming metrics and predictions...</div>}
      {error && <div style={{ ...styles.statusText, color: '#dc3545' }}>❌ {error}</div>}

      {!loading && !error && (
        <div style={styles.grid}>
          {filteredItems.map((item) => (
            <div key={item.id} style={styles.card}>
              <span style={styles.badge}>{item.category}</span>
              <h3 style={styles.cardTitle}>{item.title}</h3>
              <p style={styles.cardDescription}>{item.description}</p>
              {item.score && (
                <div style={styles.scoreContainer}>
                  <span style={styles.scoreLabel}>Match Confidence:</span>
                  <strong style={styles.scoreValue}>{(item.score * 100).toFixed(0)}%</strong>
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

const styles = {
  container: { maxWidth: '1200px', margin: '0 auto', padding: '40px 20px', fontFamily: 'system-ui, sans-serif' },
  header: { textAlign: 'center', marginBottom: '40px' },
  title: { fontSize: '2.3rem', color: '#1a1a1a', margin: '0 0 10px 0', fontWeight: '700' },
  subtitle: { fontSize: '1.1rem', color: '#666', margin: 0 },
  tabContainer: { display: 'flex', justifyContent: 'center', gap: '10px', marginBottom: '30px' },
  tabButton: { padding: '10px 20px', border: '1px solid #ddd', borderRadius: '20px', cursor: 'pointer', fontWeight: '600' },
  grid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '20px' },
  card: { backgroundColor: '#ffffff', padding: '24px', borderRadius: '12px', boxShadow: '0 4px 12px rgba(0,0,0,0.08)', border: '1px solid #eef2f5', position: 'relative', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' },
  badge: { position: 'absolute', top: '15px', right: '15px', backgroundColor: '#e3f2fd', color: '#0d47a1', padding: '4px 10px', borderRadius: '12px', fontSize: '0.75rem', fontWeight: 'bold' },
  cardTitle: { fontSize: '1.25rem', color: '#222', margin: '10px 0 8px 0' },
  cardDescription: { color: '#555', fontSize: '0.95rem', lineHeight: '1.5', marginBottom: '20px' },
  scoreContainer: { display: 'flex', alignItems: 'center', borderTop: '1px solid #f0f0f0', paddingTop: '12px', fontSize: '0.9rem' },
  scoreLabel: { color: '#888', flexGrow: 1 },
  scoreValue: { color: '#28a745', fontWeight: '700' },
  statusText: { textAlign: 'center', fontSize: '1.2rem', marginTop: '50px' }
};

export default App;