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
        response = tester.get('/DC2/', content_type='html/text')
        self.assertTrue(b'Honda Integra DC2 (year 96-00)' in response.data)
        
    #this ensures that the correct page loads (DC5 page in this case).
    def test_index_DC5(self):
        tester = app.test_client(self)
        response = tester.get('/DC5', content_type='html/text')
        self.assertTrue(b'Honda Integra DC5 (year 01-06)' in response.data)
        
    #this ensures that the correct page loads (Supra page in this case).
    def test_index_Supra(self):
        tester = app.test_client(self)
        response = tester.get('/Supra/', content_type='html/text')
        self.assertTrue(b'Toyota Supra (year 93-02)' in response.data)
        
    #this ensures that the correct page loads (S13 page in this case).
    def test_index_S13(self):
        tester = app.test_client(self)
        response = tester.get('/S13/', content_type='html/text')
        self.assertTrue(b'Nissan S13 (year 89-95)' in response.data)
        
    #this ensures that the correct page loads (S15 page in this case).
    def test_index_S15(self):
        tester = app.test_client(self)
        response = tester.get('/S15/', content_type='html/text')
        self.assertTrue(b'Nissan S15 (year 99-02)' in response.data)
        
    #this ensures that the correct page loads (Chaser page in this case).
    def test_index_Chaser(self):
        tester = app.test_client(self)
        response = tester.get('/Chaser/', content_type='html/text')
        self.assertTrue(b'Toyota Chaser (year 96-01)' in response.data)
        
    #this ensures that the correct page loads (Map page in this case).
    def test_index_Map(self):
        tester = app.test_client(self)
        response = tester.get('/Map/', content_type='html/text')
        self.assertTrue(b'Japan on Google Maps' in response.data)
        
    #this ensures that the correct page loads (error404 page in this case).
    def test_index_404(self):
        tester = app.test_client(self)
        response = tester.get('/404/', content_type='html/text')
        self.assertTrue(b'OOPS!!!! PAGE NOT FOUND!! PLEASE RETURN TO HOMEPAGE BY CLICKING ON THE HEADER, OTHERWISE CLICK ONE OF THE TABS ABOVE =]' in response.data)
        
          
        
if __name__ == '__main__':
    unittest.main()
