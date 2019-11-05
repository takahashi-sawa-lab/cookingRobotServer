from collections import deque
from flask import Flask, request
import inter_objects

app = Flask(__name__)

orderQueue = deque()

@app.route('/')
def show_usage():
    return "Hello World. TODO: show USAGE"

@app.route('/order/input', methods=['POST'])
def input_order():
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        preorder = request.get_json()
        target = preorder['target']
        action = preorder['action']
        how = preorder['how']
        to = preorder['to']
        order = inter_objects.Order(target, action, how, to)
        orderQueue.append(order)
        return "finish input order"
    else:
        err = "error"
        return err

@app.route('/order/output', methods=['GET'])
def output_order():
    if orderQueue:
        latestOrder = orderQueue.popleft()
        return "latest order output"
    else:
        return "order is empty"

if __name__ == '__main__':
    app.run(debug=True)
