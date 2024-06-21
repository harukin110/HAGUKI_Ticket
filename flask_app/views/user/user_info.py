from flask import render_template, flash, request, redirect, session,url_for
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.staff import read_staff_staff_account
from flask_app.models.functions.customer import read_customer_customer_account
from flask_app.views.staff.common.staff_common import is_staff_login


# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()
# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()

#会員情報
@app.route("/user_info", methods=["GET", "POST"])
# @is_staff_login
def user_info():
    customer_account = session["logged_in_customer_account"] 
    mst_custemer=read_customer_customer_account(customer_account)
    print (mst_custemer)

#会員情報変更入力
@app.route("/user_info_change", methods=["GET", "POST"])
@is_staff_login
def user_info_change():
    return render_template("/user/mypage/info_change/user_info_change.html")

#会員情報変更確認
@app.route("/user_info_check", methods=["GET", "POST"])
@is_staff_login
def user_info_check():
    return render_template("/user/mypage/info_change/user_info_check.html")

#会員情報変更完了
@app.route("/user_info_comp", methods=["GET", "POST"])
@is_staff_login
def user_info_comp():
    return render_template("/user/mypage/info_change/user_info_comp.html")