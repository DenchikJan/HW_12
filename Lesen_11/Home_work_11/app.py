from flask import Flask
import function

candidates = function.Candidates('candidates.json')

app = Flask(__name__)


@app.route("/")
def main_page():
    text = ''
    for candidate in candidates.content:
        text += f"""<p><a href="/candidate/{candidate['id']}">{candidate['name']}</a></p>"""

    return f'<h1>Все кандидаты</h1>{text}'


@app.route("/candidate/<int:uid>/")
def candidate_by_number(uid):
    candidate = candidates.get_candidate(uid)
    return f"""
<h1>{candidate['name']}</h1>
<p>{candidate['position']}</p>
<img src="{candidate['picture']}" width=200/>
<p>{candidate['skills']}</p>
"""


@app.route("/search/<candidate_name>/")
def candidate_by_name(candidate_name):
    text = ''
    for candidate in candidates.get_candidates_by_name(candidate_name):
        text += f"""<p><a href="/candidate/{candidate['id']}">{candidate['name']}</a></p>"""

    return f'<h1>Найдено кандидатов {len(candidates.get_candidates_by_name(candidate_name))}</h1>{text}'


@app.route("/skill/<skill_name>/")
def candidate_by_skills(skill_name):
    text = ''
    for candidate in candidates.get_candidates_by_skill(skill_name):
        text += f"""<p><a href="/candidate/{candidate['id']}">{candidate['name']}</a></p>"""

    return f'<h1>Найдено со скиллом {skill_name}: {len(candidates.get_candidates_by_skill(skill_name))}</h1>{text}'


app.run(host='127.0.0.2', port=80)
