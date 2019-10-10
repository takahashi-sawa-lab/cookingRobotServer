import unittest
import requests

url = 'http://localhost:9999/'

class TestServer(unittest.TestCase):
    def test_index(self):
        response = requests.get(url)
        response_text = response.text
        answer = 'hello world'
        self.assertEqual(answer, response_text)

if __name__ == '__main__':
    unittest.main()
