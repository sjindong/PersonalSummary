#导入SQLite驱动
import sqlite3
#连接sqlite数据库
#数据库文件 test.db
#如果文件不存在，则自动在当前目录创建
conn =  sqlite3.connect('test.db')
#创建一个Cursor指针
cursor = conn.cursor()
#执行 sql语句，创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#执行语句，插入记录
cursor.execute('insert into user (id, name) values (\'1\',\'name\')')
#通过rowcount获取插入的行数
cursor.rowcount
#执行语句，查询记录
cursor.execute('select * from user where id=?', ('1',))
values = cursor.fetchall()
print(values)
#关闭sql指针
cursor.close()
