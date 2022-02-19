import  pymysql
from typing import Optional



'''上传文件  传入 title标题 filenam文件名 remark备注 promulgator发布人'''
def add_file(title:str,filename:str,promulgator:str,remark:Optional[str]=None):
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """INSERT INTO document(title, filename, promulgator, remark) VALUES("%s","%s","%s","%s") """%(title, filename, promulgator, remark)
    try:
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
        db.close() 
    except:
        db.rollback()


'''搜索文件, 输入文件标题  输出: id   title   filename   creat_date   promulgator'''
def search_file(title:str):
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """SELECT * FROM `document` WHERE title LIKE '%"""+title+"%'"
    try:
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        db.close()
        # print(result)
        if len(result)!=1:
            for i in result:
                i["create_date"] = str(i["create_date"].date())
        else:
            result = result[0]
            result["create_date"] = str(result["create_date"].date())
        return result
    except:
        db.rollback()


'''下载文件     输入文件id    输出文件名'''
def download_file(title:str):
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """SELECT filename FROM document WHERE title = "%s" """%title
    try:
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchone()
        db.close()
        return result
    except:
        db.rollback()

def download_file_path(file_name: str):
    path = 'http://42u47210c7.wicp.vip/tempFile/' + file_name
    # print("dao")
    # path = 'http://127.0.0.1:10086/tempFile/' + file_name
    return path
# print(download_file_path('csi.docx'))

'''返回全部文件信息,可能用于下载页面初始化'''
def search_all():
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """SELECT * FROM document """
    try:
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        db.close()
        # print(result)
        if len(result)!=1:
            for i in result:
                i["create_date"] = str(i["create_date"].date())
        else:
            result["create_date"] = str(result["create_date"].date())
        return result
    except:
        db.rollback()


'''删除文件    返回删除文件的文件名(可能用于本地或服务器文件的删除)'''
def delete_file(title:str):
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql1 =  """SELECT filename FROM document WHERE title = "%s" """%title
    sql2 = """DELETE FROM document WHERE title = "%s" """%title
    try:
        # 执行sql语句
        cursor.execute(sql1)
        result = cursor.fetchone()
        print(result)
        cursor.execute(sql2)
        db.commit()
        db.close()
        return result
    except:
        db.rollback()


"""
返回对于某用户而言的新文件的序列
返回一个列表，列表中的数字即为对于该用户需要标注为'新文件'的文件其对应id
使用方法：new_file_id_list('lisi')
返回信息：[2]
"""
def new_file_id_list(login_name: str):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # 获得当前用户的latest_file_id
    sql1 = """SELECT latest_file_id FROM `employee` WHERE login_name = '%s'"""%login_name
    cursor.execute(sql1)
    data1 = cursor.fetchall()
    db.commit()
    latest_file_id = data1[0]['latest_file_id']
    # 获取数据库中所有file的id(转化成列表)
    sql2 = """SELECT id FROM `document`"""
    try:
    # 执行sql语句
        cursor.execute(sql2)
        data2 = cursor.fetchall()
        db.commit()
        # data2： [{'id': 1}, {'id': 11}, {'id': 12}]
        file_id_list = []
        for item in data2:
            file_id = item['id']
            file_id_list.append(file_id)
        # new_file_id_list存放file_id_list中比latest_file_id更大的id，即需要标注为新公告的id
        new_file_id_list = []
        for i in file_id_list:
            if i > latest_file_id:
                new_file_id_list.append(i)
    except:
    # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()
    return new_file_id_list

"""
更新数据库中用户最近查看文件的id
使用方法：update_latest_file_id('lisi')
"""
def update_latest_file_id(login_name: str):
    # 打开数据库连接
    db = pymysql.connect(host="101.34.48.210", user="root", password="Wangweijie123", database="hlj")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # 获取数据库中所有file的id（转化成列表file_id_list）
    sql1 = """SELECT id FROM `document`"""
    cursor.execute(sql1)
    data1 = cursor.fetchall()
    db.commit()
    # data1： [{'id': 1}, {'id': 11}, {'id': 12}]
    file_id_list = []
    for item in data1:
        file_id = item['id']
        file_id_list.append(file_id)
    file_id_list.sort(reverse=True)
    new_latest_id = file_id_list[0]
    # print(new_latest_id)
    # SQL 插入语句
    sql = """update employee set latest_file_id=%d where login_name='%s'"""%(new_latest_id, login_name)
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

