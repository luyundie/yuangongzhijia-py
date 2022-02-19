# 员工 数据库相关的操作

import  pymysql
import time
from typing import Optional

'''
普通用户 多条件查询员工
六个参数：职位、姓名、身份证号、性别、手机、所属部门（全部可选）
使用方法如下：
所有参数非空：search_employee_foruser(job_name="架构师", name='XX', card_id='XXXX', sex=1, phone='XXXX', dept_name='XXXX')
只用部分条件筛选：search_employee_foruser(job_name="架构师", name='XX')
不输入任何参数则返回全部列表：search_employee_foruser()
返回内容：姓名、性别、部门、职位、手机
{'name': '李四', 'sex': 1, 'dept_name': '市场部', 'job_name': '分析师', 'phone': '13600000000'}
'''
def search_employee_foruser(job_name: Optional[str]='', name: Optional[str]='', card_id: Optional[str]=None, \
    sex: Optional[int]=None, phone: Optional[str]=None, dept_name: Optional[str]=''):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句 
    # 注意！因为只有职位、姓名、部门三个参数是所有员工都有的数据，其他的选项要选判断非空再加入多条件筛选，否则就算不输入参数也会默认参数非空，造成有些结果检索不到。
    sql = """select employee.name, employee.sex, employee.dept_name, employee.job_name, employee.phone from employee where job_name like '%"""+job_name+"%'" \
        + """ and name like '%"""+name+"%'" \
            + """ and dept_name like '%"""+dept_name+"%'"
    if sex != None:
        sql += """ and sex like '%"""+str(sex)+"%'"
    if card_id != None:
        sql += """ and card_id like '%"""+card_id+"%'"
    if phone != None:
        sql += """ and phone like '%"""+phone+"%'"
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
    # print(data)
    # if len(data)!=1:
    #     for i in data:
    #         i["create_date"] = str(i["create_date"].date())
    # else:
    #     data = data[0]
    #     data["create_date"] = str(data["create_date"].date())
    return data


'''
管理员 多条件查询员工 - 详情页显示所有信息，非详情的员工列表就只选取姓名、年龄、职位、手机显示，其他不显示）
六个参数：职位、姓名、身份证号、性别、手机、所属部门（全部可选）
使用方法如下：
所有参数非空：search_employee_foradmin(job_name="架构师", name='XX', card_id='XXXX', sex=1, phone='XXXX', dept_name='XXXX')
只用部分条件筛选：search_employee_foruser(job_name="架构师", name='XX')
不输入任何参数则返回全部列表：search_employee_foruser()
返回内容：全部信息 
{'login_name': 'lisi', 'password': '654321', 'status': 1, 'name': '李四'........}
'''
def search_employee_foradmin(job_name: Optional[str]='', name: Optional[str]='', card_id: Optional[str]=None, \
    sex: Optional[int]=None, phone: Optional[str]=None, dept_name: Optional[str]=''):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句 
    # 注意！因为只有职位、姓名、部门三个参数是所有员工都有的数据，其他的选项要选判断非空再加入多条件筛选，否则就算不输入参数也会默认参数非空，造成有些结果检索不到。
    sql = """select * from employee where job_name like '%"""+job_name+"%'" \
        + """ and name like '%"""+name+"%'" \
            + """ and dept_name like '%"""+dept_name+"%'"
    if sex != None:
        sql += """ and sex like '%"""+str(sex)+"%'"
    if card_id != None:
        sql += """ and card_id like '%"""+card_id+"%'"
    if phone != None:
        sql += """ and phone like '%"""+phone+"%'"
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
    # print(data)
    if len(data)!=1:
        for i in data:
            i["create_date"] = str(i["create_date"].date())
    else:
        data = data[0]
        data["create_date"] = str(data["create_date"].date())
    return data


# print(search_employee_foruser(dept_name='技术'))

'''返回所有员工的所有信息 - 相当于返回整个employee表'''
def search_employeeAll():
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    sql = '''select * from employee'''
    try:
    # 执行sql语句
        cursor.execute(sql)
        data = cursor.fetchall()
        db.commit()
    except:
        db.rollback()
    db.close()
    # print(data)
    if len(data)!=1:
        for i in data:
            i["create_date"] = str(i["create_date"].date())
    else:
        data = data[0]
        data["create_date"] = str(data["create_date"].date())
    return data

