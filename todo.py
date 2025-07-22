import sys
import json
import os

TODO_FILE = 'todo.json'

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w', encoding='utf-8') as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

def list_todos():
    todos = load_todos()
    if not todos:
        print("目前沒有待辦事項！")
    for i, todo in enumerate(todos, 1):
        status = "✔️" if todo["done"] else "❌"
        print(f"{i}. [{status}] {todo['task']}")

def add_todo(task):
    todos = load_todos()
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print(f"已新增：{task}")

def done_todo(index):
    todos = load_todos()
    if 0 < index <= len(todos):
        todos[index-1]["done"] = True
        save_todos(todos)
        print(f"已完成：{todos[index-1]['task']}")
    else:
        print("無此編號")

def delete_todo(index):
    todos = load_todos()
    if 0 < index <= len(todos):
        removed = todos.pop(index-1)
        save_todos(todos)
        print(f"已刪除：{removed['task']}")
    else:
        print("無此編號")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python todo.py [add/list/done/delete] ...")
    elif sys.argv[1] == "add":
        add_todo(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_todos()
    elif sys.argv[1] == "done":
        try:
            done_todo(int(sys.argv[2]))
        except:
            print("請輸入正確的任務編號")
    elif sys.argv[1] == "delete":
        try:
            delete_todo(int(sys.argv[2]))
        except:
            print("請輸入正確的任務編號")
    else:
        print("未知指令")
