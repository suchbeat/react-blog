import os

from flask import Flask

from server.extensions import cors, db


class Application(object):

    def __init__(self, config=None):
        self.config = config
        self.app = Flask(__name__, template_folder='../templates', static_folder='../static')
        self.configure_app()
        self.configure_extensions()
        self.configure_routes()

    def configure_app(self):
        self.app.config.from_object('server.config')
        if self.config is not None:
            self.app.config.from_object(self.config)

        for key, val in self.app.config.iteritems():
            self.app.config[key] = os.environ.get(key, val)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = (
            'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}?'
            'charset=utf8'.format(user=self.app.config['DB_USER'],
                                  password=self.app.config['DB_PASSWORD'],
                                  host=self.app.config['DB_HOST'],
                                  port=self.app.config['DB_PORT'],
                                  db_name=self.app.config['DB_NAME'])
        )

    def configure_extensions(self):
        self.db = db
        self.db.init_app(self.app)

        self.cors = cors
        self.cors.init_app(self.app)

    def configure_routes(self):
        self.app.url_map.strict_slashes = False

        with self.app.app_context():
            from .routes import ROUTES
            for rule, view, kwargs in ROUTES:
                self.app.add_url_rule(rule, view_func=view, **kwargs)


def create_app(config=None):
    return Application(config)
