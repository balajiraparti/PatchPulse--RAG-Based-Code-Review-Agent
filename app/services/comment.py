from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
load_dotenv()
import streamlit as st
from pydantic import BaseModel
class CommentSchema(BaseModel):
     comment:str

def generate_comment(review:str,code:str):
    
    llm = ChatOpenAI(
        model="gpt-5-nano",
        api_key=st.secrets['API_KEY']
    )
    messages =ChatPromptTemplate.from_messages( [
    (
        "system",
        """You are expert github code comment generator. You're task is to generate comment for given github code review. Generate accurate,short and actionable comment.  
{{
  "comment": str
}}

Only return valid JSON.
        """,
    ),
    ("human", "review: {llm_review} code:{code}"),
])
    llm_with_structured_output=messages | llm.with_structured_output(CommentSchema,method="json_mode")
    response= llm_with_structured_output.invoke({"llm_review":review,"code":code})
    return response.comment
    
    