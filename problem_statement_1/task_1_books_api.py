import requests
import sqlite3

def fetch_and_store_books():
    """
    Fetches book data from Google Books API,
    stores it in a SQLite database,
    and displays the stored records.
    """

    # Google Books API endpoint
    url = "https://www.googleapis.com/books/v1/volumes?q=python&maxResults=5"

    print(f"Fetching data from {url}...")

    try:
        # User-Agent header to avoid request blocking
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        # Google Books returns book list under "items"
        books = data.get("items", [])

        # Database setup (SQLite)
        conn = sqlite3.connect("problem_statement_1/database_1.db")
        cursor = conn.cursor()

        # Recreate table for fresh data
        cursor.execute("DROP TABLE IF EXISTS books")
        cursor.execute("""
            CREATE TABLE books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                published_year INTEGER
            )
        """)

        print(f"Inserting {len(books)} books into database...")

        # Insert book records
        for book in books:
            volume_info = book.get("volumeInfo", {})

            title = volume_info.get("title", "No Title")

            authors = volume_info.get("authors", ["Unknown"])
            author_str = ", ".join(authors)

            # publishedDate can be "YYYY" or "YYYY-MM-DD"
            published_date = volume_info.get("publishedDate", "0")
            year = int(published_date[:4]) if published_date[:4].isdigit() else 0

            cursor.execute(
                "INSERT INTO books (title, author, published_year) VALUES (?, ?, ?)",
                (title, author_str, year)
            )

        conn.commit()

        # Display stored data
        print("\n--- Stored Books Data ---")
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()

        print(f"{'ID':<5} {'Year':<10} {'Title':<40} {'Author'}")
        print("-" * 80)

        for row in rows:
            bid, title, author, year = row
            display_title = (title[:37] + "...") if len(title) > 37 else title
            print(f"{bid:<5} {year:<10} {display_title:<40} {author}")

        conn.close()
        print("\nSuccess")

    except requests.exceptions.Timeout:
        print("Error: The request timed out. API may be temporarily unavailable.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    fetch_and_store_books()
