import unittest
import requests
import json

url_usage = 'http://localhost:9999/'
url_cook = 'http://localhost:9999/cook'


class TestServer(unittest.TestCase):
    def test_usage(self):
        response = requests.get(url_usage)
        response_text = response.text
        answer = 'hello world'
        self.assertEqual(answer, response_text)


    def test_cook(self):
        response = requests.post(
            url_cook,
            json.dumps(
                {'target':'poteto', 'action':'cut', 'howto':'slice'}),
            headers={'Content-Type': 'application/json'})
        response_text = response.text
        answer = "finish"
        self.assertEqual(answer, response_text)


if __name__ == '__main__':
    unittest.main()
