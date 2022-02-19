from fastapi import APIRouter,FastAPI,File,UploadFile
# 让数据以json的格式返回
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from service import MineService

# 构建api路由
router = APIRouter()

class userInfo(BaseModel):
    login_name :str = ""
    address : str = ""
    post_code : str = ""
    phone : str = ""
    card_id : str = ""
    qq_num : str = ""
    email : str = ""
    party : str = ""# 政治面貌
    birthday : str = ""# 出生日期
    race : str = ""# 民族
    education : str = ""# 学历
    speciality : str = ""# 专业
    hobby : str = ""# 爱好
    remark : str = ""# 备注

class adminInfo(BaseModel):
    name : str = ""
    login_name : str = ""
    sex : str = ""
    dept_name : str = ""
    job_name : str = ""
    phone : str = ""
    login_name : str = ""
    card_id : str = ""
    address : str = ""
    post_code : str = ""
    qq_num : str = ""
    email : str = ""
    party : str = ""# 政治面貌
    birthday : str = ""# 出生日期
    race : str = ""# 民族
    education : str = ""# 学历
    speciality : str = ""# 专业
    hobby : str = ""# 爱好
    remark : str = ""# 备注
    card_id : str = ""

class AccountSave(BaseModel):
    login_name : str = ""
    bepassword : str = ""
    password : str = ""



# 上传头像（上传一个文件）
@router.post("/updateIcon",tags=["我的"])
async def updateIcon(id:int):
    print(1)
    # print(info)
    # ### 1.通过调用相应的服务得到对应的反馈
    return MineService.updateIcon(id)

# 修改信息
@router.post("/updateInfo_U",tags=["我的"])
async def updateinfo(info:userInfo):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return MineService.userInfoEdit(dict(info))

# 管理员权限

# 信息修改
# @router.post("/updateIcon_U",tags=["我的"])
# async def loginadmin(info:adminInfo):
#     print(info)
#     ### 1.通过调用相应的服务得到对应的反馈
#     return MineService.InfouUpdateA(dict(info))

# 更换主题

# 

# 密码修改
@router.post("/passwordupdate",tags=["账户安全"])
async def passwordupdate(info:AccountSave):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return MineService.updatePassword(dict(info))

