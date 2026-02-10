import requests
import json
import os
import sys
from dotenv import load_dotenv


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from storage.storage import get_all_documents, get_detail_document

load_dotenv()

NODE_API_URL = os.getenv("NODE_API_URL")

def send_documents_to_node(documents):

    payload = {
        "documents" : documents
    }

    try: 
        response = requests.post(
            NODE_API_URL,
            json=payload,
            timeout=30
        )
        
        response.raise_for_status()

        print("Bulk upload successful")
        print(response.json())

    except requests.exceptions.RequestException as e:
        print("Failed to send documents")
        print(e)

    
if __name__ == "__main__":
    
    doc_rows = get_all_documents()
    
    if not doc_rows:
        print("No documents found in database. Run the crawler first!")
        sys.exit(1)
    
    
    crawled_documents = []
    for doc_id, text in doc_rows:
        title, url = get_detail_document(doc_id)
        crawled_documents.append({
            "url": url,
            "title": title,
            "text": text
        })
    
    print(f"Sending {len(crawled_documents)} documents to Node API...")
    send_documents_to_node(crawled_documents)