from flask import Flask, request
import control

app = Flask(__name__)

class Order():
    def __init__(self, target, action, howto):
        self.target = target
        self.action = action
        self.howto = howto


@app.route('/')
def usage():
    res = control.usage()
    return res

@app.route('/cook', methods=['POST'])
def cook():
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        preorder = request.get_json()
        target = preorder['target']
        action = preorder['action']
        howto = preorder['howto']
        order = Order(target, action, howto)
        control.cook(order)
        return "finish"
    else:
        err = "error"
        return err

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9999)
