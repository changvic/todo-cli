# Day 1 - Python CLI ToDo List

一個簡單命令列代辦清單工具，支援新增、查詢、標記完成、刪除，資料儲存在本地 json 檔。

## 使用方式

- 新增任務  
  `python todo.py add "買牛奶"`
- 查看任務  
  `python todo.py list`
- 標記完成  
  `python todo.py done 1`
- 刪除任務  
  `python todo.py delete 1`

## 範例畫面

已新增：寫明天的筆記
已新增：運動 30 分鐘

1. [❌] 寫明天的筆記
2. [❌] 運動 30 分鐘
   已完成：寫明天的筆記
3. [✔️] 寫明天的筆記
4. [❌] 運動 30 分鐘
   已刪除：運動 30 分鐘
5. [✔️] 寫明天的筆記
