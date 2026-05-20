import streamlit as st
import requests

# Page Configuration
st.set_page_config(
    page_title="AI Inference & Recommendation Engine", 
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Personal Inference & Recommendation Engine")
st.caption("Real-time data warehouse pipeline analytics interface")

# Category selection pills
category = st.pills("Categories", ["All", "Movies", "Books", "Products"], default="All")

# Text Input for User ID
user_id = st.text_input("Enter User ID to generate custom AI inferences:", "123")

# Put your exact Render Web Service URL here (without a trailing slash)
BACKEND_URL = "https://ai-recommendation-service-d86l.onrender.com"

if st.button("Generate Recommendations", type="primary"):
    with st.spinner("🧠 Querying AI Recommendation Service on Render..."):
        try:
            # Make the network request to the production cloud container
            endpoint = f"{BACKEND_URL}/api/recommend/{user_id}"
            response = requests.get(endpoint, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                st.success("Data synchronized successfully!")
                
                # Layout UI Grid
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("🎬 Featured Recommendation: Inception")
                    st.video("https://www.youtube.com/watch?v=YoHD9XEInc0")
                    st.write("A thief who steals corporate secrets through the use of dream-sharing technology.")
                    
                with col2:
                    st.subheader("📚 Engineering Text: Designing Data-Intensive Applications")
                    st.markdown("**O'Reilly Media — Martin Kleppmann**")
                    st.info("Key engineering architecture text covering storage engines, processing, and system topologies.")
                    
                # Debug output to verify what raw data came back from your model
                with st.expander("🔍 View Raw AI Engine Payload"):
                    st.json(data)
            else:
                st.error(f"❌ Backend returned an error status: {response.status_code}")
                st.info("Check your Render service log streams to see why the router rejected the request.")
                
        except requests.exceptions.Timeout:
            st.error("⏳ Connection Timed Out! Your free Render instance might be sleeping. Give it a minute to spin up and try again.")
        except Exception as e:
            st.error(f"⚠️ Could not connect to backend engine.")
            st.code(f"Error Details: {e}")