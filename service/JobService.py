from fastapi.responses import JSONResponse
from dao import JobDao

'''
添加（发布）职位
info包含两个key：名称name、备注remark（可选）。
'''
def addJob(info):
    JobDao.add_job(info['name'],info['remark'])
    return JSONResponse(
        content={
            'code': 200,
            'message': "successfully"     
        }
    )

'''
删除职位
一个参数：职位名称。
'''
def deleteJob(info):
    JobDao.delete_job(info['name'])
    return JSONResponse(
        content={
            'code': 200,
            'message': "successfully"     
        }
    )

'''修改职位
两个参数：原名称、新名称、新备注（bename, name, remark）
'''
def updateJob(info):
    JobDao.update_job(info['bename'], info['name'],info['remark'])
    return JSONResponse(
        content={
            'code': 200,
            'message': "successfully"
        }
    )

'''
查询职位
一个参数：职位名称，支持模糊查询，即返回所有包含输入字段的职位
'''
def searchJob(info):
    data=JobDao.search_job(info['name'])
    return JSONResponse(
        content={
            'code': 200,
            'data': {  
                'data':data
            },
            'message': 'if find successfully'
        }
    ) 

def refreshJobAll():
    data = JobDao.search_deptAll()
    return JSONResponse(
        content={
            'code': 200,
            'data': {
                'data':data           
            },
            'message': "find all successfully"     
        }
    ) 