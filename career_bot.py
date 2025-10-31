import streamlit as st
from openai import OpenAI
import json

# --- Load CV data ---
with open("cv_data.json", "r", encoding="utf-8") as f:
    cv_data = json.load(f)

# --- Initialize OpenAI client (uses system OPENAI_API_KEY) ---
client = OpenAI()

# --- Streamlit page config ---
st.set_page_config(
    page_title="💬 Ghassan Mountassir – Career Chatbot",
    page_icon="💼",
    layout="centered"
)

# --- Header ---
st.title("💬 Career Chatbot – Ghassan Mountassir")
st.markdown(
    """
Welcome to **Ghassan Mountassir’s interactive career assistant**!  
Ask anything about his background, education, or experience 🌍  
Type your question below 👇
    """
)

# --- Input field ---
question = st.text_input("💭 Your question:")

# --- Generate response ---
if question:
    with st.spinner("🤔 Thinking..."):
        context = json.dumps(cv_data, indent=2)
        prompt = f"""You are a chatbot that answers questions about Ghassan Mountassir's background, skills, and experience.
Answer based strictly on the CV information below. You wanna be positive about him, and make him look good and competent.

CV DATA:
{context}

Question: {question}
Answer clearly and professionally in English."""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        answer = response.choices[0].message.content.strip()

    st.markdown(f"💬 {answer}")

# --- Footer ---
st.divider()
st.caption("Made with ❤️ using Streamlit + OpenAI")
