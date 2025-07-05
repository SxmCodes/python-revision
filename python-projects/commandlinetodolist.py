import sqlite3
# connecting to a database. 
conn = sqlite3.connect('todo_list.db')
# creatinig a cursor object using the cursor() method
cursor = conn.cursor()

# Creating a table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY AUTOINCREMENT,
task TEXT NOT NULL,
due_date TEXT,
status TEXT DEFAULT 'pending'
)               
''')

conn.commit()  # Commit the changes to the database

# Individual statements (operations)
def add(task, todo_list):
    todo_list.append(task)
    print(f"Task {task} has been added.")

def remove(task, todo_list):
    cursor.execute("DELETE FROM tasks WHERE task = ?", (task,))
    conn.commit()  # Commit the changes to the database
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task {task} has been removed.")
    else:
        print(f"Task {task} was not found in the list. Cannot remove.")

def list_tasks(todo_list):
    if todo_list:
        print("Current tasks:")
        for task in todo_list:
            print(f"{task}")
    else:
        print("No tasks in the list. You are done for the day!")

def markasdone(task, todo_list):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task {task} has been marked as done.")
    else:
        print(f"Task {task} was not found in the list.")

def sortingtasks(todo_list):
    todo_list.sort()
    print("Tasks have been sorted alphabetically.")

def addduedates(task, due_date, todo_list):
    if task in todo_list:
        print(f"Due date for {task} is set to {due_date}.")
    else:
        print(f"Task {task} was not found in the list. Cannot set due date.")

def listingtasks(todo_list):
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    if rows:
        print("Current tasks in the database:")
        for row in rows:
            print(f"ID: {row[0]}, Task: {row[1]}, Due Date: {row[2]}, Status: {row[3]}")
    else:
        print("No tasks found in the database.")

# Main function, which will be called when the script is run
def main():
    todo_list = []
    while True:
        print("Welcome to this shitty calculator!")
        print("You are dumb, now you will choose any option!")
        print("1 for add, 2 for remove, 3 for list")

        userinput = int(input("Enter the input (1,2,3) - "))
        if userinput == 1:
            task = input("Enter the task to add: ")
            add(task, todo_list)
        elif userinput == 2:
            task = input("Enter the task to remove: ")
            remove(task, todo_list)
        elif userinput == 3:
            list_tasks(todo_list)
        elif userinput == 4:
            task = input("Enter the task to mark as done: ")
            markasdone(task, todo_list)
        elif userinput == 5:
            sortingtasks(todo_list)
        elif userinput == 6:
            task = input("Enter the task to add due date: ")
            due_date = input("Enter the due date (YYYY-MM-DD): ")
            addduedates(task, due_date, todo_list)
        else:
            print("Invalid option. Please try again.")
        cont = input("Do you want to continue? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Exiting the program. Goodbye!")
            break   
if __name__ == "__main__":
    main()
# This is the entry point of the script, which will call the main function when the script is run.
# It allows the script to be imported without executing the main function immediately.
# This is useful for testing or when the script is used as a module in another program.
conn.close()  # Close the database connection when done
