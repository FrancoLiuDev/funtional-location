import os
import sys
import pymysql
import time
import psycopg2

# HOST = "35.201.196.254"
# USER = "root"
# PASS = "msfashion5932"
# DBNAME = "dd_location"
# PORT = "3306"

#   host: '35.234.6.247',
#     database: 'postgres',
#     user: 'postgres',
#     password: 'ezmealadmin'

HOST = "35.234.6.247"
USER = "postgres"
PASS = "ezmealadmin"
DBNAME = "postgres"
PORT = "5432"

class DbDataset(object):

    @staticmethod
    def estanblishConn():
        db = psycopg2.connect(database=DBNAME, user = USER, password = PASS, host = HOST, port = PORT)
        return db

    @staticmethod
    def estanblishConnMysql():
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
                        VALUES ('%s', '%s', '%s', '%s');"""
                        % (str(items['marketid'][index]),items['nickname'][index],(items['addr'][index]),(items['city'][index])))
            print('sqlQuery',sqlQuery)
            sqlQuery = cursor.execute(sqlQuery)
            db.commit()

        cursor.close()

    @staticmethod
    def datasetInsertShopMysql(items):
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
                        % (str(items['marketid'][index]),items['nickname'][index],(items['addr'][index]),(items['city'][index])))

            sqlQuery = cursor.execute(sqlQuery)
            db.commit()

        cursor.close()
   
