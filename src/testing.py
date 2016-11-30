from app import app
import unittest


class TestCaseOne(unittest.TestCase):

    #ensure that flask is set up without issues
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
