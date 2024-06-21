from flask import render_template, flash, request, redirect, session,url_for
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.staff import read_staff_staff_account
from flask_app.views.staff.common.staff_common import is_staff_login
from flask_app.database import db
from flask_app.models.mst_ticket import Mst_ticket
from flask_app.models.mst_event import Mst_event

#myチケット一覧画面
@app.route("/my_ticket", methods=["GET", "POST"])
@is_staff_login
def my_ticket():
    return render_template("user/ticket_manage/my_ticket.html")

#myチケット詳細画面
@app.route("/ticket_info", methods=["GET", "POST"])
@is_staff_login
def ticket_detail():
    return render_template("user/ticket_manage/ticket_info.html")

#イベントIDとチケットIDを条件に抽出し、myチケットキャンセル画面に表示
@app.route("/ticket_cancel", methods=["GET", "POST"])
@is_staff_login
def read_ticket(event_id,event_category_id):
    ticket_list = Mst_ticket.query.filter(
    Mst_ticket.event_id == event_id).all()
    from flask_app.models.mst_event import Mst_event
    return render_template("user/ticket_manage/cancel/ticket_cancel.html"),ticket_list,event

# チケットを削除し、削除完了画面を表示
@app.route("/ticket_cancel_comp", methods=["GET", "POST"])
@is_staff_login
def delete_ticket(ticket_id):
    ticket = Mst_ticket.query.get(ticket_id)
    db.session.delete(ticket)
    db.session.commit()
    return render_template("user/ticket_manage/cancel/ticket_cancel_comp.html")
