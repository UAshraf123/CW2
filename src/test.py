from index import index
import unittest


class FlaskTestCase(unittest.TestCase):

    def test_login_page_loads(self):
        tester = index.test_client(self)
        response = tester.get('/DC2', content_type='html/text')
        self.assertTrue(b'integra' in response.data)

          
        
if __name__ == '__main__':
    unittest.main()
