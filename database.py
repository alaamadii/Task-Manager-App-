import sqlite3
import os

DB_DIR = "data"
DB_PATH = os.path.join(DB_DIR, "tasks.db")

def get_connection():
    """
    Establish and return a connection to the SQLite database.
    Creates the 'data' directory if it doesn't exist.
    """
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)
        

    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row  # to return results as dict-like objects
    return conn

def create_table():
    """
    Create the 'tasks' table if it does not already exist.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        due_date TEXT,
        status TEXT DEFAULT 'Pending'
    )
    '''
    
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

def add_task(title, description, due_date, status):
    """
    Add a new task to the database.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, due_date, status) VALUES (?, ?, ?, ?)",
        (title, description, due_date, status)
    )
    conn.commit()
    conn.close()

def view_all_tasks():
    """
    Retrieve all tasks from the database.
    Returns a list of lists, each representing a task.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    return [list(row) for row in rows]

def update_task(task_id, title, description, due_date, status):
    """
    Update an existing task by its ID.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET title = ?, description = ?, due_date = ?, status = ? WHERE id = ?",
        (title, description, due_date, status, task_id)
    )
    conn.commit()
    conn.close()

def delete_task(task_id):
    """
    Delete a task from the database by its ID.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# Automatically create the table when the module is imported
create_table()
