import unittest

from run import app


class ViewTestCases(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_index_should_return_200(self):
        """ Tests GET / """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_register_should_return_200(self):
        """ Tests GET / """
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_about_should_return_200(self):
        """ Tests GET / """
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
