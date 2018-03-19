# -*- coding:utf-8 -*-
import pypyodbc
import re
"""
南京12345获取数据库派送工单
pypyodbc - 1.3.4 need extra deployment
"""


def get_training_data():
    server = '127.0.0.1'
    username = 'sa'
    password = '559650Sql'
    dbname = 'njzwfw'
    SQL = "SELECT  DEALUNIT, concat(SUQIUADDRESS,'.',REQUESTTITLE,'.',[DESCRIPTION]) AS DETAIL " \
          "FROM [njzwfw].[dbo].[CASEINFO] WHERE DEALUNIT IS NOT NULL AND CREATEDATE >'2016-01-01 12:00:00' "
    connection_string = "Driver={SQL Server}; Server="+server+"; Database="+dbname \
                        + "; UID="+username+"; PWD="+password + ";"
    db = pypyodbc.connect(connection_string)
    cursor = db.cursor()
    cursor.execute(SQL)
    content = cursor.fetchall()
    cursor.close()
    db.close()

    f = open('train.txt', 'wb')
    for item in content:
        try:
            line = "{0}\t{1}\n".format(re.sub('[\s+]', '', item[0].encode('utf-8')),
                                       re.sub('[\s+]', '', item[1].encode('utf-8')))
            f.write(line)
        except Exception as err:
            print(err)
            print item[0], " This skipped line has an unknown issue, please check this line in your database. "
    f.close()

if __name__ == "__main__":
    get_training_data()