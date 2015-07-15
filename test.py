from app import app
import unittest

class My_ProjTest(unittest.TestCase):

	#to ensure flask is working correctly
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	#ensuring login page loads correctly
	def test_login_page(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertTrue(b'Login Below' in response.data)

	#ensures login behaves correctly
	#ensures logout
if __name__ == '__main__':
	unittest.main()