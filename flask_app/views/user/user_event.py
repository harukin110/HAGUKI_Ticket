from flask import render_template, flash, request, redirect, session,url_for
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.staff import read_staff_staff_account
from flask_app.views.staff.common.staff_common import is_staff_login


# イベント詳細
@app.route("/event_info", methods=["GET", "POST"])
def event_info():
    return render_template("/user/event/event_info.html")

# イベント申込
@app.route("/event_app", methods=["GET", "POST"])
def event_app():
    return render_template("/user/event/event_app.html")

# 申込者情報入力
@app.route("/event_app_input", methods=["GET", "POST"])
def event_app_input():
    return render_template("/user/event/event_app_input.html")

# 申込者情報確認
@app.route("/event_app_check", methods=["GET", "POST"])
def event_app_check():
    return render_template("/user/event/event_app_check.html")

# 申込確認
@app.route("/event_app_comp", methods=["GET", "POST"])
def event_app_comp():
    return render_template("/user/event/event_app_comp.html")