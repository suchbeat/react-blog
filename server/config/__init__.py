import os

config_mode = os.environ.get('WEB_SERVER', 'dev')

if config_mode == 'dev':
    from server.config.development import *
elif config_mode == 'test':
    from server.config.testing import *
else:
    from server.config.production import *