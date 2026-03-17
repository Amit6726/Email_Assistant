import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # FREE model
    google_api_key='AIzaSyATLKqL9QI55x7_VPNtMJVmv-BFt5_ryWE'
)

def email_assistant(task_type, content):
    if task_type == "generate":
        prompt = f"Write a professional email about: {content}"
    elif task_type == "summarize":
        prompt = f"Summarize this email:\n{content}"
    elif task_type == "reply":
        prompt = f"Write a reply to this email:\n{content}"
    elif task_type == "improve":
        prompt = f"Improve this email professionally:\n{content}"
    else:
        return "Invalid type"

    response = llm.invoke(prompt)
    return response.content