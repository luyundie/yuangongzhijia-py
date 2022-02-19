from fastapi.responses import JSONResponse
from dao import ReviewDao

''' 管理员审核注册人 '''



"""
返回待审核表中所有用户所有信息（除密码）
data返回管理员待审核的员工列表的：姓名、用户名、email、dept_name、job_name
"""
def showUnderReviewList():
    data=ReviewDao.show_under_review_list()
    return JSONResponse(
        content={
            'code': 200,
            'data': {
                'data': data
            },
            'message': "successfully"
        }
    )

"""
管理员审核界面(详情)显示审核信息: 用户名、姓名、部门、职位、email、身份证号
输入info包含login_name
data返回一个字典:{'name': '陈七', 'login_name': 'chenqi', 'dept_name': '后勤部', 'job_name': '采购员', 'email': '12321@163.com', 'card_id': ''}
"""
def showReviewInfo(info):
    data=ReviewDao.show_review_info(info['login_name'])
    return JSONResponse(
        content={
            'code': 200,
            'data': {
                'data': data
            },
            'message': "successfully"
        }
    )


"""
某用户审核通过
输入info包含login_name
"""
def reviewPassed(info):
    ReviewDao.review_passed(info['login_name'])
    return JSONResponse(
        content={
            'code': 200,
            'message': "successfully"
        }
    )

"""
某用户审核失败
输入info包含login_name
"""
def reviewFailed(info):
    ReviewDao.review_failed(info['login_name'])
    return JSONResponse(
        content={
            'code': 200,
            'message': "successfully"
        }
    )