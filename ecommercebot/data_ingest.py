import os
from dotenv import load_dotenv
from langchain_astradb import AstraDBVectorStore
from ecommercebot.data_converter import dataConverter
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
## AstraDB
ASTRADB_API_ENDPOINT = os.getenv('ASTRADB_API_ENDPOINT')
ASTRADB_APPLICATION_TOKEN = os.getenv('ASTRADB_APPLICATION_TOKEN')
ASTRADB_NAMESPACE = os.getenv('ASTRADB_NAMESPACE')
ASTRADB_NAMESPACE = os.getenv('ASTRADB_NAMESPACE')

os.environ["TOKENIZERS_PARALLELISM"] = "false"

embeddings = HuggingFaceEmbeddings()

def ingestData(status):
    vectorStore = AstraDBVectorStore(
        embedding=embeddings,
        collection_name="ecommercechatbot",
        api_endpoint=ASTRADB_API_ENDPOINT, 
        token=ASTRADB_APPLICATION_TOKEN,
        namespace=ASTRADB_NAMESPACE
    )
    if status == None:
        docs = dataConverter()
        inserted_ids = vectorStore.add_documents(docs)
    else:
        return vectorStore
    return vectorStore, inserted_ids 


if __name__ == "__main__":
    # vectorStore, inserted_ids = ingestData(None)
    status = 'done'
    if status == None: 
        vectorStore, inserted_ids = ingestData(None)
        print(f"\n Inserted {len(inserted_ids)} documents")
    else: 
        vectorStore = ingestData("done")

    results = vectorStore.similarity_search("can you tell me the low budget sound basshead.")
    for res in results:
        print(f"* {res.page_content} [{res.metadata}]")