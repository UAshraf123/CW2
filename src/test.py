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
        
    #this ensures that the correct page loads (DC2 page in this case).
    def test_index_DC2(self):
        tester = app.test_client(self)
        response = tester.get('/DC2', content_type='html/text')
        self.assertTrue(b'Honda Integra DC2 (year 96-00)' in response.data)
        
    #this ensures that the correct page loads (DC5 page in this case).
    def test_index_DC5(self):
        tester = app.test_client(self)
        response = tester.get('/DC5', content_type='html/text')
        self.assertTrue(b'Honda Integra DC5 (year 01-06)' in response.data)      
        
    #this ensures that the correct page loads (Supra page in this case).
    def test_index_Supra(self):
        tester = app.test_client(self)
        response = tester.get('/Supra', content_type='html/text')
        self.assertTrue(b'Toyota Supra (year 93-02)' in response.data)
        

        
          
        
if __name__ == '__main__':
    unittest.main()
