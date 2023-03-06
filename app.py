
from flask import Flask, render_template, request
from logic.getsysinfo import sys_name, database_check, insert_data

apk = Flask(__name__)


@apk.route('/')
def root():
    return render_template('login.html')


@apk.route('/validation', methods=['POST', 'GET'])
def validation():
    uname = request.form['name']
    password = request.form['pass']
    value = database_check(uname, password)
    if value == 1:
        return render_template('index.html')
    else:
        # return redirect('/')
        return render_template('invalid.html')


@apk.route('/home', methods=['POST', 'GET'])
def load_home():
    system_info = request.form['select_val']
    response = sys_name(system_info)
    if system_info == "allinfo":
        return render_template('all_info_response.html', result=response)
    else:
        return render_template('response.html', result=response)


@apk.route('/new')
def new_register():
    return render_template('register.html')


@apk.route('/register', methods=['POST', 'GET'])
def register():
    name = request.form['name']
    password = request.form['pass']
    age = request.form['age']
    gender = request.form['select_gender']
    response = insert_data(name, password, age, gender)
    if response == 1:
        return render_template('login.html')
    else:
        return render_template('register.html')


if __name__ == '__main__':
    apk.run(debug=True, port=5001)

