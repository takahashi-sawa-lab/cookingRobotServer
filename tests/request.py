import unittest
import requests
import json

url_usage = 'http://localhost:5000/'
url_order_input= 'http://localhost:5000/order/input'
url_order_output= 'http://localhost:5000/order/output'


class TestServer(unittest.TestCase):
    def test_usage(self):
        response = requests.get(url_usage)
        response_text = response.text
        answer = "Hello World. TODO: show USAGE"
        self.assertEqual(answer, response_text)

    def test_order_io(self):
        response = requests.post(
            url_order_input,
            json.dumps(
                {'target':'poteto', 'action':'cut', 'how':'slice', 'to': ''}),
            headers={'Content-Type': 'application/json'})
        response_text = response.text
        answer = "finish input order"
        self.assertEqual(answer, response_text)
        response = requests.get(url_order_output)
        response_text = response.text
        answer = "latest order output"
        self.assertEqual(answer, response_text)
        response = requests.get(url_order_output)
        response_text = response.text
        answer = "order is empty"
        self.assertEqual(answer, response_text)

if __name__ == '__main__':
    unittest.main()
