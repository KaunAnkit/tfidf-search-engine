import sqlite3
from datetime import datetime

def init_db():

    conn  = sqlite3.connect("data/search_engine.db")

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents(
                id INTEGER PRIMARY KEY,
                url TEXT UNIQUE,
                title TEXT,
                text TEXT,
                created_at TIMESTAMP
                )


    ''')

    conn.commit()

    conn.close()


def url_exists(base_url):

    conn  = sqlite3.connect("data/search_engine.db")

    cursor = conn.cursor()

    cursor.execute('SELECT 1 FROM documents WHERE url = ?', (base_url,))

    result = cursor.fetchone()
    
    conn.close()

    if result != None:
        return True
    else:
        return False

    

def save_document(data):
    conn = sqlite3.connect("data/search_engine.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            'INSERT INTO documents (url,title,text,created_at) VALUES (?, ?, ?, ?)',
            (
                data["url"],
                data["Title"],
                data["Text"],
                datetime.utcnow().isoformat()
            )
        )
        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()

def get_all_documents():

    conn = sqlite3.connect("data/search_engine.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id,text FROM documents  ")

    rows = cursor.fetchall()
    
    conn.close()

    return rows


def get_detail_document(doc_id):
    conn = sqlite3.connect("data/search_engine.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT title, url FROM documents WHERE id = ?",
        (doc_id,)
    )

    row = cursor.fetchone()  
    conn.close()

    return row

    

