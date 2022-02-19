from fastapi import APIRouter,FastAPI,File,UploadFile
from fastapi.responses import JSONResponse
from pymysql.connections import DEFAULT_CHARSET
from starlette.responses import FileResponse
from dao import FileDao
import os
from service import fileController

'''
上传文件  
info的key值： title标题 filenam文件名 remark备注 promulgator发布人
'''
def addFile(title,filename,remark,promulgator,localfilepath):
    FileDao.add_file(title,filename,promulgator,remark)
    # fileController.upload(localfilepath,filename)
    return JSONResponse(
        content={
            'code': 200,
            'message': "successfully"
        }
    )

'''搜索文件
输入文件标题 
输出:data包含 id   title   filename   creat_date   promulgator
'''
def searchFile(info):
    data=FileDao.search_file(info['title'])
    if data:
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
            {'message': "查无此文件"}           
        )

'''
下载文件     
输入文件id    
输出文件名
'''
def downloadFile(info):
    #data=FileDao.download_file(info['filename'])
    # localfile = fileController.download(info['title'])
    # print("service")
    file_path = FileDao.download_file_path(info['title'])
    # return file_path
    print("filepath=",file_path)
    return JSONResponse(
        content={
            'code': 200,
            'data': {
                'data':file_path           
            },
            'message': "successfully"     
        }
    ) 

'''
返回全部文件信息,可能用于下载页面初始化
'''
def findAllFile():
    data =FileDao.search_all()
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
删除文件 
info包括：文件id   
返回：删除文件的文件名(可能用于本地或服务器文件的删除)
'''
def deleteFile(info):
    data = FileDao.delete_file(info['title'])
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
返回对于某用户而言的新文件的序列
返回一个列表，列表中的数字即为对于该用户需要标注为'新文件'的文件其对应id
'''
def newFileId(info):
    data=FileDao.new_file_id_list(info['login_name']) #获取新文件id
    FileDao.update_latest_file_id(info['login_name']) #更新数据库
    return JSONResponse(
        content={
            'code': 200,
            'data': {
                'data': data
            },
            'message': "successfully"
        }
    )