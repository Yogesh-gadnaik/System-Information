
from flask import Flask, render_template, request

from handlers.handlers import Load_Home_Page, Load_Root_Page

apk = Flask(__name__)


@apk.route('/')
def root():
    page_Name = Load_Root_Page()
    return render_template(page_Name)


@apk.route('/home', methods=['POST', 'GET'])
def load_home():
    if request.method == 'POST':
        system_info = request.form['select_val']
        resp = Load_Home_Page(system_info)
        if system_info == "allinfo":
            return render_template('all_info_response.html', result=resp)
        else:
            return render_template('response.html', result=resp)
    else:
        return "<html><body><h1>Error</h1></body></html>"


if __name__ == '__main__':
    apk.run(debug=True)
