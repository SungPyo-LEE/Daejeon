import sys
import requests
import base64
import json
import logging
import pymysql
import csv
import pandas as pd

host = "hostname"
port =
username = "name"
database = "mydb"
password = "mypassword"


def insert_row(cursor, data, table):
    placeholders=','.join(['%s'] * len(data)) #'%s','%s','%s'...'%s'
    columns = ','.join(data.keys())
    key_placeholders=','.join(['{0}=%s'.format(k) for k in data.keys()]) #id=%s,name=%s
    sql="INSERT INTO %s ( %s ) VALUES ( %s ) ON DUPLICATE KEY UPDATE %s" %(table,columns, placeholders, key_placeholders)
    cursor.execute(sql, list(data.values())*2)


def main():

    #connection을 먼저 만들고
    try:
        conn = pymysql.connect(host, user=username, passwd=password, db=database, port=port, use_unicode=True, charset='utf8')
        cursor = conn.cursor()
    except:
        logging.error("could not connect to RDS")
        sys.exit(1)

    indx_10=pd.read_csv('csv경로\\08_19_TOP40_1330.csv',engine='python')
    x=indx_10['x']
    y=indx_10['y']
    RN= indx_10['RN']
    congestion = indx_10['Congestion']
    dic={}
    for i in range(len(RN)):
        dic.update({
                'RN':RN[i],
                'congestion':congestion[i],
                'x':round(x[i],4),
                'y':round(y[i],4)
            })
        query="INSERT INTO sktmap (RN, congestion, x, y) VALUES ('{}','{}','{}','{}')".format(RN[i],congestion[i],round(x[i],4),round(y[i],4))
        cursor.execute(query)
    conn.commit()
if __name__=="__main__":
    main()
