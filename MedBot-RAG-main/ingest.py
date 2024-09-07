from llama_index.core import Settings
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import SimpleDirectoryReader
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

LawDocuments = SimpleDirectoryReader(input_dir='./data').load_data()

splitter = SentenceSplitter(chunk_size=1024)
nodes = splitter.get_nodes_from_documents(LawDocuments)

vectorIndex = VectorStoreIndex(nodes)
vectorIndex.storage_context.persist(persist_dir="./vectorDB")