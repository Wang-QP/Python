import pymysql
import xlrd

#打开数据库连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    database='test003',
    charset='utf8'
)
#获取游标
cursor=conn.cursor()
# print(cursor)

count = 0

def getUnid():
    """第二种方法"""
    import time, hashlib
    m = hashlib.md5()
    m.update(bytes(str(time.time()), encoding='utf-8'))
    return m.hexdigest()

def findDept(deptName):
  sql = "select * from cfg_dept where dept_alias = (%s);"
  length = cursor.execute(sql,[deptName])
  # print(length)

  # data = cursor.fetchmany(length)
  data = cursor.fetchone()
  if data is None:
    return None;
  return data[0]

def findUser(pliceNo):
  sql = "select * from cfg_user where user_police_id = (%s);"
  length = cursor.execute(sql,[pliceNo])
  data = cursor.fetchone()
  # print(length)
  # if length > 0: 
  #   global count
  #   count +=1 
  if data is None:
    return None;
  return data[0]

def insertUser(user):
  sql = "insert into cfg_user(unid,dept_unid,user_login_name,user_password,user_real_name,user_police_id,user_id_card) values(%s,%s,%s,%s,%s,%s,%s);"
  length = cursor.execute(sql,user)
  if length == 1:
    conn.commit()
  else:
    print(user)


def updateUser(user):
  sql = "update cfg_user set dept_unid = %s, user_real_name = %s, user_id_card = %s where unid = %s"
  length = cursor.execute(sql,user)
  if length == 1:
    conn.commit()
  else:
    print(user)

def excel():
    book1 = xlrd.open_workbook('表格.xls')
    excel_sheet = book1.sheet_by_index(0)
    nrows = excel_sheet.nrows
    deptNameList = []
    for i in range(1,nrows) :
      # print(type(excel_sheet.row(i)))
      dept = excel_sheet.cell_value(i,1)
      name = excel_sheet.cell_value(i,2)
      pliceNo = str(int(excel_sheet.cell_value(i,3)))
      idcardNo = excel_sheet.cell_value(i,4)


      deptUind = findDept(dept)
      if deptUind is None :
        # print(dept)
        deptNameList.append(dept)
        global count
        count += 1

    print(set(deptNameList))

if __name__ == '__main__':
  excel()
  print(count)