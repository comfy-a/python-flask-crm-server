from flaskext.mysql import MySQL

mysql = MySQL()

class DatabaseConfig():
    
    def __init__(self, flask_app):
        flask_app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
        flask_app.config['MYSQL_DATABASE_USER'] = 'root'
        flask_app.config['MYSQL_DATABASE_PASSWORD'] = 'p@ssw0rd'
        flask_app.config['MYSQL_DATABASE_DB'] = 'crm'
        mysql.init_app(flask_app)