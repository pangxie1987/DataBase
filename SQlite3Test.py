# -*- coding:utf-8 -*-

'''
使用sqlite3数据库，python自带，不需要安装
当connect的库不存在时，自动创建一个库
将sql数据以本地文件的形式保存
'''

import sqlite3
conn = sqlite3.connect('test')
cuor = conn.cursor()

# cuor.execute('create table users(id INTEGER, name VARCHAR(8))')

def execute(sql):
    data = cuor.execute(sql)
    print(data.fetchall())
    return data.fetchall()
sql_insert = 'insert into users values(50002,1000)'
sql = 'select * from users'

execute(sql_insert)
conn.commit()
execute(sql)

sql_update = 'update users set name=1001 where id=50002'
execute(sql_update)
execute(sql)