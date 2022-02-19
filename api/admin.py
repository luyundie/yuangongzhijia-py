from api.login import create
from fastapi import APIRouter
# 让数据以json的格式返回
from pydantic import BaseModel
from service import EmployeeService
from service import FileService
from service import DeptService
from service import NoticeService
from service import JobService
from service import ReviewService
from fastapi import APIRouter,FastAPI,File,UploadFile
import os

# 构建api路由
router = APIRouter()

# 数据类型设定
#--------------------------------------------------------------------------
# ● 部门类
#--------------------------------------------------------------------------
class department_admin(BaseModel):
    bename : str = ""
    name :str = ""
    remark : str = ""
    director : str = ""

## 添加部门及其信息
@router.post("/deptadd",tags=["管理-部门"])
async def adddept(info:department_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return DeptService.addDept(dict(info))
    
## 删除部门及其信息
@router.post("/deptdelete",tags=["管理-部门"])
async def deldept(info:department_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return DeptService.deleteDept(dict(info))

## 修改部门信息
@router.post("/deptupdate",tags=["管理-部门"])
async def updatedept(info:department_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return DeptService.updateDept(dict(info))

## 查询部门及其信息
@router.post("/deptsearch_A",tags=["管理-部门"])
async def searchdept_a(info:department_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return DeptService.searchDeptForadmin(dict(info))

#--------------------------------------------------------------------------
# ● 职位类
#--------------------------------------------------------------------------
class job_admin(BaseModel):
    name : str = ""
    bename : str = ""
    remark : str = ""

## 添加职位及其信息
@router.post("/jobadd",tags=["管理-职位"])
async def addjob(info:job_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return JobService.addJob(dict(info))

## 删除职位及其信息
@router.post("/jobdelete",tags=["管理-职位"])
async def deljob(info:job_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return JobService.deleteJob(dict(info))

## 查找职位及其信息
@router.post("/jobsearch",tags=["管理-职位"])
async def searchjob(info:job_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return JobService.searchJob(dict(info))

## 修改职位及其信息
@router.post("/jobupdate",tags=["管理-职位"])
async def updatejob(info:job_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return JobService.updateJob(dict(info))

#--------------------------------------------------------------------------
# ● 员工类
#--------------------------------------------------------------------------
class Empdata_admin(BaseModel):
    name : str = ""
    login_name : str = ""
    sex : str = ""
    dept_name : str = ""
    job_name : str = ""
    phone : str = ""
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

## 查询用户
@router.post("/Empsearch_A",tags=["管理-用户"])
async def searchEmployee_A(info:Empdata_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return EmployeeService.searchEmployeeForadmin(dict(info))

# ## 添加用户
# @router.post("/Empadditon",tags=["用户"])
# async def addemployee(info:Empdata_admin):
#     print(info)
#     ### 1.通过调用相应的服务得到对应的反馈
#     return EmployeeService.addEmployee(dict(info))

## 删除用户
@router.post("/Empdelete",tags=["管理-用户"])
async def delemployee(info:Empdata_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return EmployeeService.deleteEmployee(dict(info))

## 修改用户
@router.post("/AdminEditEmployeeInfo",tags=["管理-用户"])
async def admin_edit_employee_info(info:Empdata_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return EmployeeService.adminEditEmployeeInfo(dict(info))

#--------------------------------------------------------------------------
# ● 公告类
#--------------------------------------------------------------------------
class Noticedata_admin(BaseModel):
    id : int = 0
    title : str = "" # 标题
    content : str = "" # 内容
    promulgator : str = "" # 发布人
    creat_date : str = "" # 发布时间

## 查询公告
@router.post("/Noticesearch_A",tags=["管理-公告"])
async def searchNotice_A(info:Noticedata_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return NoticeService.searchNotice(dict(info))

## 添加公告
@router.post("/Noticeaddition",tags=["管理-公告"])
async def addnotice(info:Noticedata_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return NoticeService.addNotice(dict(info))

## 删除公告
@router.post("/noticedelete",tags=["管理-公告"])
async def delnotice(info:Noticedata_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return NoticeService.deleteNotice(dict(info))

## 修改公告
@router.post("/noticeupdate",tags=["管理-公告"])
async def updatenotice(info:Noticedata_admin):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return NoticeService.updateNotice(dict(info))

#--------------------------------------------------------------------------
# ● 文件类
#--------------------------------------------------------------------------
class Filedata_admin(BaseModel):
    title :str = ""
    filename : str = ""
    remark : str = ""
    promulgator : str = ""

# 上传文件
@router.post("/Fileupload",tags=["管理-文件"])
async def uploadFile(file:UploadFile = File(...),title:str = "",remark:str = "",promulgator:str = ""):
    content = await file.read()
    print(title)
    localfilepath = os.path.join("sx","tempFile",file.filename)
    with open(localfilepath,'wb') as f:
        f.write(content)
    f.close()
    return FileService.addFile(title,file.filename,remark,promulgator,localfilepath)
    # content = await info['file'].read()
    # localfilepath = info
    # #localfilepath = os.path.join("sx","tempFile",file.filename)
    # with open(localfilepath,'wb') as f:
    #     f.write(content)
    # # print(localfilepath)
    # fileController.upload(localfilepath,file.filename)
    # return

# 删除文件
@router.post("/Filedelete",tags=["管理-文件"])
async def deldFile(info:Filedata_admin):
    return FileService.deleteFile(dict(info))

# 查找文件
@router.post("/Filesearch_A",tags=["管理-文件"])
async def searchFile(info:Filedata_admin):
    return FileService.searchFile(dict(info))

#--------------------------------------------------------------------------
# ● 注册审核
#--------------------------------------------------------------------------
class Register(BaseModel):
    login_name : str = ""

# 通过
@router.post("/reviewpassed",tags=["管理-注册审核"])
async def reviewpassed(info:Register):
    return ReviewService.reviewPassed(dict(info))

# 否决
@router.post("/reviewfailed",tags=["管理-注册审核"])
async def reviewfailed(info:Register):
    return ReviewService.reviewFailed(dict(info))