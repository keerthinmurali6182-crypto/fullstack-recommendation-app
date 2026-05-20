import streamlit as st
import requests

st.set_page_config(page_title="AI Inference & Recommendation Engine", layout="wide")

st.title("🎬 Personal Inference & Recommendation Engine")
st.caption("Real-time data warehouse pipeline analytics interface")

category = st.pills("Categories", ["All", "Movies", "Books", "Products"], default="All")
user_id = st.text_input("Enter User ID to generate custom AI inferences:", "123")

# Target Render domain string
BACKEND_URL = "https://ai-recommendation-service-d86l.onrender.com"

if st.button("Generate Recommendations", type="primary"):
    with st.spinner("🧠 Querying AI Recommendation Service on Render..."):
        try:
            # Attempt 1: Standard routing path
            endpoint = f"{BACKEND_URL}/api/recommend/{user_id}"
            response = requests.get(endpoint, timeout=12)
            
            # Attempt 2: Fallback path if Attempt 1 returns a 404
            if response.status_code == 404:
                endpoint = f"{BACKEND_URL}/recommend/{user_id}"
                response = requests.get(endpoint, timeout=12)
            
            if response.status_code == 200:
                data = response.json()
                st.success("Data synchronized successfully!")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("🎬 Featured Recommendation: Inception")
                    st.video("https://www.youtube.com/watch?v=YoHD9XEInc0")
                with col2:
                    st.subheader("📚 Engineering Text: Designing Data-Intensive Applications")
                    st.markdown("**O'Reilly Media — Martin Kleppmann**")
                
                with st.expander("🔍 View Raw AI Engine Payload"):
                    st.json(data)
            else:
                st.error(f"❌ Backend returned an error status: {response.status_code}")
                st.info(f"Attempted Endpoint call: {endpoint}")
                
        except Exception as e:
            st.error(f"⚠️ Could not connect to backend engine: {e}")