from fastapi import APIRouter
# 让数据以json的格式返回
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from service import UserService

# 构建api路由
router = APIRouter()

class Empdata_user(BaseModel):
    name : str = ""
    login_name : str = ""
    sex : str = ""
    dept_name : str = ""
    job_name : str = ""
    phone : str = ""


class Empdata_admin(BaseModel):
    name : str = ""
    login_name : str = ""
    sex : str = ""
    dept_name : str = ""
    job_name : str = ""
    phone : str = ""
    login_name : str = ""
    card_id : str = ""
    
    # address : str = ""
    # post_code : str = ""
    # qq_num : str = ""
    # email : str = ""
    # party : str = ""# 政治面貌
    # birthday : str = ""# 出生日期
    # race : str = ""# 民族
    # education : str = ""# 学历
    # specially : str = ""# 专业
    # hobby : str = ""# 爱好
    # remark : str = ""# 备注
    # card_id : str = ""

    
# 显示页面

## 显示所有用户
@router.post("/refreshEmpAll",tags=["页面"])
async def refreshuser():
    ### 1.通过调用相应的服务得到对应的反馈
    return UserService.refreshUserAll()

# 员工权限

## 查询用户
@router.post("/Empsearch_U",tags=["用户"])
async def searchuser(info:Empdata_user):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return UserService.searchUser(dict(info))

# 管理员权限

## 查询用户
@router.post("/Empsearch_A",tags=["用户"])
async def searchuser(info:Empdata_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return UserService.searchUser(dict(info))

## 添加用户
@router.post("/Empadditon",tags=["用户"])
async def adduser(info:Empdata_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return UserService.addUser(dict(info))

## 删除用户
@router.post("/Empdelete",tags=["用户"])
async def deluser(info:Empdata_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return UserService.deleteUser(dict(info))

## 修改用户
@router.post("/Empupdate",tags=["用户"])
async def updateuser(info:Empdata_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return UserService.updateUser(dict(info))



