#!/usr/bin/env python
"""Test script to verify LangSmith tracing is working"""
import os
from dotenv import load_dotenv
load_dotenv()

print("=" * 60)
print("LangSmith Tracing Test")
print("=" * 60)

# Display environment variables
print(f"\nLANGSMITH_TRACING: {os.getenv('LANGSMITH_TRACING')}")
print(f"LANGSMITH_PROJECT: {os.getenv('LANGSMITH_PROJECT')}")
print(f"LANGSMITH_ENDPOINT: {os.getenv('LANGSMITH_ENDPOINT')}")
print(f"LANGSMITH_API_KEY: {os.getenv('LANGSMITH_API_KEY')[:30]}...")

print("\n" + "=" * 60)
print("Making a test LangChain call...")
print("=" * 60 + "\n")

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Create LLM with explicit tracing
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Make a simple call - this should be traced
response = llm.invoke([HumanMessage(content="Say 'Hello from LangSmith test!'")])

print(f"Response: {response.content}")
print("\n" + "=" * 60)
print("✅ Test complete!")
print("Check LangSmith dashboard at: https://smith.langchain.com/")
print(f"Project: {os.getenv('LANGSMITH_PROJECT')}")
print("=" * 60)
