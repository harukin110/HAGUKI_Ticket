from flask import render_template, flash, request, redirect, session,url_for
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.staff import read_staff_staff_account
from flask_app.views.staff.common.staff_common import is_staff_login

# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()
# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()

#会員情報
@app.route("/user_info", methods=["GET", "POST"])
@is_staff_login
def user_info(mode):
    customer_id = request.form['customer_id']
    customer_account = request.form['customer_account']
    customer_password = request.form['customer_password']
    customer_name = request.form['customer_name']
    customer_zipcode = request.form['customer_zipcode']
    customer_address = request.form['customer_address']
    customer_phone = request.form['customer_phone']
    customer_payment = request.form['customer_payment']

    return render_template("/user/mypage/user_info.html",
                           customer_id=customer_id,
                           customer_name=customer_name,
                           customer_account=customer_account,
                           customer_password=customer_password,
                           customer_zipcode=customer_zipcode,
                           customer_address=customer_address,
                           customer_phone=customer_phone,
                           customer_payment=customer_payment,
                           mode=mode)

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