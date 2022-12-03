# SQlite原生类型：BLOB对应python的bytes字节码
# python3使用sqlite3保存图片以及从数据读取图片
import sqlite3
import base64  # pip install pybase64
import cv2  # pip install opencv-python
import numpy as np  # pip3 install numpy scipy matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple


db_file = "studentDB.db"  # 数据库文件名
table_name = 'plant'  # 数据表名
    
def connect_db(db_file):
    """ 创建数据库连接 """
    conn = None  # 数据库连接
    try:
        conn = sqlite3.connect(db_file)  
        # 如果数据库不存在则创建文件
        print(f"数据库{db_file}连接成功。")
    except sqlite3.Error as e:
        print(e)
        print(f"数据库{db_file}连接失败！ ")
    return conn
 
def create_table(conn, table_name):
    """ 创建表 """
    cur = conn.cursor()  # 获得数据库的操作游标
    try:
        cur.execute(f'CREATE TABLE IF NOT EXISTS {table_name} '
                    '(name TEXT, photo TEXT, diary TEXT, image_bytes BLOB)')  # BLOB数据类型
        conn.commit()  #提交到数据库        
    except Exception as e:
        print(e)
        print(f"创建表 {table_name} 失败！ ")
    print(f"创建表  {table_name} 成功。 ")

def close_db(conn): 
    """ 关闭数据库连接 """
    if conn is not None:
        conn.close()

def get_pic_bytes(pic_file):
    """ 获取图片文字的字节码内容 """
    pic_bytes = None
    with open(pic_file, 'rb') as f:
        pic_bytes = f.read()
        #字节码进行编码
        content = base64.b64encode(pic_bytes) # 获取图片文字的字节码内容
        return content
    return None

def save_pic_to_db(conn, table_name, stu_name, pic_file):
    """ 把图片字节码存入数据库 """
    cur = conn.cursor()  # 获得数据库的操作游标
    content = get_pic_bytes(pic_file) # 获取图片文字的字节码内容
    #插入图片的二进制数据
    sql = f"INSERT INTO  {table_name} (name, photo, diary, image_bytes) VALUES (?,?,?,?);"
    #使用?占位符，是安全的sql语句
    cur.execute(sql, (stu_name, pic_file, content))
    conn.commit()


def get_pic_from_db(conn, table_name, stu_name):
    """ 从数据库读取指定学生的图片字节码，显示图片 """
    cur = conn.cursor()  # 获得数据库的操作游标     
    sql = f"SELECT image_bytes FROM  {table_name}  WHERE name='{stu_name}'"
    cur.execute(sql)
    value = cur.fetchone()  # 获取查询到的一条记录
    print("value类型：",type(value))
    if value:
        # base64编码对应的解码（解码完字符串）
        str_encode=base64.b64decode(value[0])
        # 把字节码转为opencv格式的数据
        nparr = np.frombuffer(str_encode, np.uint8)
        img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imshow("img",img_decode)  # 显示图片
        cv2.waitKey(0)

if __name__ == '__main__':
    conn = connect_db(db_file)
    create_table(conn, table_name)
    save_pic_to_db(conn, table_name, 'Crinkle Leaf', 'Crinkle Leaf.jepg')
    save_pic_to_db(conn, table_name, 'Graptoveria', 'Graptoveria.jepg')
    get_pic_from_db(conn, table_name, 'Crinkle Leaf')
    get_pic_from_db(conn, table_name, 'Graptoveria')    
    close_db(conn)