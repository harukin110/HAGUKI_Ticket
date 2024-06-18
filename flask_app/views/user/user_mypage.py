from flask import render_template, flash, request, redirect, session,url_for
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.staff import read_staff_staff_account
from flask_app.views.staff.common.staff_common import is_staff_login

# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()
# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()

# マイページの表示
@app.route("/user_user_mypage", methods=["GET", "POST"])
@is_staff_login
def mypage():
    return render_template("/user/user_mypage.html")##変更が必要



#myチケット一覧画面
@app.route("/user_user_my_ticket", methods=["GET", "POST"])
@is_staff_login
def my_ticket():
    return render_template("user/user_ticket.html")##変更が必要


#myチケット詳細画面
@app.route("/user_user_my_ticket", methods=["GET", "POST"])
@is_staff_login
def ticket_detail():
    return render_template("user/user_ticket_detail.html")##変更が必要


