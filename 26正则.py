from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return{"code":0,"msg":"登录成功","date":[]}

@app.route('/login',methods=["post"])
def user_login():
    username = request.json.get("username")
    type = request.args.get("type")
    print("11212121212")
    return"{},{}".format(username,type)

if __name__ == '__main__':
    app.run(host='0.0.0.0',post=5000,debug=True)