from fastapi.responses import JSONResponse
from dao import NoticeDao

'''
添加（发布）公告
三个参数：标题、内容、发布者(可选)。title, content, promulgator
'''
def addNotice(info):
    NoticeDao.add_notice(info['title'], info['content'], info['promulgator'])
    return JSONResponse(
        content={
            'code': 200,
            'message': "successfully"     
        }
    )

#删除公告,输入公告id
def deleteNotice(info):
    data=NoticeDao.delete_notice(info['id'])
    if data:
        return JSONResponse(
            content={
                'code': 200,
                'data': {
                    'data':data
                },
                'message': "successful"
            }
        )
    else:
        return JSONResponse(             
            {'message': "请输入正确的公告id"}           
        )

'''
修改公告 
info包括id、标题、内容、发布者(id, title, content, promulgator)
'''
def updateNotice(info):
    NoticeDao.update_notice(info['id'], info['title'],info['content'] ,info['promulgator'] )
    return JSONResponse(
        content={
            'code': 200,
            'message': "successfully"     
        }
    )

'''
查询公告 
参数：标题
支持模糊查询
返回所有包含输入字段通知的id，title，content，create_date，promulgator
'''
def searchNotice(info):
    data=NoticeDao.search_notice(info['title'])
    if data:
        return JSONResponse(
            content={
                'code': 200,
                'data': {
                    'data':data
                },
                'message': "successful"
            }
        )
    else:
        return JSONResponse(             
            {'message': "查无此公告"}           
        )

def refreshNoticeAll():
    data = NoticeDao.search_noticAll()
    return JSONResponse(
        content={
            'code':200,
            'data':data,
            'message':'successful'
        }
    )

'''
返回对于某用户而言的新公告的序列
返回一个列表，列表中的数字即为对于该用户需要标注为'新公告'的公告其对应id
'''
def newNoticeId(info):
    data=NoticeDao.new_notice_id_list(info['login_name']) #获取新公告id
    NoticeDao.update_latest_notice_id(info['login_name']) #更新数据库
    return JSONResponse(
        content={
            'code': 200,
            'data': {
                'data': data
            },
            'message': "successfully"
        }
    )