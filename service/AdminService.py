from fastapi.responses import JSONResponse
from pymysql import NULL
from dao import LoginDao
from dao import RegisterDao

'''
更新 密码加密
登录账号，info为字典，包含：用户登录名login_name、密码password，对应管理员或普通用户 status
输入正确的用户名和密码，返回1.密码是否正确 2.用户的全部信息 3.以及是否为管理员
否则登陆失败
'''
def userLogin(info):
    
    data_password=LoginDao.get_password(info['login_name'])#获取数据库加密后密码
    data_admin=LoginDao.is_admin(info['login_name'])#返回true/false

    #返回用户全部信息
    data=LoginDao.login_ueserInfo(info['login_name'])

    #对比密码
    #if data_password['password']==RegisterDao.encrypt(info['password']):
    if data_password==RegisterDao.encrypt(info['password']):
        data['isPassword']=True  #添加键值对，密码正确
    else:
        data['isPassword']=False 

    #对比status
    if data_admin:
        data['isAdmin']=True  #添加键值对，为管理员
    else:
        data['isAdmin']=False

    if data['isPassword']:
        return JSONResponse(
            content={
                'code': 200,
                'data': {
                    'data':data
                },
                'message': "successful"
            }
        )
    else:
        return JSONResponse(             
            {'message': "fail"}           
        )
    





'''
注册 
先判重，如果重复就提醒，如果不重复再增加待审核用户
info里包含login_name: str, password: str, name: str, dept_name: str, job_name: str, email:str, card_id:str
'''
def register_new_user(info):
    flag=RegisterDao.is_login_name_occupied(info['login_name'])
    #判断用户名是否重复
    if flag:  #true 被占用
        return JSONResponse(
            content={
                'code': 200,
                'message': "用户名重复"
            }
        )
    else:  #false 不重复，增加待审核用户
        RegisterDao.add_register(info['login_name'], info['password'], info['name'], info['dept_name'], info['job_name'], info['email'], info['card_id'])
        return JSONResponse(
        content={
            'code': 200,
            'message': 'successfully'
        }
    ) 


