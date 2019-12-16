import pymysql
from flask import current_app as app
from crm.database_config import mysql
import logging

class UserService():
    
    ## class UserService(): 사용자 서비스 클래스
    def __init__(self, logger=None):
        self.logger = logging.getLogger('User service')

    def user_get(self):
        self.logger = logging.getLogger('사용자 조회')

        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "SELECT * FROM user"
            cursor.execute(sqlQuery)
            response = cursor.fetchall()
            
            return response
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def user_post(self, user):
        self.logger = logging.getLogger('사용자 등록')
        
        user_name = user['name']
        age = user['age']
        gender = user['gender']

        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO user (name, age, gender) VALUES (%s, %s, %s)"
            bindData = (user_name, age, gender)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            
            return "success"
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def user_put(self, user):
        self.logger = logging.getLogger('사용자 수정')

        user_id = user['id']
        user_name = user['name']
        age = user['age']
        gender = user['gender']

        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "UPDATE user SET name=%s, age=%s, gender=%s WHERE id=%s"
            bindData = (user_name, age, gender, user_id)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            
            return "success"
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def user_delete(self, id):
        self.logger = logging.getLogger('사용자 삭제')
        
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "DELETE FROM user WHERE id=%s"
            bindData = (id)
            cursor.execute(sqlQuery, bindData)
            conn.commit()

            return "success"
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
