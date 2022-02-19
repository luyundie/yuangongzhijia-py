from fastapi.responses import JSONResponse
from dao import DeptDao


'''
更新director
添加部门,
输入info,其中key值包括：部门名称，部门信息 name,remark
'''
def addDept(info):
    DeptDao.add_dept(info['name'],info['director'],info['remark'])
    return JSONResponse(
        content={
            'code': 200,
            'message': "successfully"     
        }
    )

#删除部门,根据部门名称
def deleteDept(info):
    DeptDao.delete_dept(info['name'])
    return JSONResponse(
        content={
            'code': 200,
            'message': 'if delete successfully'   
        }
    )

'''
更新director
修改部门
输入info,包括部门旧名称，新名称，新信息 bename,name,remark
'''
def updateDept(info):
    DeptDao.update_dept(info['bename'],info['name'],info['director'],info['remark'])
    return JSONResponse(
        content={
            'code': 200,
            'message': 'if change successfully'    
        }
    )  

'''
查询某个部门，
输入部门名称
返回name, director, remark
'''
def searchDept(info):
    data=DeptDao.search_dept(info['name'])
    return JSONResponse(
        content={
            'code': 200,
            'data': {  
                'data':data
            },
            'message': 'if find successfully'
        }
    )  

#返回全部部门及其信息
def searchDeptAll():
    data = DeptDao.search_deptAll()
    return JSONResponse(
        content={
            'code': 200,
            'data': {
                'data':data           
            },
            'message': "successfully"     
        }
    ) 

'''
新功能
普通用户查询，返回名称、主任、备注、员工列表
searchDeptForuser
'''
def searchDeptForuser(info):
    data=DeptDao.search_dept(info['name']) #返回 name, director, remark
    data_emp=DeptDao.dept_employeeList(info['name'])#返回员工字典的列表
    return JSONResponse(
        content={
            'code': 200,
            'data': {
                'data':data,
                'data_emp':data_emp          
            },
            'message': "successfully"     
        }
    )

'''
新功能
管理员查询，返回名称、主任、备注
searchDeptForuser
'''
def searchDeptForadmin(info):
    data=DeptDao.search_dept(info['name']) #返回 name, director, remark
    return JSONResponse(
        content={
            'code': 200,
            'data': {
                'data':data,       
            },
            'message': "successfully"     
        }
    )