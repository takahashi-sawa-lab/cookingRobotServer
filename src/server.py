from collections import deque
from flask import Flask, request
import inter_objects
from flask_httpauth import HTTPBasicAuth
import json
from flask import Flask, jsonify

app = Flask(__name__) 
auth = HTTPBasicAuth()

users = {
    "user_name": "password123",
}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None



orderQueue = deque()

@app.route('/')
def show_usage():
    return "Hello World. TODO: show USAGE"



@app.route('/order/input', methods=['POST'])  
def input_order(): # Input to googlehome
     @auth.login_required
     def index():
         return "Hello, World" 

         if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
            preorder = request.get_json()
            target = preorder['target']
            action = preorder['action']   
            how = preorder['how']
            to = preorder['to'] 
     
            order = inter_objects.Order(target,action,how,to)
            orderQueue.append(order)
       
            @app.route('/hello')
            def jesonify():
                return jsonify({'message': 'order.target,order.action,order.how,order.to'})
 
         else:
            err = "error"
            return err


@app.route('/order/output',methods=['GET'])
def output_order(): # output to robot
    @auth.login_required
    def index():
        return "Hello, World" 
        if orderQueue:
            latestOrder = orderQueue.popleft()
            order_text = { "target": latestOrder.target, "action": latestOrder.action, "to": latestOrder.to, "how": latestOrder.how}
            json_text = json.dumps(order_text)
         
            @app.route('/hello')
            def jesonify():
                return jsonify({'message': 'json_text'})
        
        else:
            return "order is empty"



if __name__ == '__main__':
    app.run(debug=True)
