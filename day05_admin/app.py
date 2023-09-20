from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/do/register")
def do_register():
    username = request.args.get('user')
    password = request.args.get('pwd')
    gender = request.args.get('gender')
    city = request.args.get('city')
    hobby = request.args.getlist('hobby')
    more = request.args.get('more')

    line = "{}|{}|{}\n".format(username,password,gender)

    file_object = open("db.txt", mode='a', encoding='utf-8')
    file_object.write(line)
    file_object.close()

    # return "执行注册"
    return redirect("/user/list")

@app.route('/user/list')
def user_list():
    data_list = []
    file_object = open("db.txt", mode='r', encoding='utf-8')
    for line in file_object:
        line = line.strip()
        data_list.append(line)
    file_object.close()

    data_list_list = []
    file_object = open("db.txt", mode='r', encoding='utf-8')
    for line in file_object:
        line = line.strip()
        data_list_list.append(line.split("|"))
    file_object.close()
    return render_template('user_list.html', v1=data_list, v2=data_list_list)

if __name__ == '__main__':
    app.run()