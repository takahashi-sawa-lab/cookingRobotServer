from flask import Flask
import cook

app = Flask(__name__)

@app.route('/')
def index():
    res = cook.hello_world()
    return res

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9999)
