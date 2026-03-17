import streamlit as st
from services.comment import generate_comment
from services.ingestion import ingestion
from services.api import get_patches
from services.github_push import push_comment
if "pull_url" not in st.session_state:
    st.session_state.pull_url=""
if "review" not in st.session_state:
    st.session_state.review=""
if "comment" not in st.session_state:
    st.session_state.comment=""
if "patch" not in st.session_state:
    st.session_state.patch=""
st.session_state.pull_url=st.text_input("Enter url of pull request")
from services.review import generate_review
if st.session_state.pull_url:
    if st.button("Code Review"):
        with st.spinner("starting ingestion...", show_time=True):
            ingestion(st.session_state.pull_url)
        with st.spinner("reviewing code...", show_time=True):
            st.session_state.review=generate_review()
        with st.spinner("Generating comment ...", show_time=True):
                st.session_state.patch=get_patches(st.session_state.pull_url)
                st.session_state.comment=generate_comment(st.session_state.review,st.session_state.patch)
        with st.spinner("Pushing Comment...", show_time=True):
            push_comment(st.session_state.pull_url,st.session_state.comment)
                      
