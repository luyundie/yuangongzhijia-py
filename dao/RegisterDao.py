
''' 注册 register '''

import  pymysql
from typing import Optional
import hashlib


"""
根据某用户名，判断该用户名是否已被占用
判断是否被占用需要判断待审核表under_review和正式员工表employee中是否有该用户名
使用方式：is_login_name_occupied('zhangsan')
返回：False：未被占用 True：已被占用
"""
def is_login_name_occupied(login_name: str):
    under_review_judge = False
    employee_judge = False
    total_judge = False
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句
    # sql = """SELECT * FROM `job` WHERE name LIKE '%"""+name+"%'"
    under_review_sql = """select COUNT(login_name) as amount from under_review where login_name='%s'"""%login_name
    employee_sql = """select COUNT(login_name) as amount from employee where login_name='%s'"""%login_name
    try:
    # 执行sql语句
        cursor.execute(under_review_sql)
        data1 = cursor.fetchall()
        cursor.execute(employee_sql)
        data2 = cursor.fetchall()
    ## 把查询的数据填充到person对象是否可以(要循环这个游标进行数据的填充)
    ## 可以将查询的数据填充(组合)到自定义的模型中
    # 提交到数据库执行
        db.commit()
    except:
    # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()
    if data1[0]['amount'] >= 1:
        under_review_judge = True
    if data2[0]['amount'] >= 1:
        employee_judge = True
    total_judge = under_review_judge or employee_judge
    return total_judge



"""
增加用户注册
用户的注册信息写入待审核数据表under_review
注册信息：用户名、密码、姓名、部门、职位、email（选填）、身份证号（选填）
使用方法：
add_register(login_name='majiu', password='987654', name='马九', dept_name='技术部', job_name='测试岗', email='987654@163.com', card_id='330382199601019999')
"""
def add_register(login_name: str, password: str, name: str, dept_name: str, job_name: str, email: Optional[str]='', card_id: Optional[str]=''):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    m = hashlib.md5()
    m.update(password.encode())
    password = m.hexdigest()
    # SQL 插入语句
    sql = """INSERT INTO under_review(login_name, password, name, dept_name, job_name, email, card_id) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s")"""%\
    (login_name, password, name, dept_name, job_name, email, card_id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
        db.close()
        return {'message':'successfully'}  
    except:
        db.rollback()


"""
加密函数
将输入的密码用SHA-1加密，返回加密结果（字符串）
使用方法：encrypt('321654')
返回结果（即加密结果）：d553d148479a268914cecb77b2b88e6a
"""
def encrypt(password: str):
    m = hashlib.md5()
    m.update(password.encode())
    password = m.hexdigest()
    return password


