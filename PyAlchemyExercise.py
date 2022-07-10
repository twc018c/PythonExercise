#
# SQLalchemy Exercise
#
# Date:2022/07/07
# 
# pip install sqlalchemy --user --no-warn-script-location
# 
from asyncio.windows_events import NULL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, Integer, String, create_engine, DATETIME
from sqlalchemy.orm import sessionmaker

# 連結 SQLite3 資料庫
engine = create_engine(r'sqlite:///database\iccf.ikd.org.db')

# Create a delclarative_base() class named Base
Base = declarative_base()

# 設定資料表 schema
class Class_info(Base):
    __tablename__ = 'class_info'
    class_code = Column(Text, primary_key=True, nullable=False)
    class_mamager = Column(Text)
    class_host = Column(Text)
    class_assistant = Column(Text)
    class_room = Column(Text, nullable=False)
    class_room_memo = Column(Text)
    class_details = Column(Text)
    singup_restrictions_no = Column(Text)

    def __repr__(self):
        return f'Class_info( {self.class_code}, {self.class_mamager}, {self.class_host}, {self.class_assistant}, {self.class_room}, {self.class_room_memo}, {self.class_details}, {self.singup_restrictions_no} )'

# 新增資料表
def create_table():
    Base.metadata.create_all(engine)

# 刪除資料表
def drop_table():
    Base.metadata.drop_all(engine)

# 建立實體類別
def create_session():
    # 把 DB engine 與 session 綁在一起
    Session = sessionmaker(bind=engine)
    # 實體化 Session 這個 class
    session = Session()
    return session

# 批次新增資料
def add_dataset(sc):

    sc.add_all([
    Class_info(class_code='A188002', class_mamager='翁嵩山', class_host='王延平, 蔡玲君', class_assistant=NULL, class_room='崇正三樓佛堂', class_room_memo=NULL, class_details=NULL, singup_restrictions_no=NULL),
    Class_info(class_code='D189018', class_mamager='王延平', class_host=NULL, class_assistant=NULL, class_room='歸元講堂六樓', class_room_memo=NULL, class_details=NULL, singup_restrictions_no=NULL),
    Class_info(class_code='D188015', class_mamager='蔡玲君', class_host=NULL, class_assistant=NULL, class_room='北部光明佛堂', class_room_memo=NULL, class_details=NULL, singup_restrictions_no=NULL)
    ])

def main():
    sc = create_session()
    add_dataset(sc)
    our_user = sc.query(Class_info).filter_by(class_code='D188015').first()
    print('the result of D188015 Class_info is: ', our_user)

# --------------- end of main() ------------------------

if __name__ == '__main__':
    main()