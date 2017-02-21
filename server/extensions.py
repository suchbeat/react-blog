from flask_bcrypt import Bcrypt
from flask_jwt import JWT
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()
jwt = JWT()