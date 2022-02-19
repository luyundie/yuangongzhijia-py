
import pymysql
from typing import Optional



'''
根据用户名判断是否为管理员
使用方法：is_admin('lisi')
返回  True/False
'''
def is_admin(login_name: str):
    judge = False
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句
    # sql = """SELECT * FROM `job` WHERE name LIKE '%"""+name+"%'"
    sql = """select COUNT(admin_login_name) as amount from admin where admin_login_name='%s'"""%login_name
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
    if data[0]['amount'] >= 1:
        judge = True
    return judge



'''登录     status对应管理员或普通用户(前端登录按钮)'''
def login(login_name: str,status:int):
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    if  status==1:
        sql = """SELECT password,status FROM employee WHERE login_name = "%s" AND status = %d"""%(login_name,status)
    else:
        sql = """SELECT password,status FROM employee WHERE login_name = "%s" """ %login_name
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        result = cursor.fetchone()
        db.commit()
        db.close()
        if result:
            return result
        else:
            return None
    except:
        db.rollback()


"""
根据login_name获取某员工的密码(加密后的)
返回密码（str）
使用方法：get_password("lisi")
返回：c33367701511b4f6020ec61ded352059
"""
def  get_password(login_name: str):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句
    s = " WHERE login_name="+"'"+str(login_name)+"'"
    sql = """SELECT employee.login_name, employee.password FROM employee"""+s
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
    if len(data) == 0:
        return {'message': 'No such a person'}
    return data[0]['password']
    

"""
登录时根据login_name获取该用户的全部信息
返回用户全部信息
使用方式：login_ueserInfo('lisi')
返回：{'login_name': 'lisi', 'password': 'c33367701511b4f6020ec61ded352059'......}

"""
def login_ueserInfo(login_name: str):
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    sql = '''select * from employee where login_name="%s"'''%login_name
    try:
    # 执行sql语句
        cursor.execute(sql)
        data = cursor.fetchall()
        db.commit()
    except:
        db.rollback()
    db.close()
    if len(data)!=1:
        for i in data:
            i["create_date"] = str(i["create_date"].date())
    else:
        data = data[0]
        data["create_date"] = str(data["create_date"].date())
    return data




'''修改密码    login_name:登录账号   bepassword:旧密码  password:新密码     ---验证登录名和旧密码后更新密码 '''
def update_password(login_name:str, bepassword:str, password:str):
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """UPDATE employee SET password = "%s" WHERE password = "%s" AND login_name = "%s" """%(password,bepassword,login_name)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        db.close()
        return {'message':'successfully'}
    except:
        db.rollback()
