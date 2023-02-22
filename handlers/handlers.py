from flask import request, render_template


def Load_Root_Page():
    return 'index.html'


def Load_Home_Page(system_info):
    from logic.getsysinfo import sys_name
    response = sys_name(system_info)
    return response
