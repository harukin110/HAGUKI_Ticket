from flask import redirect, render_template, session
from flask_app.__init__ import app
from flask_app.views.user.common.user_common import is_customer_login


# スタッフメニュー（トップページ）
@app.route("/user_user_top", methods=["GET", "POST"])
@is_customer_login
def user_user_top():
    if session["logged_in_customer"] == True:
        return render_template("/user/user_mypage.html")
    else:
        return redirect("/user/user_login.html")


