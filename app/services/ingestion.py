from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter as rs
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
import bs4
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from services.api import get_code_changes
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

from langchain_qdrant import QdrantVectorStore
from langchain_community.document_loaders import WebBaseLoader
load_dotenv()


def ingestion(url:str):
    # for doc in loader.alazy_load():
    #      docs.append(doc)

    # assert len(docs) == 1
    # doc = docs[0]
    # url="https://github.com/balajiraparti/balajiraparti/pull/3"
    url_split=url.split('/')
    OWNER=url_split[3]
    REPO=url_split[4]
    PR_NUMBER=url_split[6]
    # print(url_split)
    commit_url=url+"/commits"
    modification_url=url+"/changes"
    loader=WebBaseLoader(web_path=[modification_url])
    docs = loader.load()
    code_changes=get_code_changes(OWNER,REPO,PR_NUMBER)
    # print(code_changes)
    docs[0].page_content=code_changes
    # print(doc[0].page_content)
    # print(type(doc))


    text_splitter = rs(
        chunk_size=1000,
        chunk_overlap=400
    )
    chunks = text_splitter.split_documents(docs)


    vector_store = QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        url="http://localhost:6333",
        collection_name="review_collection",
        force_recreate=True
    )
