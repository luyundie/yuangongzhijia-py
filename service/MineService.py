from fastapi.responses import JSONResponse
from pymysql import NULL
from dao import LoginDao
from dao import RegisterDao
from dao import UserInfoDao

'''
修改密码，
info为字典，包含：用户登录名login_name、旧密码bepassword，新密码password
验证登录名和旧密码后更新密码
'''
def updatePassword(info):
    en_bepassword=RegisterDao.encrypt(info['bepassword'])#旧密码加密
    en_password=RegisterDao.encrypt(info['password'])#新密码加密
    LoginDao.update_password(info['login_name'], en_bepassword,en_password)   
    return JSONResponse(
       content={
           'code': 200,
           'message': "successful"
       }
   )

'''
非管理员用户个人资料编辑 EmployeeService
以login_name为索引，管理员添加的用户名、权限状态、部门、职位信息个人不可修改，其他信息为选填
'''
def userInfoEdit(info):
    data=UserInfoDao.user_info_edit(info['login_name'], info['card_id'],\
         info['address'], info['post_code'], info['phone'], \
             info['qq_num'], info['email'], \
                 info['party'], info['birthday'], info['race'], \
                     info['education'], info['speciality'], info['hobby'], info['remark'])
    return JSONResponse(
        content={
            'code': 200,
            'message': "successfully"     
        }
    )