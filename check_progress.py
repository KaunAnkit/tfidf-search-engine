#!/usr/bin/env python3
"""Check crawler progress"""

import os
from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")

try:
    client = MongoClient(MONGODB_URL, serverSelectionTimeoutMS=5000)
    db = client["search_engine"]
    collection = db["documents"]
    
    # Count total documents
    total_docs = collection.count_documents({})
    
    print(f"📊 CRAWLER PROGRESS")
    print("=" * 50)
    print(f"✅ Total Documents Crawled: {total_docs}")
    
    if total_docs == 0:
        print("\n⏳ Crawler is still starting up or processing...")
    else:
        # Show recent documents
        print(f"\n📝 Last 10 Documents Added:")
        print("-" * 50)
        
        docs = collection.find().sort("created_at", -1).limit(10)
        for i, doc in enumerate(docs, 1):
            title = doc.get('title', 'N/A')[:50]
            url = doc.get('url', 'N/A')[:50]
            created = doc.get('created_at', 'N/A')
            
            print(f"\n{i}. {title}")
            print(f"   URL: {url}")
            print(f"   Added: {created}")
        
        # Show database stats
        print(f"\n" + "=" * 50)
        print(f"📈 Database Size Stats:")
        stats = db.command("collStats", "documents")
        size_mb = stats.get('size', 0) / (1024 * 1024)
        print(f"   Collection Size: {size_mb:.2f} MB")
        print(f"   Average Doc Size: {stats.get('avgObjSize', 0) / 1024:.2f} KB")
    
    client.close()

except Exception as e:
    print(f"❌ Error: {e}")
    print("\nMake sure MongoDB Atlas is accessible and MONGODB_URL is set in .env")
