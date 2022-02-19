import pymysql
from typing import Optional



"""
根据部门名称获取部门的员工列表（不支持模糊查询！）
返回的员工列表内员工的信息包括：姓名、性别、部门、职位、手机
使用方式：dept_employeeList("技术")
返回内容：[{'name': '孙兴', 'sex': None, 'dept_name': '技术部', 'job_name': '架构师', 'phone': '13500000000'}, 
{'name': '王六', 'sex': 1, 'dept_name': '技术部', 'job_name': '算法岗', 'phone': '13500000000'}, 
{'name': '张三', 'sex': 1, 'dept_name': '技术部', 'job_name': '架构师', 'phone': '13500000000'}]
"""
def dept_employeeList(name: str):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句
    sql = """select name, sex, dept_name, job_name, phone from employee where dept_name = '%s'"""%name
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


'''添加部门    name:部门名字  director:部门主任  remark:备注 '''
def add_dept(name:str, director:str, remark: Optional[str]=None):
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """INSERT INTO dept(name, director, remark) VALUES ("%s","%s","%s")"""%(name, director, remark)
    try:
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
        db.close()
        return {'message':'successfully'}  
    except:
        db.rollback()


'''删除部门    name:要删除的部门名字'''
def delete_dept(name:str):  
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """DELETE FROM dept WHERE name = "%s" """%name
    try:
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
        db.close()
        return {'message':'successfully'}  
    except:
        db.rollback()


'''修改部门信息    old_name:原部门名字  name:新名 director:主任(可选)  remark:备注(可选)'''
def update_dept(old_name:str,name:str,director:Optional[str]=None,remark:Optional[str]=None):  
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """UPDATE dept SET name = "%s", director = "%s", remark = "%s" WHERE name = "%s" """%(name,director,remark,old_name)
    try:
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
        db.close()
        return {'message':'successfully'}  
    except:
        db.rollback()


'''搜索某个部门     name:部门名字'''
def search_dept(name:str):  
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # sql = """SELECT name, director, remark FROM dept WHERE name = "%s" """%name
    sql = """select name, director, remark from dept where name LIKE '%"""+name+"%'"
    try:
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchone()
        db.close()
        return result
    except:
        db.rollback()


'''返回全部部门及其信息'''
def search_deptAll():
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """SELECT name, director, remark FROM dept """
    try:
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        db.close()
        return result
    except:
        db.rollback()