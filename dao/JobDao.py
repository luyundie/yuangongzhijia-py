# 公告 相关的数据库操作

import  pymysql
import time
from typing import Optional

# id name remark

'''
添加（发布）职位
两个参数：名称、备注（可选）。使用方法如下：
add_job(name='HR',remark='负责人事工作')
'''
def  add_job(name: str, remark: Optional[str]=None):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句
    sql = """insert into job(name, remark) values('%s', '%s')"""%(name, remark)
    try:
    # 执行sql语句
        cursor.execute(sql)
    ## 把查询的数据填充到person对象是否可以(要循环这个游标进行数据的填充)
    ## 可以将查询的数据填充(组合)到自定义的模型中
    # 提交到数据库执行
        db.commit()
    except:
    # 如果发生错误则回滚
        db.rollback() 
    # 关闭数据库连接
    db.close()
    return 


'''
删除职位
一个参数：职位名称。使用方法如下：delete_job("HR")
如果数据库中没有该职位，则不会有动作
'''
def  delete_job(name: str):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句
    sql = """delete from job where name = '%s'"""%(name)
    try:
    # 执行sql语句
        cursor.execute(sql)
    ## 把查询的数据填充到person对象是否可以(要循环这个游标进行数据的填充)
    ## 可以将查询的数据填充(组合)到自定义的模型中
    # 提交到数据库执行
        db.commit()
    except:
    # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()
    return 


'''
修改职位
两个参数：原名称、新名称、新备注（可选）。使用方法如下：
update_job("架构师","程序员","从事程序代码编写工作")
'''
def update_job(old_name: str, new_name: str, remark: Optional[str]=None):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句
    sql = """update job set name='%s', remark='%s' where name='%s'"""%(new_name, remark, old_name)
    try:
    # 执行sql语句
        cursor.execute(sql)
    ## 把查询的数据填充到person对象是否可以(要循环这个游标进行数据的填充)
    ## 可以将查询的数据填充(组合)到自定义的模型中
    # 提交到数据库执行
        db.commit()
    except:
    # 如果发生错误则回滚
        db.rollback() 
    # 关闭数据库连接
    db.close()
    return 


'''
查询职位
一个参数：职位名称，支持模糊查询，即返回所有包含输入字段的职位。使用方法如下：
search_job("开发岗")
'''
def  search_job(name: str):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句
    sql = """SELECT * FROM `job` WHERE name LIKE '%"""+name+"%'"
    try:
    # 执行sql语句
        cursor.execute(sql)
        data = cursor.fetchall()
    ## 把查询的数据填充到person对象是否可以(要循环这个游标进行数据的填充)
    ## 可以将查询的数据填充(组合)到自定义的模型中
    # 提交到数据库执行
        db.commit()
    except:
    # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()
    return data

# print(search_job("开发岗"))

def search_deptAll():
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """SELECT name, remark FROM job """
    try:
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        db.close()
        return result
    except:
        db.rollback()


