import streamlit as st
from utils import load_and_index_pdf
from qa_chain import get_qa_chain
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="PDF Q&A Assistant", page_icon="📄")
st.title("📄 Your PDF Q&A Assistant")

# Initialize session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Upload PDF
uploaded_file = st.file_uploader("📤 Upload a PDF file", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ PDF uploaded successfully. You can now ask questions!")

    vectorstore = load_and_index_pdf("temp.pdf")
    chain = get_qa_chain(vectorstore)

    query = st.text_input("🔎 Ask something about the PDF:")

    if query:
        with st.spinner("💡 Thinking..."):
            answer = chain.run(query)

        # Store Q&A in session
        st.session_state.history.append((query, answer))

        # Display answer
        st.markdown("### 💬 **Answer:**")
        st.write(answer)

# Optional: Show past Q&A
if st.session_state.history:
    with st.expander("📚 Previous Questions"):
        for i, (q, a) in enumerate(reversed(st.session_state.history), 1):
            st.markdown(f"**{i}. Q:** {q}")
            st.markdown(f"👉 **A:** {a}")
