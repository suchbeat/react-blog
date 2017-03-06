DEBUG = True

DB_USER = 'user'
DB_PASSWORD = 'secret'
DB_HOST = 'db'
DB_NAME = 'react_blog'
DB_PORT = 3306

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}?'
    'charset=utf8'.format(user=DB_USER, password=DB_PASSWORD, host=DB_HOST,
                          port=DB_PORT, db_name=DB_NAME)
)

SECRET_KEY = 'T\xa7"\xb7\xa4\x8b+\xee\xba5-\xddh2\xa3@M"21\r\x1a\xaa\xc1'
