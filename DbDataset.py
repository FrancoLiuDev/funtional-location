import os
import sys
import pymysql
import time


HOST = "35.231.99.193"
USER = "root"
PASS = "root"
DBNAME = "dd_location"
PORT = "3306"

lastItem = ''

class DbDataset(object):

    @staticmethod
    def estanblishConn():
        db = pymysql.connect(HOST,
                             USER,
                             PASS,
                             DBNAME,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        return db

    @staticmethod
    def datasetInsertShop(items):
        tName = 'dd_location.supermarket'
     
        db = DbDataset.estanblishConn()
        cursor = db.cursor()
    
        fields = "(marketid,\
                   nickname, \
                   addr,\
                   city)"
        # for item in items['marketid']:
        for index in range(0, len(items['marketid'])-1):
            print('item',items['marketid'][index])
            print('nickname',items['nickname'][index])
            print('addr',items['addr'][index])
            print('city',items['city'][index])
         
            sqlQuery = ("INSERT INTO " + tName + fields + """\
                        VALUES ("%s", "%s", "%s", "%s")"""
                        % (str(items['marketid'][index]),unicode(items['nickname'][index]),unicode(items['addr'][index]),unicode(items['city'][index])))

            sqlQuery = cursor.execute(sqlQuery)
            db.commit()

        cursor.close()
   
