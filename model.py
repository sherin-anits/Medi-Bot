from llama_index.core import StorageContext, load_index_from_storage

from llama_index.core import Settings
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from dotenv import load_dotenv
import os

load_dotenv()


api_key = os.getenv("AZURE_API_KEY")
azure_endpoint = os.getenv("AZURE_ENDPOINT")


if not api_key or not azure_endpoint:
    raise ValueError("API key and endpoint must be set in the .env file")

Settings.llm = AzureOpenAI(
    model="gpt-4-32k",
    deployment_name="gpt4-demetrius",
    api_key=api_key,
    azure_endpoint=azure_endpoint,
    api_version="2023-07-01-preview",
)
Settings.embed_model = AzureOpenAIEmbedding(
    model="text-embedding-ada-002",
    deployment_name="resume-ranking",
    api_key=api_key,
    azure_endpoint=azure_endpoint,
    api_version="2024-02-15-preview",
)


storage_context = StorageContext.from_defaults(persist_dir="./vectorDB")


index = load_index_from_storage(storage_context)

vector_query_engine = index.as_query_engine()

def get_response(question):
    return vector_query_engine.query(question)