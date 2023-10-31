import streamlit as st
from PIL import Image
from memory.capture_memory import capture_memory
from memory.view_memory import view_memory
import uuid

query_params = st.experimental_get_query_params()

if 'debug' not in st.session_state:
    st.session_state['debug'] = False
if 'page' not in st.session_state:
    st.session_state['page'] = query_params.get("page", ["capture_memory"])[0]
if 'capture_user' not in st.session_state:
    st.session_state['capture_user'] = str(uuid.uuid4())
if 'capture_session' not in st.session_state:
    st.session_state['capture_session'] = str(uuid.uuid4())
# Neum pipeline only matters at capture. Everything in the DB for view
if "neumai_pipeline" not in st.session_state:
    st.session_state["neumai_pipeline"] = ""
if 'view_user' not in st.session_state:
    st.session_state['view_user'] = query_params.get("user", [""])[0]
if 'view_session' not in st.session_state:
    st.session_state['view_session'] = query_params.get("session", [""])[0]

image = Image.open('./media/R.gif')

with st.sidebar:
    st.markdown("<h1 style='text-align: center'>Pensieve by <a href='neum.ai'>Neum AI</a></h1>", unsafe_allow_html=True)
    st.image(image=image)
    tab1, tab2 = st.tabs(["Home", "About"])

    with tab2:
        st.caption("This application is a showcase for Neum AI Chat Memory. The goal is to leverage Retrieval Augmented Generation (RAG) in the context of chat memory. This helps reduce the amount of context provided back to LLM models and only providing the most contextual information.")

        st.caption("As a side-effect of doing this, it means that conversations are fully indexed making them suitable to be shared with other users. Like Dumbuldore in Harry Potter, share your memories with co-workers or friends from the conversations you have with the Pensieve.")

    with tab1:
        st.markdown("Using the Pensieve is simple:")
        st.markdown("1. Capture a memory\n\n2. Share a memory\n\n3. View a memory")
        if st.button("Capture new memory", use_container_width=True):
            st.session_state['page'] = "capture_memory"
            st.session_state['capture_user'] = str(uuid.uuid4())
            st.session_state['capture_session'] = str(uuid.uuid4())    
        # if st.button("Update memory", use_container_width=True):
        #     st.session_state['page'] = "update_memory"
        if st.button("View memory", use_container_width=True):
            st.session_state['page'] = "view_memory"

        st.divider()
        
        if st.session_state['page'] == "capture_memory":
            st.text_input("User ID", value=st.session_state['capture_user'], disabled=True)
            st.session_state['capture_session'] = st.text_input("Session ID", value=st.session_state['capture_session'], disabled=True)
            # Change value of URL if you want to change the share path
            url = "https://neumai-pensieve.streamlit.app/?user=" + st.session_state['capture_user'] + "&session=" + st.session_state['capture_session'] + "&page=view_memory"
            if st.button('Share memory', use_container_width=True):
                st.code(url)
            st.session_state['debug'] = st.toggle("Debug mode")
        
        if st.session_state['page'] == "view_memory":
            st.session_state['view_user'] = st.text_input("Share User ID", value=st.session_state['view_user'])
            st.session_state['view_session'] = st.text_input("Share Session ID", value=st.session_state['view_session'])
            st.session_state['debug'] = st.toggle("Debug mode")

if st.session_state['page'] == "capture_memory":
    capture_memory()

elif st.session_state['page'] == "view_memory":
    view_memory()
