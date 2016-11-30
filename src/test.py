from index import index
import unittest


class FlaskTestCase(unittest.TestCase):

def test(self):
        tester = app.test_client(self)
        response = tester.get('/DC2', content_type='html/text')
        self.assertTrue(b'Integra' in response.data)
        
if __name__ == '__main__':
    unittest.main()
