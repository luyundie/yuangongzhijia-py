# 公告 相关的数据库操作

import  pymysql
import time
from typing import Optional



'''
添加（发布）公告
三个参数：标题、内容、发布者(可选)。使用方法如下：
add_notice(title="测试公告3",content="这是测试公告的内容3.this is test notice content 3",promulgator="发布者3")
'''
def  add_notice(title: str, content: str, promulgator: Optional[str]=None):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句
    sql = """insert into notice(title, content, promulgator) values('%s', '%s', '%s')"""%(title, content, promulgator)
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
删除公告
一个参数：公告id。使用方法如下：delete_notice(8)
如果数据库中没有该id，则不会有动作
'''
def  delete_notice(id: int):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句
    sql = """delete from notice where id = %d"""%(id)
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
修改公告
四个参数：id、标题、内容、发布者(可选)，根据id为索引，更新公告。使用方法如下：
update_notice(id=8,title="测试公告3",content="这是测试公告的内容3.this is test notice content 3",promulgator="发布者3")
'''
def update_notice(id: int, title: str, content: str, promulgator: Optional[str]=None):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句
    sql = """update notice set title='%s', content='%s', promulgator='%s' where id=%s"""%(title, content, promulgator, id)
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
查询公告
一个参数：标题，用标题进行查询(支持模糊查询，返回所有包含输入字段的通知)。使用方法如下：
search_notice("测试")
'''
def search_notice(title: str):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句
    sql = """SELECT * FROM `notice` WHERE title LIKE '%"""+title+"%'"
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
    if len(data)!=1:
        for i in data:
            i["create_date"] = str(i["create_date"].date())
    else:
        data = data[0]
        data["create_date"] = str(data["create_date"].date())
    return data

# print(search_notice("测试"))


'''返回所有公告及其内容'''
def search_noticAll():
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """SELECT * FROM notice """
    try:
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        db.close()
    except:
        db.rollback()
    # print(data)
    if len(data)!=1:
        for i in data:
            i["create_date"] = str(i["create_date"].date())
    else:
        data = data[0]
        data["create_date"] = str(data["create_date"].date())
    return data


"""
返回对于某用户而言的新公告的序列
返回一个列表，列表中的数字即为对于该用户需要标注为'新公告'的公告其对应id
使用方法：new_notice_id_list('lisi')
返回信息：[11, 12]
"""
def new_notice_id_list(login_name: str):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # 获得当前用户的latest_notice_id
    sql1 = """SELECT latest_notice_id FROM `employee` WHERE login_name = '%s'"""%login_name
    cursor.execute(sql1)
    data1 = cursor.fetchall()
    db.commit()
    if len(data1) == 0:
        return {'message': 'No such a person'} 
    latest_notice_id = data1[0]['latest_notice_id']
    # 获取数据库中所有notice的id(转化成列表)
    sql2 = """SELECT id FROM `notice`"""
    try:
    # 执行sql语句
        cursor.execute(sql2)
        data2 = cursor.fetchall()
        db.commit()
        # data2： [{'id': 1}, {'id': 11}, {'id': 12}]
        notice_id_list = []
        for item in data2:
            notice_id = item['id']
            notice_id_list.append(notice_id)
        # new_notice_id_list存放notice_id_list中比latest_notice_id更大的id，即需要标注为新公告的id
        new_notice_id_list = []
        for i in notice_id_list:
            if i > latest_notice_id:
                new_notice_id_list.append(i)
    except:
    # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()
    return new_notice_id_list


"""
更新数据库中用户最近查看公告的id
使用方法：update_latest_notice_id('lisi')
"""
def update_latest_notice_id(login_name: str):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # 获取数据库中所有notice的id（转化成列表notice_id_list）
    sql1 = """SELECT id FROM `notice`"""
    cursor.execute(sql1)
    data1 = cursor.fetchall()
    db.commit()
    # data1： [{'id': 1}, {'id': 11}, {'id': 12}]
    notice_id_list = []
    for item in data1:
        notice_id = item['id']
        notice_id_list.append(notice_id)
    notice_id_list.sort(reverse=True)
    new_latest_id = notice_id_list[0]
    # print(new_latest_id)
    # SQL 插入语句
    sql = """update employee set latest_notice_id=%d where login_name='%s'"""%(new_latest_id, login_name)
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
