from api.login import log
from fastapi import APIRouter
from pydantic.main import BaseModel
# 让数据以json的格式返回
from service import EmployeeService
from service import FileService
from service import DeptService
from service import NoticeService
from service import AdminService
from service import ReviewService
from service import MineService

# 构建api路由
router = APIRouter()

# 构造页面

## 显示所有用户
@router.post("/refreshEmpAll",tags=["页面"])
async def refreshuser():
    ### 1.通过调用相应的服务得到对应的反馈
    return EmployeeService.refreshUserAll()

## 直接显示所有部门信息
@router.post("/deptrefresh",tags=["页面"])
async def refershdeptall():
    return DeptService.searchDeptAll()

## 显示所有公告
@router.post("/Noticrefresh",tags=["页面"])
async def refreshnotice():
    return NoticeService.refreshNoticeAll()

# ## 注册审核 显示注册信息
# @router.post("/Registerrefresh",tags=["页面"])
# async def refreshregister():
#     ### 1.通过调用相应的服务得到对应的反馈
#     return AdminService.refreshRegister()

# 所有文件显示
@router.post("/refreshFileAll",tags=["页面"])
async def refreshFileAll():
    return FileService.findAllFile()

# 我的资料显示
@router.post("/refreshInfoAll",tags=["页面"])
async def refreshInfo():
    print()
    ### 1.通过调用相应的服务得到对应的反馈
    return MineService.refreshInfoAll()

# 注册页面列表
@router.post("/refresh_underReview",tags=["页面"])
async def show_under_review_list():
    return ReviewService.showUnderReviewList()

# 注册详细信息页面
class ReviewInfo(BaseModel):
    login_name : str = ""
    name : str = ""
    email : str = ""
    dept_name : str = ""
    job_name : str = ""

@router.post("/refresh_ReviewInfo",tags=["页面"])
async def show_reviewinfo(info:ReviewInfo):
    return ReviewService.showReviewInfo(info)


class update_index(BaseModel):
    login_name : str = ""


# 更新最新文件显示
@router.post("/updaten_new_file",tags=["页面"])
async def refreshNewFile(info :  update_index):
    return FileService.newFileId(dict(info))

# 更新最新公告显示
@router.post("/updaten_new_notice",tags=["页面"])
async def refreshNewNotice(info :  update_index):
    return NoticeService.newNoticeId(dict(info))