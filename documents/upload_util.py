from supabase import create_client, Client
import os

url: str = "https://auth.neum.ai"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlzaW1oZ2VlcmxrbGFoeXZ3eWxnIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODg2MDEyMTIsImV4cCI6MjAwNDE3NzIxMn0.DQOcTMDA2hdTdvVXYipEdCRGaEKnsSsv0XdxcpiMuk0"
supabase: Client = create_client(url, key)

def uploadFile(file_bytes:bytes, file_name:str, user:str, session:str):
    try:
        path = user + "/" + session + "/" + file_name
        supabase.storage.from_("pensieve").upload(file=file_bytes,path=path)
        return 200
    except Exception as e:
        print("Upload failed. Exception: " + str(e))
        return 400