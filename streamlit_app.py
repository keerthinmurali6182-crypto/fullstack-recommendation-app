import streamlit as st
import requests

st.set_page_config(page_title="AI Inference & Recommendation Engine", layout="wide")

st.title("🎬 Personal Inference & Recommendation Engine")
st.caption("Real-time data warehouse pipeline analytics interface")

# Category selection pills
category = st.pills("Categories", ["All", "Movies", "Books", "Products"], default="All")

# Text Input for User ID
user_id = st.text_input("Enter User ID to generate custom AI inferences:", "123")

if st.button("Generate Recommendations", type="primary"):
    with st.spinner("🧠 Querying AI Recommendation Service..."):
        try:
            # Connect directly to your running FastAPI service
            response = requests.get(f"https://ai-recommendation-service-xxxx.onrender.com/api/recommend/{user_id}")
            if response.status_code == 200:
                data = response.json()
                
                # Display recommendations cleanly in a grid
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Inception")
                    st.video("https://www.youtube.com/watch?v=YoHD9XEInc0") # Example placeholder
                with col2:
                    st.subheader("Designing Data-Intensive Applications")
                    st.markdown("*O'Reilly Media — Key Engineering Architecture Text*")
            else:
                st.error("Failed to fetch from AI service.")
        except Exception as e:
            st.error(f"Could not connect to backend engine: {e}")