
''' 管理员审核注册人 '''

import  pymysql
from typing import Optional


"""
返回待审核表中所有用户所有信息（除密码）
管理员待审核的员工列表：姓名、用户名、email、dept_name、job_name
"""
def show_under_review_list():
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句
    sql = """SELECT name, login_name, email, dept_name, job_name FROM `under_review`"""
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


"""
管理员审核界面显示审核信息（详情界面）: 用户名、姓名、部门、职位、email、身份证号
根据login_name返回相关用户的信息
使用方法：show_review_info('chenqi')
返回一个字典:{'name': '陈七', 'login_name': 'chenqi', 'dept_name': '后勤部', 'job_name': '采购员', 'email': '12321@163.com', 'card_id': ''}
"""
def show_review_info(login_name: str):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句
    sql = """SELECT name, login_name, dept_name, job_name, email, card_id FROM `under_review` WHERE login_name = '%s'"""%login_name
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
    return data[0]


"""
某用户审核通过
将该用户的信息从under_view表移入employee表
使用方法：review_passed('yangba')
"""
def review_passed(login_name: str):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # 先获取该用户在under_review中的信息
    sql1 = """SELECT name, login_name, password, dept_name, job_name, email, card_id FROM `under_review` WHERE login_name = '%s'"""%login_name
    cursor.execute(sql1)
    data = cursor.fetchall()
    db.commit()
    if len(data) == 0:
        return {'message': 'No such a person'}
    user_name = data[0]['name']
    user_login_name  = data[0]['login_name'] 
    user_password  = data[0]['password'] 
    user_dept_name = data[0]['dept_name']
    user_job_name = data[0]['job_name']
    user_email = data[0]['email']
    user_card_id = data[0]['card_id']
    # 插入employee表
    sql2 = """INSERT INTO employee(name, login_name, password, dept_name, job_name, email, card_id) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s")"""%\
    (user_name, user_login_name, user_password, user_dept_name, user_job_name, user_email, user_card_id)
    # 审核通过，于是从under_review中删除
    sql3 = """DELETE FROM under_review WHERE login_name = "%s" """%login_name
    try:
    # 执行sql语句
        cursor.execute(sql2)
        cursor.execute(sql3)
        # data = cursor.fetchall()
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


"""
某用户审核不通过
将该用户的信息直接从under_view表删除
使用方法：review_failed('zhangwu')
"""
def review_failed(login_name: str):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句
    sql = """delete from under_review where login_name = '%s'"""%(login_name)
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

