from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
load_dotenv()


embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

def generate_review():
    userquery="Extract code changes from given github pull request"
    vector_db=QdrantVectorStore.from_existing_collection(
        url="http://localhost:6333",
        collection_name="review_collection",
        embedding=embeddings,
    )
    search_result=vector_db.similarity_search(query=userquery)
    context="\n\n\n".join([f"Page Content:{result.page_content}\nFile Location:{result.metadata['source']}" for result in search_result])
    system_prompt=f"""You are expert code review agent who reviews code changes in github pull request and provide clear and actionable feedback  
    focus on identifying:
    - bug and logical errors
    - security vulnerabilities
    - potential edge cases
    classify each issue using severity levels:
    - High
    - Medium
    - Low
    if changed code is good and no problems were detected then respond with:
    No major issues detected and the reason behind.
    Context:
    {context}
    """
    print(context)
    model = ChatOpenAI(
        model="gpt-5-nano",
        api_key=st.secrets['API_KEY']
    )
    messages = [
        ("system", system_prompt),
        ("human", userquery),
    ]
    response=model.invoke(messages)
    return response.content