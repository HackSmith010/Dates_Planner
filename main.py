import streamlit as st
from google_search import search_cafes
from ai_engine import generate_card_details

st.set_page_config(page_title="HYPE Date Planner", layout="centered")
st.title("💖 Plan Your Perfect Date")

user_prompt = st.text_input("Enter your dreamy date idea ✨", placeholder="e.g., beachside cafe with strong coffee in Goa under ₹700")

if st.button("Generate Date Ideas") and user_prompt:
    with st.spinner("Fetching magical date spots..."):
        try:
            raw_results = search_cafes(user_prompt)

            # Simplify and normalize the cafe info
            cafes_info = []
            for r in raw_results[:5]:
                cafes_info.append({
                    "name": r.get("title", "Unknown"),
                    "address": r.get("snippet", "No details"),
                    "price": "₹N/A",
                    "link": r.get("link", "#"),
                    "image": r.get("pagemap", {}).get("cse_image", [{}])[0].get("src", "")
                })

            # Step 1: Generate AI plan
            ai_response = generate_card_details(user_prompt, cafes_info)

            # Step 3: Show raw plan too (optional)
            st.subheader("💌 Full Date Plan (AI Generated)")
            st.markdown(ai_response)

        except Exception as e:
            st.error(f"An error occurred: {e}")
