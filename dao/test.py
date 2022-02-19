import DeptDao
import UserDao
import FileDao
# result = userDao.login("zhangsan")
# old_name = "财务部"
# name = "行政部"
# remark = ""
# remark = "财务部有从资本的融通（筹资管理）到现金的运营（财务管理）再到资本运作（投资管理）的三项职能"
# DeptDao.add_dept(name,remark)
# print(DeptDao.search_deptAll())
# print(UserDao.search_user("张三","2"))
# UserDao.delete_user("sunxing")
# UserDao.add_user("孙兴","2","sunxing","sunxing123","技术部","开发岗")
# UserDao.change_user("sunxing","Sunxing","sunxing456", "2")

# print(FileDao.search_file("title1"))
# print(FileDao.download_file(2))
# print(FileDao.search_all())
print(FileDao.delete_file(2))