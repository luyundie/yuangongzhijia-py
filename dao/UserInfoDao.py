# 个人资料编辑 

import  pymysql
import time
from typing import Optional


'''
非管理员用户个人资料编辑 - 用户编辑自己的资料
以login_name为索引，管理员添加的用户名、权限状态、部门、职位信息个人不可修改，其他信息为选填
使用方法如下：
user_info_edit(login_name='lisi', card_id='330382199401010000', address='浙江省杭州市凤起路', post_code='310000', phone='13600000000')
'''
def user_info_edit(login_name: str, \
    card_id: Optional[str]="", address: Optional[str]="", post_code: Optional[str]="", \
        phone: Optional[str]="", qq_num: Optional[str]="", email: Optional[str]="", \
            party: Optional[str]="", birthday: Optional[str]="", \
                race: Optional[str]="", education: Optional[str]="", speciality: Optional[str]="", \
                    hobby: Optional[str]="", remark: Optional[str]=""):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句
    # 空参数对应的命令应该忽略，不然原有值会被空值覆盖。用if判断，判断为非空参数后再把命令加入SQL
    sql = """update employee set"""
    if card_id != "":
        sql += " card_id='%s',"%card_id
    if address != "":
        sql += " address='%s',"%address
    if post_code != "":
        sql += " post_code='%s',"%post_code
    if phone != "":
        sql += " phone='%s',"%phone
    if qq_num != "":
        sql += " qq_num='%s',"%qq_num
    if email != "":
        sql += " email='%s',"%email
    # if sex != "":
    #     sql += " sex=%s,"%sex
    if party != "":
        sql += " party='%s',"%party
    if birthday != "":
        sql += " birthday='%s',"%birthday
    if race != "":
        sql += " race='%s',"%race
    if education != "":
        sql += " education='%s',"%education
    if speciality != "":
        sql += " speciality='%s',"%speciality
    if hobby != "":
        sql += " hobby='%s',"%hobby
    if remark != "":
        sql += " remark='%s',"%remark
    # 最后多出一个逗号，要删除
    sql = sql[:-1]
    sql += """ where login_name='%s'"""%login_name
    # print(sql)
    try:
    # 执行sql语句
        cursor.execute(sql)
    ## 把查询的数据填充到person对象是否可以(要循环这个游标进行数据的填充)
    ## 可以将查询的数据填充(组合)到自定义的模型中
    # 提交到数据库执行
        db.commit()
    except:
    # 如果发生错误则回滚
        db.rollback() 
    # 关闭数据库连接
    db.close()
    return 



'''
管理员编辑员工资料
以login_name为索引，管理员只能员工的修改部门和职位信息
使用方法如下：admin_edit_employeeInfo(login_name='Sunxing',dept_name='技术部',job_name='UI设计')
'''
def admin_edit_employeeInfo(login_name: str, dept_name: Optional[str]="", job_name: Optional[str]=""):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # SQL 插入语句
    # 空参数对应的命令应该忽略，不然原有值会被空值覆盖。用if判断，判断为非空参数后再把命令加入SQL
    sql = """update employee set"""
    if dept_name != "":
        sql += " dept_name='%s',"%dept_name
    if job_name != "":
        sql += " job_name='%s',"%job_name
    # 最后多出一个逗号，要删除
    sql = sql[:-1]
    sql += """ where login_name='%s'"""%login_name
    # print(sql)
    try:
    # 执行sql语句
        cursor.execute(sql)
    ## 把查询的数据填充到person对象是否可以(要循环这个游标进行数据的填充)
    ## 可以将查询的数据填充(组合)到自定义的模型中
    # 提交到数据库执行
        db.commit()
    except:
    # 如果发生错误则回滚
        db.rollback() 
    # 关闭数据库连接
    db.close()
    return 
