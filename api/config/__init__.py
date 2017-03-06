import os

config_mode = os.environ.get('WEB_SERVER', 'dev')

if config_mode == 'dev':
    from config.development import *
elif config_mode == 'test':
    from config.testing import *
else:
    from config.production import *