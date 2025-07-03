from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import os

def get_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever()

    llm = ChatOpenAI(
        temperature=0.3,
        model_name="NousResearch/Nous-Hermes-2-Mistral-7B-DPO",
        openai_api_key=os.getenv("TOGETHER_API_KEY"),
        openai_api_base="https://api.together.xyz/v1"
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )
    return chain
