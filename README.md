# AI/ML Hiring Assignment - AccuKnox

This repository contains the solutions for the AI/ML Trainee hiring assignment at AccuKnox.

## Candidate Details

**Role:** AI/ML Trainee
**Date:** 11 January 2026

## Project Structure

```text
Hiring-Assignment-2026/
├── complex_code_samples/      # Links to complex code references
├── problem_statement_1/       # Practical Coding Tasks
│   ├── database_1.db          # SQLite DB for Task 1
│   ├── database_2.db          # SQLite DB for Task 3
│   ├── students.csv           # Input data for Task 3
│   ├── task_1_books_api.py    # Script for Books API task
│   ├── task_2_student_viz.ipynb # Notebook for Visualization task
│   └── task_3_csv_import.py   # Script for CSV to DB import
├── problem_statement_2/       # Subjective Questions
│   └── subjective_answers.md  # Answers to theoretical questions
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Setup & Installation

1. **Prerequisites:** Ensure Python 3.8+ is installed.
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Problem Statement 1: Coding Tasks

### Task 1: API Data Retrieval and Storage

Fetches book data from the Google Books API and stores it in `database_1.db`.

**Run:**

```bash
python problem_statement_1/task_1_books_api.py
```

### Task 2: Data Processing and Visualization

Fetches student score data, calculates averages, and generates a bar chart.

**Run:**
Open the notebook in Jupyter:

```bash
jupyter notebook problem_statement_1/task_2_student_viz.ipynb
```

### Task 3: CSV Data Import to Database

Reads `students.csv` and imports user data into `database_2.db`.

**Run:**

```bash
python problem_statement_1/task_3_csv_import.py
```

## Problem Statement 2: Subjective Questions

Answers to the theoretical questions regarding LLMs, Chatbot Architecture, and Vector Databases can be found in:
[problem_statement_2/subjective_answers.md](problem_statement_2/subjective_answers.md)

## Complex Code Samples

Links to the most complex Python and Database code I have written are available in:
[complex_code_samples/references.md](complex_code_samples/references.md)
