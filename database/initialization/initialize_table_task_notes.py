import sqlite3

def initialize_table_task_notes():

    conn = sqlite3.connect('task_notes.db')
    c = conn.cursor()
    
    # 创建表 task_notes
    c.execute('''
        CREATE TABLE IF NOT EXISTS task_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            changed_on TIMESTAMP      
        )
    ''') 

    conn.commit()
    conn.close()