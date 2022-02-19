import pymysql

'''查询用户  name:用户名(名字)   status:状态 '''
def search_user(name: str,status:int):
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    if name == "":
        sql = """SELECT login_name,password,status,creat_date FROM employee WHERE status = "%s" """%status
    elif status == None:
        sql = """SELECT login_name,password,status,creat_date FROM employee WHERE name = "%s" """%name
    else:
        sql = """SELECT login_name,password,status,creat_date FROM employee WHERE name = "%s" AND status = %d """%(name,status)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        result = cursor.fetchone()
        db.commit()
        db.close()
        result["creat_date"] = str(result["creat_date"].date())
        if result:
            return result
        else:
            return None
    except:
        db.rollback()

'''删除用户     login_name:登录账号'''
def delete_user(login_name:str):
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """DELETE FROM employee WHERE login_name = "%s" """%login_name
    try:
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
        db.close()
        return {'message':'successfully'}  
    except:
        db.rollback()
# delete_user("test")
'''修改用户信息    old_login_name:旧登陆账号    login_name:新账号   password:新密码     status:新状态  dept_name    job_name'''
def change_user(old_login_name:str,login_name:str,password:str,status:int,dept_name:str,job_name:str):
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """UPDATE employee SET login_name = "%s", password = "%s", status = "%s", dept_name = "%s", job_name = "%s" WHERE login_name = "%s" """%(login_name,password,status,dept_name,job_name,old_login_name)
    try:
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
        db.close()
        return {'message':'successfully'}  
    except:
        db.rollback()

'''添加用户    name:姓名   status:状态    login_name:登录账号   password:密码   dept_name:部门  job_name:职位 '''
def add_user(name:str,status:int,login_name:str,password:str,dept_name:str,job_name:str):
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """INSERT INTO employee(name, status, login_name, password, dept_name, job_name) VALUES ("%s",%d,"%s", "%s", "%s", "%s")"""%\
    (name, status, login_name, password, dept_name, job_name)
    try:
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
        db.close()
        return {'message':'successfully'}  
    except:
        db.rollback()
