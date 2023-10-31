# Pensieve by Neum AI

![Pensieve GIF](./img/gif.gif)

## What is the Pensieve?

This application is a showcase for Neum AI Chat Memory. The goal is to leverage Retrieval Augmented Generation (RAG) in the context of chat memory. This helps reduce the amount of context provided back to LLM models and only providing the most contextual information. In this application, like in Harry Potter's Pensieve, the user can capture memories in the form of chat history which can then be shared with others for viewing. When viewed, the users can interact through a chat interface with the memory.

### Features
- 🧠 Chat history indexed for fast retrieval.
- 📕 Chat history summarization when memory is searched
- 📄 Memory augmentation with documents. Documents can be uploaded through the UI. Connection to other sources supported through Neum AI.
- 👤 User and session ID tracking. User + Session IDs unlock access to captured memories
- 🔗 Share memories with other users by providing a user and session ID. 

### Comming soon
- 🦾 Augmentation of chat history with categorization
- 🔊🖼 Explorations to augment experience with other mediums including voice and images

## Running it locally

The Pensieve is built using Streamlit, Supabase, Neum AI and Weaviate. Neum AI is used as the orchestration layer to help create the indexes for the chat history and documents. The index itself is hosted on Weaviate, but can we swapped out for any other vector storage supported by Neum AI. The documents uploaded through the app are stored in Supabase. You will need to create a bucket that the app can access through the `anon` key.

To run locally you will need the following API Keys added to a `secrets.toml` file under the `.streamlit` folder.

```
    Supabase_URL = ""
    Supabase_Key = ""
    Supabase_Bucket = ""
    OpenAI_Key = ""
    Weaviate_URL = ""
    Weaviate_Key = ""
    NeumAI_Key = ""
```

Run:

```bash

streamlit run main.py

```