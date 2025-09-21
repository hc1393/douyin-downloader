from dbutils.pooled_db import PooledDB
from pymysql import cursors
import pymysql
POOL=PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=2,
    maxcached=5,
    blocking=True,
    setsession=[],
    ping=0,
    host='127.0.0.1',port=3306,user='roothc',password='root123',db='hc'
)

def fetch_one(sql: object, params: object) -> object:
    conn=POOL.connection()
    cursor=conn.cursor(cursor=cursors.DictCursor)
    cursor.execute(sql,params)
    result=cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def fetch_all(sql,params):
    conn=POOL.connection()
    cursor=conn.cursor(cursor=cursors.DictCursor)
    cursor.execute(sql,params)
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return result