""" This is a basic intro to using llama_index to develop AI applications with azure open AI"""

import os
from dotenv import load_dotenv
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import logging
import sys
from llama_index.core import Settings

# Load environment variables
load_dotenv()

logging.basicConfig(
    stream=sys.stdout, level=logging.INFO
)  # logging.DEBUG for more verbose output
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

api_key = os.environ.get("AZURE_OAI_KEY")
azure_endpoint = os.environ.get("AZURE_OAI_ENDPOINT")
api_version = "2023-09-01-preview"

llm = AzureOpenAI(
    model="gpt-35-turbo-16k",
    deployment_name="gpt-35-turbo-16k",
    api_key=api_key,
    azure_endpoint=azure_endpoint,
    api_version=api_version,
)

# You need to deploy your own embedding model as well as your own chat completion model
embed_model = AzureOpenAIEmbedding(
    model="text-embedding-ada-002",
    deployment_name="text-embedding-ada-002",
    api_key=api_key,
    azure_endpoint=azure_endpoint,
    api_version=api_version,
)

Settings.llm = llm
Settings.embed_model = embed_model

documents = SimpleDirectoryReader(
    input_files=["../data/paul_graham_essay.txt"]
).load_data()
index = VectorStoreIndex.from_documents(documents)

query = "What was done for the undergraduate thesis?"
query_engine = index.as_query_engine()
answer = query_engine.query(query)

print(answer.get_formatted_sources())
print("query was:", query)
print("answer was:", answer)