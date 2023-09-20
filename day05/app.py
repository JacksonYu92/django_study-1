import random
from flask import Flask, render_template

app = Flask(__name__)

# http://127.0.0.1:5000

# http://127.0.0.1:5000/index
@app.route("/index")
def index():

    name = random.choice(["上海移动","广东移动","中国移动"])

    return render_template("index.html", n1=name)

# http://127.0.0.1:5000/login
@app.route("/login")
def login():
    return "登录"

if __name__ == '__main__':
    app.run()