from flask import redirect, render_template, session
from flask_app.__init__ import app
from flask_app.views.user.common.user_common import is_customer_login
from flask_app.models.functions.event import  read_event, read_event_event_category, read_event_event_name


"""
# スタッフメニュー（トップページ）
@app.route("/user_user_top", methods=["GET", "POST"])
@is_customer_login
def user_user_top():
    if session["logged_in_customer"] == True:
        return render_template("/user/user_mypage.html")
    else:
        return redirect("/user/user_login.html")
"""
@app.route("/user_user_top", methods=["GET", "POST"])
def user_user_top():
    mst_event = read_event()
    mst_event_dict = []
    for event in mst_event:
        param = {'isDeletable': True,
                    'event_id': event.event_id,
                    'event_category_id': event.event_category_id,
                    'event_name': event.event_name,
                    'event_date': event.event_date,
                    'event_place': event.event_place,
                    'event_overview': event.event_overview
                    }
        mst_event_dict.append(param)
    return render_template("/user/mypage/user_mypage.html", mst_event = mst_event_dict )

@app.route("/user_user_top/event_check", methods=["GET", "POST"])
def event_check():
    return render_template("/user/event/event_app_check.html")