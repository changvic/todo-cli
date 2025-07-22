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
        due = todo.get("due_date", "無")
        print(f"{i}. [{status}] {todo['task']}（到期日：{due}）")

def add_todo(task, due_date=None):
    todos = load_todos()
    todos.append({"task": task, "done": False, "due_date": due_date})
    save_todos(todos)
    print(f"已新增：{task}，到期日：{due_date or '無'}")

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

def edit_todo(index, new_task, new_due_date=None):
    todos = load_todos()
    if 0 < index <= len(todos):
        todos[index-1]['task'] = new_task
        if new_due_date is not None:
            todos[index-1]['due_date'] = new_due_date
        save_todos(todos)
        print(f"已編輯第{index}項目：{new_task}（到期日：{new_due_date or '無'}）")
    else:
        print("無此編號")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python todo.py [add/list/done/delete] ...")
    elif sys.argv[1] == "add":
        if len(sys.argv) == 4:  # 有到期日
            add_todo(sys.argv[2], sys.argv[3])
        else:
            add_todo(" ".join(sys.argv[2:]), None)
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
    elif sys.argv[1] == "edit":
        try:
            index = int(sys.argv[2])
            if len(sys.argv) == 5:
                edit_todo(index, sys.argv[3], sys.argv[4])
            else:
                edit_todo(index, sys.argv[3])
        except:
            print("請輸入正確的指令：python3 todo.py edit 編號 '新內容' [新到期日]")
    else:
        print("未知指令")
