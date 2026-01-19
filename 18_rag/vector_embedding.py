from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore


# from qdrant_client import QdrantClient

load_dotenv()
# qdrant_client = QdrantClient(
#     url=os.getenv("QRANT_URL"),
#     api_key=os.getenv("QDRANT_API_KEY"),
# )

# print(qdrant_client.get_collections())

pdf_path = Path(__file__).parent/"The_Courage.pdf"
# file_path = "./example_data/layout-parser-paper.pdf"
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

# print(docs[10])


# split docs into smaller chunks

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=400)
chunks = text_splitter.split_documents(docs)

# print(chunks[10])

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

print("indexing of document done")
