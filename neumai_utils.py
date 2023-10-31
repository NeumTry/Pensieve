import streamlit as st

def createPipeline(user:str, session:str):
    import requests
    pipeline = {
        "source":{
            "source_name":"supabase",
            "metadata": {
                "url":st.secrets["Supabase_URL"],
                "key":st.secrets["Supabase_Key"],
                "bucket":st.secrets["Supabase_Bucket"],
                "folder":user + "/" + session
            }
        },
        "embed":{
            "embed_name":"openai",
            "metadata":{
                "api_key":st.secrets["OpenAI_Key"],
            }
        },
        "sink":{
            "sink_name":"weaviate",
            "metadata":{
                "url":st.secrets["Weaviate_URL"],
                "api_key":st.secrets["Weaviate_Key"],
                "class_name":"User_" + user.replace("-","_") + "_documents"
            }
        },
    }

    url = f"https://api.neum.ai/v1/pipelines"

    # Headers
    headers = {
        "neum-api-key":st.secrets["NeumAI_Key"],
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=pipeline)
    return response.json()['id']

def triggerPipeline(pipeline:str):
    import requests

    url = f"https://api.neum.ai/v1/pipelines/{pipeline}/trigger"

    # Headers
    headers = {
        "neum-api-key":st.secrets["NeumAI_Key"],
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json={ "sync_type": "full" })
