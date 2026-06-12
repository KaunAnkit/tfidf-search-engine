from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB connection
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DB_NAME = "search_engine"
COLLECTION_NAME = "documents"

client = None
db = None
collection = None

def init_db():
    global client, db, collection
    
    try:
        client = MongoClient(MONGODB_URL)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]
        
        # Create unique index on url
        collection.create_index("url", unique=True)
        
        print(f"Connected to MongoDB: {DB_NAME}.{COLLECTION_NAME}")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        raise

def url_exists(base_url):
    init_db_if_needed()
    
    try:
        result = collection.find_one({"url": base_url})
        return result is not None
    except Exception as e:
        print(f"Error checking url: {e}")
        return False

def save_document(data):
    init_db_if_needed()
    
    try:
        document = {
            "url": data["url"],
            "title": data["Title"],
            "text": data["Text"],
            "created_at": datetime.utcnow()
        }
        
        collection.insert_one(document)
        return True
    
    except Exception as e:
        # Duplicate url or other error
        return False

def get_all_documents():
    init_db_if_needed()
    
    try:
        documents = collection.find({}, {"_id": 1, "text": 1})
        rows = []
        for doc in documents:
            # Return as (id, text) tuples to match SQLite behavior
            rows.append((str(doc["_id"]), doc["text"]))
        return rows
    except Exception as e:
        print(f"Error getting documents: {e}")
        return []

def get_detail_document(doc_id):
    init_db_if_needed()
    
    try:
        from bson.objectid import ObjectId
        
        doc = collection.find_one({"_id": ObjectId(doc_id)})
        if doc:
            return (doc["title"], doc["url"])
        return None
    except Exception as e:
        print(f"Error getting document detail: {e}")
        return None

def init_db_if_needed():
    global collection
    
    if collection is None:
        init_db()

    
def get_all_titles():
    init_db_if_needed()

    try:

        documents = collection.find(
            {},
            {"title": 1}
        )

        titles = []

        for doc in documents:

            if "title" in doc:
                titles.append(doc["title"])

        return titles

    except Exception as e:
        print(f"Error getting titles: {e}")
        return []

