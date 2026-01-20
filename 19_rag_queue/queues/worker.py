from openai import OpenAI
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
os.environ["OBJC_DISABLE_INITIALIZE_FORK_SAFETY"] = "YES"
load_dotenv()


openai_client = OpenAI()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
    # documents=chunks,

    url="http://localhost:6333",
    collection_name="learning_rag2",
    embedding=embedding_model,
)


def process_query(query: str):
    print("Searching Chunks", query)
    search_results = vector_db.similarity_search(query=query)
    context = "\n\n".join(
        f"""
[Page {res.metadata['page']}]
{res.page_content}
""".strip()
        for res in search_results
    )
    SYSTEM_PROMPT = f"""
You are a helpful AI assistant answering questions from a book PDF.

Rules:
- Answer ONLY using the given context
- If the answer is not present, clearly say so
- Mention relevant page numbers
- Be clear, concise, and explanatory

Context:
{context}
"""
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query}
        ]
    )
    print(f"🤖 : {response.choices[0].message.content}")
    return response.choices[0].message.content
