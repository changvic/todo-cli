# Day 1 - Python CLI ToDo List

一個簡單命令列代辦清單工具，支援新增、查詢、標記完成、刪除，資料儲存在本地 json 檔。

## 使用方式

- 新增任務  
  `python3 todo.py add "買牛奶"`
- 查看任務  
  `python3 todo.py list`
- 標記完成  
  `python3 todo.py done 1`
- 刪除任務  
  `python3 todo.py delete 1`

## 範例畫面

vic@iMac todo-cli % python3 todo.py add "買牛奶"
已新增：買牛奶
vic@iMac todo-cli % python3 todo.py list

1. [❌] 買牛奶
   vic@iMac todo-cli % python3 todo.py done 1
   已完成：買牛奶
   vic@iMac todo-cli % python3 todo.py delete 1
   已刪除：買牛奶
   vic@iMac todo-cli % python3 todo.py list
   目前沒有待辦事項！

### 編輯任務

- 編輯內容  
  `python3 todo.py edit 2 "練習刷題"`
- 編輯內容＋到期日  
  `python3 todo.py edit 2 "練習刷題" 2024-07-31`

### 新增任務＋到期日

`python3 todo.py add "報名線上課程" 2024-07-27`

## 範例畫面

vic@iMac todo-cli % python3 todo.py add "寫明天的筆記"
已新增：寫明天的筆記，到期日：無
vic@iMac todo-cli % python3 todo.py add "運動 30 分鐘"
已新增：運動 30 分鐘，到期日：無
vic@iMac todo-cli % python3 todo.py list

1. [❌] 寫明天的筆記（到期日：None）
2. [❌] 運動 30 分鐘（到期日：None）
   vic@iMac todo-cli % python3 todo.py edit 2 "練習刷題"
   已編輯第 2 項目：練習刷題（到期日：無）
   vic@iMac todo-cli % python3 todo.py list
3. [❌] 寫明天的筆記（到期日：None）
4. [❌] 練習刷題（到期日：None）
   vic@iMac todo-cli % python3 todo.py edit 2 "練習刷題" 2025-07-31
   已編輯第 2 項目：練習刷題（到期日：2025-07-31）
   vic@iMac todo-cli % python3 todo.py list
5. [❌] 寫明天的筆記（到期日：None）
6. [❌] 練習刷題（到期日：2025-07-31）
