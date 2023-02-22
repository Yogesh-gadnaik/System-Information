

from flask import Flask, request, render_template, redirect

apk = Flask(__name__)


@apk.route('/')
def loadPage():
    return render_template('index.html')


@apk.route('/home', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        system_info = request.form['select_val']
        from main import sys_name
        response = sys_name(system_info)
        if system_info == "allinfo":
            return render_template('all_info_response.html', result=response)
        else:
            return render_template('response.html', result=response)
    else:
        return "<html><body><h1>Error</h1></body></html>"


if __name__ == '__main__':
    apk.run(debug=True)
