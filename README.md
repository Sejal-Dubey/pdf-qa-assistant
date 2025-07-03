# 📄 Your PDF Q&A Assistant

A fully functional GenAI-powered assistant that answers questions from any PDF document using **LangChain**, **HuggingFace embeddings**, **FAISS**, and **Together AI's LLMs**.

> This project solves a real-world problem: retrieving relevant answers from long documents (e.g., research papers, resumes, legal contracts) — **without relying on OpenAI or paid APIs**.

---

## Features

- Upload any PDF document
- Ask natural language questions about its contents
- Uses **Retrieval-Augmented Generation (RAG)** to provide contextual answers
- Powered by **Mixtral-8x7B** via Together.ai (OpenAI-compatible LLM)
- Embedding done using **sentence-transformers** (local + free)
- Instant feedback UI via **Streamlit**

## Tech Stack

| Component | Tool |
|-----------|------|
| LLM       | Together AI (Mixtral, Hermes, LLaMA2) |
| Embeddings | HuggingFace (`all-MiniLM-L6-v2`) |
| Vector DB | FAISS |
| Framework | LangChain |
| UI        | Streamlit |
| PDF Parsing | LangChain's PyPDFLoader |


## Use Cases

-  Resume/document screening
-  Research paper summarization
-  Legal or compliance document Q&A
-  Building custom chatbots over your own knowledge


##  Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/pdf-qa-assistant.git
cd pdf-qa-assistant
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add API key

Create a `.env` file:

```
TOGETHER_API_KEY=your_together_api_key
```

> [Get a free key from Together.ai](https://www.together.ai)

### 4. Run the app

```bash
streamlit run app.py
```

---
![image](https://github.com/user-attachments/assets/095164ee-09a8-41fb-bbac-062e0b83a8b1)


---

## What I Learned

* Real-world application of **RAG** to reduce hallucinations in LLMs
* How to integrate **free + open-source tools** to avoid rate limits and API lock-in
* Handling common issues like **503 server errors** and **token limits**
* How to design a complete **GenAI product pipeline** — from PDF to answer

---

## Future Improvements

* 🗃️ Support for multiple PDFs
* 🌐 Add URL / website summarizer
* 💾 Save Q\&A chat history per session
* 🔐 Add user auth and document permissions

---


