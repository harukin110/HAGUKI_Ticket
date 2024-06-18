from flask import render_template, flash, request, redirect, session
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.staff import read_staff_staff_account
from flask_app.views.staff.common.staff_common import is_staff_login

# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()
# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()


# スタッフログイン
@app.route("/user_user_signup", methods=["GET", "POST"])
def user_user_signup():
    return render_template("/user/user_signup.html")