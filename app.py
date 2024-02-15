from flask import Flask, render_template, request, redirect, url_for, flash
import secrets
import re




secret_key = secrets.token_hex(16)
app = Flask(__name__, static_url_path="/static")
app.secret_key = secret_key


users = []

def is_valid_password(password):
    return len(password) >= 8

def is_valid_name(username):
    return re.match('^[a-zA-Z0-9_-]+$', username) is not None

def is_valid_email(email):
    return re.match("@", email) is not None



@app.route("/")
def chatbot():
    return render_template("bot.html")





# end def

if __name__ == "__main__":
    app.run(debug=True)
