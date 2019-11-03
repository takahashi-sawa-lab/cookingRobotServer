from collections import deque
from flask import Flask, request

app = Flask(__name__)

class Order():
    def __init__(self, target="", action="", how="", to=""):
        self.target = target
        self.action = action
        self.how = how
        self.to = to

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
        order = Order(target, action, how, to)
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
