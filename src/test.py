from index import index
import unittest


class FlaskTestCase(unittest.TestCase):

    #ensure that flask is set up correctly
    def test_index(self):
        tester = index.test_client(self)
        response = tester.get('/index', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
