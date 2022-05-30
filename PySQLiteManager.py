#
# IKD Web API Database Manager
# 
#
# Date:2022/05/30
#
#
import sqlite3
from sqlite3 import Error

# subroutine db_connection
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn
# --------- end of create_connection() ----------------

def create_table(dbConn):

    #Creating a cursor object using the cursor() method
    cursor = dbConn.cursor()

    #Doping table if already exists.
    cursor.execute("DROP TABLE IF EXISTS normal_class_member")

    #Creating table as per requirement
    sql ='''CREATE TABLE normal_class_member(
        -- 各班期內部課程總表
        `class_code` TEXT NOT NULL, -- 班級編號
        `course_no` TEXT PRIMARY KEY NOT NULL, -- 課程編號
        `course_name` TEXT NOT NULL, -- 課程名稱
        `course_date` TEXT NOT NULL, -- 上課日期
        `course_lector` TEXT NOT NULL, -- 授課講師
        `course_type` TEXT DEFAULT NULL, -- 課程類型 (NULL、必修、選修)
        `course_status` TEXT DEFAULT NULL, -- 狀態 (NULL、上過、調課、停課)
        `cdate` TEXT NOT NULL, -- 課程建立日期
        `cauth` TEXT NOT NULL -- 課程建立帳號紀錄
        )'''

    cursor.execute(sql)
    print("Table created successfully........")
    
# --------- end of create_table() ----------------

def main():
    database = r"database\iccf.ikd.org.db"

    #建立資料庫連線
    conn = create_connection(database)
    
    # create data table
    #create_table(conn)

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    NULL = None
    
    # The qmark style used with executemany():
    lang_list = [
        ('B289008', 'B2109000002', '41868', '段玉蘭', 'TWC033', '到班', '2020/04/05', '賴富子', '莫程安'),
        ('B289008', 'B2109000002', '41869', '林偉祥', 'TWC033', '到班', '2020/04/05', '賴富子', '莫惠萍'),
        ('B289008', 'B2109000002', '41876', '洪淑蕙', 'TWC034', '到班', '2020/04/05', '賴富子', '沈玉琳'),
        ('B289008', 'B2109000002', '113656', '謝敬&#23791;', 'TWC069', '到班', '2020/04/05', '賴富子', '嚴瑞蘭'),
        ('B289008', 'B2109000003', '41868', '段玉蘭', 'TWC033', '到班', '2020/04/05', '賴富子', '莫程安'),
        ('B289008', 'B2109000003', '41869', '林偉祥', 'TWC033', '到班', '2020/04/05', '賴富子', '莫惠萍'),
        ('B289008', 'B2109000003', '41876', '洪淑蕙', 'TWC034', '缺席', '2020/04/05', '賴富子', '沈玉琳'),
        ('B289008', 'B2109000003', '113656', '謝敬&#23791;', 'TWC069', '請假', '2020/04/05', '賴富子', '嚴瑞蘭'),
        ('B289008', 'B2109000004', '41868', '段玉蘭', 'TWC033', NULL, '2020/04/05', '賴富子', '莫程安'),
        ('B289008', 'B2109000004', '41869', '林偉祥', 'TWC033', NULL, '2020/04/05', '賴富子', '莫惠萍'),
        ('B289008', 'B2109000004', '41876', '洪淑蕙', 'TWC034', NULL, '2020/04/05', '賴富子', '沈玉琳'),
        ('B289008', 'B2109000004', '41874', '陳  治', 'TWT023', NULL, '2020/04/05', '賴富子', '吳清炎'),
        ('B289008', 'B2109000004', '113656', '謝敬&#23791;', 'TWC069', NULL, '2020/04/05', '賴富子', '嚴瑞蘭'),
        ('B289008', 'B2109000005', '41868', '段玉蘭', 'TWC033', NULL, '2020/04/05', '賴富子', '莫程安'),
        ('B289008', 'B2109000005', '41869', '林偉祥', 'TWC033', NULL, '2020/04/05', '賴富子', '莫惠萍'),
        ('B289008', 'B2109000005', '41876', '洪淑蕙', 'TWC034', NULL, '2020/04/05', '賴富子', '沈玉琳'),
        ('B289008', 'B2109000005', '41874', '陳  治', 'TWT023', NULL, '2020/04/05', '賴富子', '吳清炎'),
        ('B289008', 'B2109000005', '113656', '謝敬&#23791;', 'TWC069', NULL, '2020/04/05', '賴富子', '嚴瑞蘭'),
        ('B289008', 'B2109000006', '41868', '段玉蘭', 'TWC033', NULL, '2020/04/05', '賴富子', '莫程安'),
        ('B289008', 'B2109000006', '41869', '林偉祥', 'TWC033', NULL, '2020/04/05', '賴富子', '莫惠萍'),
        ('B289008', 'B2109000006', '41876', '洪淑蕙', 'TWC034', NULL, '2020/04/05', '賴富子', '沈玉琳'),
        ('B289008', 'B2109000006', '41874', '陳  治', 'TWT023', NULL, '2020/04/05', '賴富子', '吳清炎'),
        ('B289008', 'B2109000006', '113656', '謝敬&#23791;', 'TWC069', NULL, '2020/04/05', '賴富子', '嚴瑞蘭'),        
    ]
    cursor.executemany("insert into cycle_class_member values (?,?,?,?,?,?,?,?,?)", lang_list)

    print("Data insert successfully........")

    # Commit your changes in the database
    conn.commit()

    #Closing the connection
    conn.close()

# --------------- end of main() ------------------------

if __name__ == '__main__':
    main()