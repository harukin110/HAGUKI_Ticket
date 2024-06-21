from flask import render_template, flash, request, redirect, session,url_for
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.staff import read_staff_staff_account
from flask_app.views.staff.common.staff_common import is_staff_login

# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()
# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()

#会員退会
@app.route("/user_unsub/delete", methods=["GET", "POST"])
# @is_staff_login
def user_delete():
    return render_template("/user/mypage/unsub/user_unsub_check.html")


#会員退会確認
@app.route("/user_unsub/delete_check", methods=["GET", "POST"])
@is_staff_login
def user_delete_check():
    return render_template("/user/mypage/unsub/user_unsub_check.html")

#会員退会完了
@app.route("/user_unsub/cmp", methods=["GET", "POST"])
# @is_staff_login
def user_comp():
    return render_template("/user/mypage/unsub/user_unsub_comp.html")