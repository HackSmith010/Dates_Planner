import streamlit as st
from google_search import search_cafes
from ai_engine import generate_card_details

st.set_page_config(page_title="HYPE Date Planner", layout="centered")
st.title("💖 Plan Your Perfect Date")

user_prompt = st.text_input("Enter your dreamy date idea ✨", placeholder="e.g., beachside cafe with strong coffee in Goa under ₹700")

if st.button("Generate Date Ideas") and user_prompt:
    with st.spinner("Fetching magical date spots..."):
        cafe_results = search_cafes(user_prompt)
        cafes_info = cafe_results[:5]  # Limit to 5 to save tokens
        plan = generate_card_details(user_prompt, cafes_info)

    if plan:
        st.success("✨ Your perfect date spots:")
        st.markdown(plan)
    else:
        st.error("Couldn't generate a plan right now. Try again.")
