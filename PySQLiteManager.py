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
    cursor.execute("DROP TABLE IF EXISTS class_room")

    #Creating table as per requirement
    sql ='''CREATE TABLE class_room(
        -- 上課教室或地點
        `no` INTEGER PRIMARY KEY AUTOINCREMENT, -- 流水號
        `status` TEXT NOT NULL , -- 顯示狀態 (Active、nouse)
        `country_code` TEXT NOT NULL, -- 地區代碼 (TW、ID、TH、MY)
        `room_no` TEXT NOT NULL, -- 教室編號
        `room_name` TEXT NOT NULL, -- 教室名稱
        `cdate` TEXT NOT NULL, -- 建立日期
        `cauth` TEXT NOT NULL -- 建立帳號紀錄
        )'''

    cursor.execute(sql)
    print("Table created successfully........")
    
# --------- end of create_table() ----------------

def main():
    database = r"database\iccf.ikd.org.db"

    #建立資料庫連線
    conn = create_connection(database)
    
    # create data table
    create_table(conn)

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    NULL = None
    
    # The qmark style used with executemany():
    lang_list = [
        (1, 'active', 'TW', 'IKD001', '崇正三樓佛堂', '2020/04/05', '賴富子'),
        (2, 'active', 'TW', 'IKD002', '歸元講堂六樓', '2020/04/05', '賴富子'),
        (3, 'active', 'TW', 'IKD003', '崇正二樓會議室', '2020/04/05', '賴富子'),
        (4, 'active', 'TW', 'IKD004', '歸元一樓餐廳', '2020/04/05', '賴富子'),
        (5, 'active', 'TW', 'IKD005', '崇正B302', '2020/04/05', '賴富子'),
        (6, 'active', 'TW', 'IKD006', '崇正B303', '2020/04/05', '賴富子'),
        (7, 'active', 'TW', 'IKD999', '崇正其他地方', '2020/04/05', '賴富子'),
        (8, 'active', 'TW', 'TWC100', '北部光明佛堂', '2020/04/05', '賴富子'),
        (9, 'active', 'TW', 'TWC101', '東部光蓮佛堂', '2020/04/05', '賴富子'),
        (10, 'active', 'TW', 'TWC102', '東部天德佛堂', '2020/04/05', '賴富子'),
        (11, 'active', 'TW', 'TWC103', '北部光浩佛堂', '2020/04/05', '賴富子'),
        (12, 'active', 'TW', 'TWC104', '北部光慈佛堂', '2020/04/05', '賴富子'),
        (13, 'active', 'TW', 'TWC105', '中部光祥佛堂', '2020/04/05', '賴富子'),
        (14, 'active', 'TW', 'TWC106', '南部光輝佛堂', '2020/04/05', '賴富子'),
        (15, 'active', 'TW', 'TWC107', '南部光雄佛堂', '2020/04/05', '賴富子'),
        (16, 'active', 'TW', 'TWA100', '台北通化佛堂', '2020/04/05', '賴富子'),
        (17, 'active', 'TW', 'TWE100', '彰化華德寶宮', '2020/04/05', '賴富子'),
        (18, 'active', 'TW', 'TWE999', '彰化華德寶宮其他地方', '2020/04/05', '賴富子'),
        (19, 'active', 'TW', 'TWH100', '屏東正宗佛堂', '2020/04/05', '賴富子'),
        (20, 'active', 'TW', 'TWH999', '屏東正宗佛堂其他地方', '2020/04/05', '賴富子'),
        (21, 'active', 'TW', 'TWT100', '精明寶宮妙極活動中心', '2020/04/05', '賴富子'),
        (22, 'active', 'TW', 'TWT999', '精明寶宮其他地方', '2020/04/05', '賴富子'),
        (23, 'active', 'TW', 'TWF100', '屏東大德佛堂', '2020/04/05', '賴富子'),
        (24, 'active', 'TW', 'TWF999', '屏東大德佛堂其他地方', '2020/04/05', '賴富子'),
    ]
    cursor.executemany("insert into class_room values (?,?,?,?,?,?,?)", lang_list)

    print("Data insert successfully........")

    # Commit your changes in the database
    conn.commit()

    #Closing the connection
    conn.close()

# --------------- end of main() ------------------------

if __name__ == '__main__':
    main()