from fastapi import APIRouter
# 让数据以json的格式返回
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from service import NoticeService

# 构建api路由
router = APIRouter()

class Noticedata_user(BaseModel):
    id : int = 0
    title : str = "" # 标题
    promulgator : str = "" # 发布人

## 查看公告
@router.post("/Noticeread",tags=["公告"])
async def NoticeRead(info:Noticedata_user):
    return NoticeService.ReadAll(dict(info))
# 员工权限

## 查询公告
@router.post("/Noticesearch_U",tags=["公告"])
async def searchNotice_U(info:Noticedata_user):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return NoticeService.searchNotice(dict(info))



