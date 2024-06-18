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
@app.route("/user_user_signup", methods=["GET", "POST"])
def user_user_signup():
    if request.methods == 'POST':
        redirect(url_for("user_signup_confirm"))
    return render_template("/user/user_signup.html")


# 新規会員登録確認画面
@app.route("/user_user_signup", methods=["GET", "POST"])
def user_user_signup():
    if request.methods == 'POST':#登録を完了が押されたら
        redirect(url_for("entry"))
    return render_template("/user/user_signup_confirm.html")##変更が必要##




