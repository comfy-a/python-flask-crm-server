import pymysql
from flask import current_app as app
from crm.database_config import mysql
import logging

class UserService():
    
    ## class UserService(): 사용자 서비스 클래스
    def __init__(self, logger=None):
        self.logger = logging.getLogger('User service')

    def user_get(self, name=None, age=None, gender=None):
        self.logger = logging.getLogger('사용자 조회')

        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "SELECT * FROM user WHERE 1=1"
            args = []

            if name:
                sqlQuery += " AND name LIKE %s"
                args.append("%" + name + "%")
            if age:
                sqlQuery += " AND age = %s"
                args.append(age)
            if gender:
                sqlQuery += " AND gender = %s"
                args.append(gender)

            cursor.execute(sqlQuery, args)
            result = cursor.fetchall()

            response = []

            if cursor.rowcount is 0:
                return response

            for row_data in result:
                res_user = {}
                addr = {}
                addr['zip_no'] = row_data['zip_no']
                addr['base_addr'] = row_data['base_addr']
                addr['detail_addr'] = row_data['detail_addr']

                res_user['id'] = row_data['id']
                res_user['name'] = row_data['name']
                res_user['age'] = row_data['age']
                res_user['gender'] = row_data['gender']
                res_user['addr'] = addr

                response.append(res_user)
            
            return response
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def user_post(self, user):
        self.logger = logging.getLogger('사용자 등록')
        
        name = user['name']
        age = user['age']
        gender = user['gender']
        zip_no = user['addr']['zip_no']
        base_addr = user['addr']['base_addr']
        detail_addr = user['addr']['detail_addr']

        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO user (name, age, gender, zip_no, base_addr, detail_addr) VALUES (%s, %s, %s, %s, %s, %s)"
            bindData = (name, age, gender, zip_no, base_addr, detail_addr)
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
        name = user['name']
        age = user['age']
        gender = user['gender']
        zip_no = user['addr']['zip_no']
        base_addr = user['addr']['base_addr']
        detail_addr = user['addr']['detail_addr']

        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "UPDATE user SET name=%s, age=%s, gender=%s, zip_no=%s, base_addr=%s, detail_addr=%s WHERE id=%s"
            bindData = (name, age, gender, zip_no, base_addr, detail_addr, user_id)
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
