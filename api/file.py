from fastapi import APIRouter,FastAPI,File,UploadFile
from starlette.responses import FileResponse
#from api import fileController
from pydantic import BaseModel
from service import FileService
import os
# 构建api路由
router = APIRouter()

class Filedata_user(BaseModel):
    title :str = ""
    # filename : str = ""
    # remark : str = ""
    promulgator : str = ""

# 员工权限

# 下载文件
@router.post("/Filedouwnload",tags=["文件"])
async def downloadFile(info:Filedata_user):
    #localfile = fileController.download(filename)
    return FileService.downloadFile(dict(info))

# 查找文件
@router.post("/Filesearch_U",tags=["文件"])
async def searchFile(info:Filedata_user):
    return FileService.searchFile(dict(info))

