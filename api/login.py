from fastapi import APIRouter
# 让数据以json的格式返回
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from service import AdminService

# 构建api路由
router = APIRouter()

class log(BaseModel):
    login_name : str = ""
    password : str = ""

## 传输用户账号
@router.post("/Userlogin",tags=["登录"])
async def loginuser(info:log):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return AdminService.userLogin(dict(info))

class create(BaseModel):
    login_name : str = ""
    password : str = ""
    name : str = ""
#    sex :str = ""
#    age :str = ""
    email : str = ""
    card_id : str = ""
    job_name : str = ""
    dept_name : str = ""

## 注册
@router.post("/Register_new_user",tags=["登录"])
async def Register_new_user(info:create):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return AdminService.register_new_user(dict(info))

## 人脸识别
# @router.post("/Passwordupdate",tags=["登录"])
# async def updatepassword(info:create):
#     print(info)
#     ### 1.通过调用相应的服务得到对应的反馈
#     return AdminService.updatePassword(dict(info))