
import pymysql
import dbconfig as conf
import logging
import sys

logger = logging.getLogger("baseSpider")
formatter = logging.Formatter('%(asctime)s\
              %(levelname)-8s:%(message)s')
file_handler = logging.FileHandler("user-database.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

def db_connect():
    #print(conf.db_config)
    try:
        conn = pymysql.connect(host=conf.db_config['host'], port=conf.db_config['port'], user=conf.db_config['user'], password=conf.db_config['password'],
                                db=conf.db_config['db'], charset = conf.db_config['charset'])
    except:
        logger.error("Database connection failed!")
        return False
    return conn

def db_close(conn):
    if conn and conn.cursor():
        conn.cursor().close()
        conn.close()
    return True

def db_execute(sql):
    #print(sql)
    conn = db_connect()
    if conn == False:
        return False
    with conn.cursor() as cursor:
        try:
            if conn and cursor:
                cursor.execute(sql)
                conn.commit()
        except:
            logger.error("sql execution failed: " + sql)
            db_close(conn)
            return False
        result = cursor.fetchall()
    db_close(conn)
    return result
