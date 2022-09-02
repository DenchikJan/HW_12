from flask import Flask
import function

app = Flask(__name__)


@app.route("/")
def main_page():
    return f'<pre>{function.get_all()}</pre>'


@app.route("/candidates/<int:uid>/")
def candidate_by_number(uid):
    picture, text = function.get_by_pk(uid)
    return f'<img {picture}>,<pre>{text}</pre>'


@app.route("/skills/<x>")
def candidates_by_skills(x):
    return f'<pre>{function.get_by_skill(x)}<pre>'


app.run(host='127.0.0.2', port=80)
