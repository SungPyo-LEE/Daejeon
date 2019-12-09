import sys
import os
import requests
import base64
import json
import logging
import pymysql
from bs4 import BeautifulSoup
from flask import request, jsonify, render_template, Flask

app = Flask(__name__)

host = "hostname"
port =
username = "name"
database = "mydb"
password = "mypassword"

# OpenAPI url 주소
url = 'https://apis.openapi.sk.com/tmap/traffic'
# 발급받은 서비스 인증키
key='apikey'

@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/update', methods=['GET'])
def update():
    try:
        conn = pymysql.connect(host, user=username, passwd=password, db=database, port=port, use_unicode=True, charset='utf8')
        cursor = conn.cursor()
    except:
        logging.error("could not connect to RDS")
        sys.exit(1)

    cursor.execute("SELECT RN,x,y FROM sktmap")
    RN=[]
    lon=[]
    lat=[]
    congestion=[]
    for (roadname,x, y,) in cursor.fetchall():
        lon.append(x)
        lat.append(y)
        RN.append(roadname)
    for i in range(0,len(lon)):
        suburl = '?version=1&centerLat=%f&centerLon=%f&reqCoordType=WGS84GEO&resCoordType=WGS84GEO&trafficType=POINT&zoomLevel=7&appKey=%s' % (lat[i], lon[i], key)
        rest_data=requests.get(url+suburl)
        soup=BeautifulSoup(rest_data.content,'html.parser')
        newDictionary=json.loads(str(soup))
        a=newDictionary['features']
        b=a[0]
        c=int(b['properties']['congestion'])
        congestion.append(c)
        query = "UPDATE sktmap SET congestion = %s WHERE x = %s" %(c,lon[i])
        cursor.execute(query)
    conn.commit()
    return render_template('home.html',
                            result=None,
                            resultUPDATE='Congestion Update')
if __name__=="__main__":
    app.run(debug=True)
