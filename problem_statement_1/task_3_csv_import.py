import sqlite3
import csv
import os

def import_csv_to_db():
    csv_file = 'problem_statement_1\students.csv'
    db_file = 'problem_statement_1\database_2.db'

    # Checking if CSV exists 
    if not os.path.exists(csv_file):
        print(f"Error: '{csv_file}' not found in the current directory.")
        return

    try:
        # Connect to SQLite Database 
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Create Table
        cursor.execute('DROP TABLE IF EXISTS students')
        cursor.execute('''
            CREATE TABLE students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                graduation_year INTEGER
            )
        ''')

        # Read CSV and Insert Data
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            row_count = 0
            for row in reader:
                cursor.execute('''
                    INSERT INTO students (name, email, graduation_year)
                    VALUES (?, ?, ?)
                ''', (row['name'], row['email'], row['graduation_year']))
                row_count += 1

        # Commit changes
        conn.commit()
        print(f"Successfully inserted {row_count} records into '{db_file}'.")

        # Verify Data 
        print("\n--- Verifying Data in Database ---")
        cursor.execute("SELECT * FROM students")
        fetched_rows = cursor.fetchall()
        
        for row in fetched_rows:
            print(row)

        conn.close()

    except sqlite3.Error as e:
        print(f"Database Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import_csv_to_db()