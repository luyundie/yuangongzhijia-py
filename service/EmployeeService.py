from fastapi.responses import JSONResponse
from dao import EmployeeDao
from dao import UserInfoDao
from dao import UserDao
'''
多条件查询员工
info包含以下6个key：职位、姓名、身份证号、性别、手机、所属部门 job_name,name,card_id,sex,phone,dept_name
（全部可选,没输入的时候，key对应的value为''）

返回示例：
用户查询：返回姓名、性别、部门、职位、手机
管理员查询: 
[{'login_name': 'wangliu', 'password': '222222', 'status': 1, 'name': '王六', 'dept_name': '技术部', 
'job_name': '算法岗', 'card_id': '330382199501011111', 'address': '江苏省苏州市观前街', 'post_code': '215000', 
'phone': '13500000000', 'qq_num': None, 'email': None, 'sex': 1, 'party': None, 'birthday': None, 'race': None,
 'education': None, 'speciality': None, 'hobby': None, 'remark': None, 
 'create_date': datetime.datetime(2021, 8, 22, 15, 41, 10)}]
'''
def searchEmployeeForuser(info):
    data=EmployeeDao.search_employee_foruser(info['job_name'], info['name'], info['card_id'], info['sex'], info['phone'], info['dept_name'])
    return JSONResponse(
        content={
            'code': 200,
            'data': {  
                'data':data
            },
            'message': 'find successfully'
        }
    )

def searchEmployeeForadmin(info):
    data=EmployeeDao.search_employee_foradmin(info['job_name'], info['name'], info['card_id'], info['sex'], info['phone'], info['dept_name'])
    return JSONResponse(
        content={
            'code': 200,
            'data': {  
                'data':data
            },
            'message': 'find successfully'
        }
    )
'''
非管理员用户个人资料编辑 EmployeeService
以login_name为索引，管理员添加的用户名、权限状态、部门、职位信息个人不可修改，其他信息为选填
'''
def userInfoEdit(info):
    UserInfoDao.user_info_edit(info['login_name'], info['card_id'],\
         info['address'], info['post_code'], info['phone'], \
             info['qq_num'], info['email'],  \
                 info['party'], info['birthday'], info['race'], \
                     info['education'], info['speciality'], info['hobby'], info['remark'])
    return JSONResponse(
        content={
            'code': 200,
            'message': "successfully"     
        }
    )

'''
管理员编辑用户资料编辑 EmployeeService
以login_name为索引，修改部门、职位信息
'''
def adminEditEmployeeInfo(info):
    UserInfoDao.admin_edit_employeeInfo(info['login_name'],info['dept_name'],info['job_name'])
    return JSONResponse(
        content={
            'code': 200,
            'message': "successfully"     
        }
    )




def refreshUserAll():
    data = EmployeeDao.search_employeeAll()
    return JSONResponse(
        content={
            'code': 200,
            'data':data,
            'message': "successfully"     
        }
    )

    '''
删除用户,输入用户名
'''
def deleteEmployee(info):
    UserDao.delete_user(info['login_name'])
    return JSONResponse(
        content={
            'code': 200,
            'message': "if delete successfully"     
        }
    )
