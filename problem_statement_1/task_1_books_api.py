import requests
import sqlite3
import json

def fetch_and_store_books():
    # 1. Fetch Data (Using OpenLibrary API which is more stable)
    url = "https://openlibrary.org/search.json?q=python&limit=5"
    
    print(f"Fetching data from {url}...")
    
    try:
        response = requests.get(url, timeout=10) 
        response.raise_for_status() 
        
        data = response.json()
        books = data.get('docs', [])
        
        # 2. Database Setup
        conn = sqlite3.connect('problem_statement_1\database.db')
        cursor = conn.cursor()
        
        # Drop table if exists to avoid duplication during testing
        cursor.execute('DROP TABLE IF EXISTS books')
        
        cursor.execute('''
            CREATE TABLE books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                published_year INTEGER
            )
        ''')
        
        # 3. Insert Data
        print(f"Inserting {len(books)} books into database...")
        for book in books:
            # OpenLibrary returns lists for authors, we join them into a string
            authors = ", ".join(book.get('author_name', ['Unknown']))
            title = book.get('title', 'No Title')
            year = book.get('first_publish_year', 0)
            
            cursor.execute("INSERT INTO books (title, author, published_year) VALUES (?, ?, ?)", 
                           (title, authors, year))
        
        conn.commit()
        
        # 4. Display Data
        print("\n--- Stored Books Data ---")
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        
        # Formatting output for better readability
        print(f"{'ID':<5} {'Year':<10} {'Title':<40} {'Author'}")
        print("-" * 80)
        for row in rows:
            # row structure: (id, title, author, year)
            bid, title, author, year = row
            # Truncate long titles for display
            display_title = (title[:37] + '...') if len(title) > 37 else title
            print(f"{bid:<5} {year:<10} {display_title:<40} {author}")
            
        conn.close()
        print("\nSuccess.")

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please check your internet connection.")
    except requests.exceptions.RequestException as e:
        print(f"Error: A network error occurred: {e}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    fetch_and_store_books()