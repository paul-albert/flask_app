# A very simple Flask Hello World app for you to get started with...

from datetime import datetime

from flask import Flask


app = Flask(__name__)


@app.route("/")
def main_endpoint():
    user_name = "user"
    current_date_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    return f"Main endpoint::: Hello, {user_name}! Now is {current_date_time} (UTC)"


@app.route("/first")
def first_endpoint():
    user_name = "user"
    current_date_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    return f"1st endpoint::: Hello, {user_name}! Now is {current_date_time} (UTC)"


@app.route("/second")
def second_endpoint():
    user_name = "user"
    current_date_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    return f"2nd endpoint::: Hello, {user_name}! Now is {current_date_time} (UTC)"


@app.route("/third")
def third_endpoint():
    user_name = "user"
    current_date_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    return f"3rd endpoint::: Hello, {user_name}! Now is {current_date_time} (UTC)"
