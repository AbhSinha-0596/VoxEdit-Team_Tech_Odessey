import os
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

'''model = SentenceTransformer("all-MiniLM-L6-v2")'''
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    cache_folder="./models"
)

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
    check_compatibility=False
)

COLLECTION = "voice_image_memory"

try:
    client.get_collection(COLLECTION)
except:
    client.create_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE)
    )

def store_mapping(text, commands):
    vec = model.encode(text).tolist()

    client.upsert(
        collection_name=COLLECTION,
        points=[
            PointStruct(
                id=abs(hash(text)) % (10**12),
                vector=vec,
                payload={
                    "text": text,
                    "commands": commands
                }
            )
        ]
    )

def retrieve_similar(text):
    vec = model.encode(text).tolist()

    result = client.query_points(
        collection_name=COLLECTION,
        query=vec,
        limit=1
    ).points

    
    if result and result[0].score >= 0.90:
        payload=result[0].payload
        return payload.get("commands")

    return None