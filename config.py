import os
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '\xec\xfa\xa6\xc3\xe4%8%\xe5\xe1z\xed\x9a[\xc2\xd9\xb5\x9f\xfe}.\x13\x16\xc9'
	SQLALCHEMY_DATATBASE_URI = os.environ["DATABASE_URI"]

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mydb.db'


class DevelopmentConfig(BaseConfig):
	"""docstring for DevelopmentConfig"""
	DEBUG = True
	def __init__(self, arg):
		super(DevelopmentConfig, self).__init__()
		self.arg = arg
		
class ProductionConfig(BaseConfig):
	DEBUG = False
	"""docstring for ProductionConfig"""
	def __init__(self, arg):
		super(ProductionConfig, self).__init__()
		self.arg = arg
		