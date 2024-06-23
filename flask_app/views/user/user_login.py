from flask import render_template, flash, request, redirect, session,url_for
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.customer import read_customer_customer_account
from flask_app.views.user.common.user_common import is_customer_login

# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()
# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()


# 会員ログイン
@app.route("/customer_customer_login", methods=["GET", "POST"])
def customer_customer_login():
    return render_template("/user/login/user_login.html")


# 会員ログイン処理
@app.route("/login_customer", methods=["POST"])
def login_customer():
    isLoginError = False
    customer_array = read_customer_customer_account(
        request.form["customer_account"])

    if len(customer_array) == 0:
        flash(errorMessages.w04('アカウント名'))
        isLoginError = True
    # 会員アカウントが存在するかチェック
    else:
        customer = customer_array[0]
        # パスワードが一致するかチェック
        if request.form["customer_password"] != customer.customer_password:
            flash(errorMessages.w04('アカウント名'))
            isLoginError = True

    # エラーがあればログインページに遷移
    if isLoginError:
        return render_template("/user/login/user_login.html")

    else:
        # login処理を実行する
        session["logged_in_customer"] = True
        session["logged_in_customer_account"] = customer.customer_account
        session["logged_in_customer_id"] = customer.customer_id
        session["logged_in_customer_name"] = customer.customer_name
        flash(infoMessages.i05())
        return redirect(url_for("user_user_top"))


# 会員ログアウト
@app.route("/logout_customer")
@is_customer_login
def logout_customer():
    session.pop("logged_in_customer", None)
    session.pop("logged_in_customer_account", None)
    session.pop("logged_in_customer_id", None)
    session.pop("logged_in_customer_name", None)

    flash("ログアウトしました")
    return render_template("/index.html")