import streamlit as st
from services.comment import generate_comment
from services.ingestion import ingestion
from services.api import get_patches
from services.github_push import push_comment
from services.review import generate_review
if "pull_url" not in st.session_state:
    st.session_state.pull_url=""
if "review" not in st.session_state:
    st.session_state.review=""
if "comment" not in st.session_state:
    st.session_state.comment=""
if "patch" not in st.session_state:
    st.session_state.patch=""
if "token" not in st.session_state:
    st.session_state.token=""
st.session_state.pull_url=st.text_input("Enter url of pull request")
with st.sidebar:
    st.session_state.token=st.text_input("Enter github token",type="password")
if st.session_state.token:
    if st.session_state.pull_url:
        if st.button("Code Review"):
            with st.spinner("Starting Retrieval...", show_time=True):
                ingestion(st.session_state.pull_url,st.session_state.token)
            with st.spinner("Reviewing Code...", show_time=True):
                st.session_state.review=generate_review()
            with st.spinner("Generating Comment ...", show_time=True):
                    st.session_state.patch=get_patches(st.session_state.pull_url,st.session_state.token)
                    st.session_state.comment=generate_comment(st.session_state.review,st.session_state.patch)
            with st.spinner("Pushing Comment...", show_time=True):
                   push_comment(st.session_state.pull_url,st.session_state.comment,st.session_state.token)
            st.write("Review:\n",st.session_state.review)
    else:
        st.write("Invalid pull request")
else:
    st.write("Please generate valid github token from https://github.com/settings/tokens")                      
