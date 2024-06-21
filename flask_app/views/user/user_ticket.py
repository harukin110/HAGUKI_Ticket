from flask import render_template, flash, request, redirect, session,url_for
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.staff import read_staff_staff_account
from flask_app.views.staff.common.staff_common import is_staff_login

#myチケット一覧画面
@app.route("/my_ticket", methods=["GET", "POST"])
# @is_staff_login
def my_ticket():
    return render_template("user/ticket_manage/my_ticket.html")



#myチケット詳細画面
@app.route("/ticket_info", methods=["GET", "POST"])
@is_staff_login
def ticket_detail():
    return render_template("user/ticket_manage/ticket_info.html")


#myチケットキャンセル
@app.route("/ticket_cancel", methods=["GET", "POST"])
@is_staff_login
def ticket_cancel():
    return render_template("user/ticket_manage/cancel/ticket_cancel.html")


#myチケットキャンセル完了
@app.route("/ticket_cancel_comp", methods=["GET", "POST"])
@is_staff_login
def ticket_cancel_comp():
    return render_template("user/ticket_manage/cancel/ticket_cancel_comp.html")
