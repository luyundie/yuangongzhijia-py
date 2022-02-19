from api.login import create
from fastapi import APIRouter
# 让数据以json的格式返回
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from service import DeptService

# 构建api路由
router = APIRouter()

class department_user(BaseModel):
    name : str = ""

# 员工权限

## 查询部门及其信息
@router.post("/deptsearch_U",tags=["部门"])
async def searchdept_U(info:department_user):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return DeptService.searchDeptForuser(dict(info))



