import sqlite3
import argparse
from datetime import datetime

DB_NAME = "tasks.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                created_at TEXT,
                completed INTEGER DEFAULT 0
            )
        """)

def add_task(title):
    with connect() as conn:
        conn.execute(
            "INSERT INTO tasks (title, created_at) VALUES (?, ?)",
            (title, datetime.now().isoformat())
        )
    print("✅ Task added")

def list_tasks():
    with connect() as conn:
        tasks = conn.execute("SELECT * FROM tasks").fetchall()

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "✔" if task[3] else "✘"
        print(f"[{task[0]}] {task[1]} ({status})")

def complete_task(task_id):
    with connect() as conn:
        conn.execute(
            "UPDATE tasks SET completed = 1 WHERE id = ?",
            (task_id,)
        )
    print("🎉 Task completed")

def delete_task(task_id):
    with connect() as conn:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    print("🗑 Task deleted")

def main():
    create_table()

    parser = argparse.ArgumentParser(description="CLI Todo App")
    parser.add_argument("--add", help="Add a new task")
    parser.add_argument("--list", action="store_true", help="List tasks")
    parser.add_argument("--done", type=int, help="Mark task as completed")
    parser.add_argument("--delete", type=int, help="Delete a task")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.done:
        complete_task(args.done)
    elif args.delete:
        delete_task(args.delete)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
