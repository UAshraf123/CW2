from index import app
import unittest


class FlaskTestCase(unittest.TestCase):

    #this ensures flask is set up without issues.
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    #this ensures that the correct page loads (homepage in this case).
    def test_index_homepage(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Welcome to JDM Cars' in response.data)

        
          
        
if __name__ == '__main__':
    unittest.main()
