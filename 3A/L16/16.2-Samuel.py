import sqlite3
from turtle import up  # 导入数据库引擎包

db_file = "taskDB.db"  # 数据库文件名

def connect_db(db_file):
    """ 创建数据库连接 """
    conn = None  # 数据库连接
    try:
        conn = sqlite3.connect(db_file)  
        # 如果数据库不存在则创建文件
        print(f"数据库{db_file}创建成功!")
    except sqlite3.Error as e:
        print(e)
    return conn
 
def create_table(conn):
    """ 创建表 """
    conn.execute("""
        CREATE TABLE Task (
        TASK_ID INTEGER PRIMARY KEY NOT NULL ,
        NAME, 
        MEMO)
    """)
    print("TASK表创建成功!")

def insert_data(conn):
    cur = conn.cursor()
    sql = "INSERT INTO Task (TASK_ID, NAME, MEMO) VALUES (?,?,?)"
    data = (1, '阅读「2021」', '10分钟')
    cur.execute(sql, data)
    data = (2, '阅读「200」', '10分钟')
    cur.execute(sql, data)
    data = (3, '阅读「2331」', '10分钟')
    cur.execute(sql, data)

    conn.commit()      
    cur.close()

def update_data(conn):
    cur = conn.cursor()
    sql = "UPDATE TASK SET NAME='慢跑20分钟' WHERE TASK_ID=2"
    cur.execute(sql)
    conn.commit()      
    cur.close()


def delete_data(conn):
    cur = conn.cursor()
    sql = "DELETE FROM TASK WHERE TASK_ID=3"
    cur.execute(sql)
    conn.commit()      
    cur.close()

def close_db(conn): 
    """ 关闭数据库连接 """
    if conn is not None:
        conn.close()

if __name__ == '__main__':
    conn = connect_db(db_file)
    #create_table(conn)
    #insert_data(conn)
    update_data(conn)
    delete_data(conn)
    close_db(conn)
