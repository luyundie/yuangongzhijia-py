from fastapi import APIRouter
# 让数据以json的格式返回
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from service import EmployeeService

# 构建api路由
router = APIRouter()

class Empdata_user(BaseModel):
    name : str = ""
    card_id : str = ""
    sex : str = ""
    dept_name : str = ""
    job_name : str = ""
    phone : str = ""



    


# 员工权限

## 查询用户
@router.post("/Empsearch_U",tags=["用户"])
async def searchEmployee_U(info:Empdata_user):
    print(info)
    ### 1.通过调用相应的服务得到对应的反馈
    return EmployeeService.searchEmployeeForuser(dict(info))




