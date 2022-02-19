# 服务层当中,服务是不能命名为数据库的操作名字
from fastapi.responses import JSONResponse
from dao import UserDao

'''
删除用户,输入用户名
'''
def deleteUser(login_name):
    UserDao.delete_user(login_name)
    return JSONResponse(
        content={
            'code': 200,
            'message': "if delete successfully"     
        }
    )

'''
查询用户  info包含key值：name:用户名(名字)   status:状态 
返回 data包含：login_name,password,status,creat_date
'''
def searchUser(info):
    data = UserDao.search_user(info['name'], info['status'])
    return JSONResponse(
        content={
            'code': 200,
            'data': {
                'data': data
            },
            'message': "successfully"
        }
    )


'''修改用户信息    
info包含key值：belogin_name:旧登陆账号 login_name:新账号 password:新密码 status:新状态
'''
def updateUser(info):
    UserDao.change_user(info['belogin_name'],info['login_name'],info['password'],info['status'],info['dept_name'],info['job_name'])
    return JSONResponse(
        content={
            'code': 200,
            'message': "successfully"     
        }
    )

'''
添加用户
infod包含key值：name:姓名 status:状态 login_name:登录账号 password:密码 dept_name:部门 job_name:职位 
'''
def addUser(info):
    UserDao.add_user(info['name'],info['status'],info['login_name'],info['password'],info['dept_name'],info['job_name'])
    return JSONResponse(
        content={
            'code': 200,
            'message': "successfully"     
        }
    )