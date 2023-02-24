
from flask import Flask, render_template, request
from logic.getsysinfo import sys_name


apk = Flask(__name__)


@apk.route('/')
def root():
    return render_template('index.html')


@apk.route('/home', methods=['POST', 'GET'])
def load_home():
    system_info = request.form['select_val']
    response = sys_name(system_info)
    if system_info == "allinfo":
        return render_template('all_info_response.html', result=response)
    else:
        return render_template('response.html', result=response)


if __name__ == '__main__':
    apk.run(debug=True,port=1999)
