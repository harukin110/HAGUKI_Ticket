from flask import render_template, flash, request, redirect, session,url_for
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.staff import read_staff_staff_account
from flask_app.views.staff.common.staff_common import is_staff_login

# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()
# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()


# 新規会員登録
@app.route("/user_signup", methods=["GET", "POST"])
def user_signup():
    if request.method == 'POST':
        redirect(url_for('user_signup_check'))
    return render_template("/user/signup/user_signup.html")


# 新規会員登録確認画面
@app.route("/user_signup_check", methods=["GET", "POST"])
def user_signup_check():

    customer_id = request.form.get('customer_id')
    customer_account = request.form.get('customer_account')
    customer_password = request.form.get('customer_password')
    customer_name = request.form.get('customer_name')
    customer_zipcode = request.form.get('customer_zipcode')
    customer_address = request.form.get('customer_address')
    customer_phone = request.form.get('customer_phone')
    customer_birth = request.form.get('customer_birth')

    return render_template("/user/signup/user_signup_check.html",
                           customer_id = customer_id,
                           customer_account = customer_account,
                           customer_password = customer_password,
                           customer_name = customer_name,
                           customer_zipcode = customer_zipcode,
                           customer_address = customer_address,
                           customer_phone = customer_phone,
                           customer_birth = customer_birth)

# 新規会員登録完了
@app.route("/user_signup_comp", methods=["GET", "POST"])
def user_signup_comp():
    return render_template("/user/signup/user_signup_comp.html")


