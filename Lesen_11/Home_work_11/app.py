from flask import Flask, render_template
import function

candidates = function.Candidates('candidates.json')

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template('list.html', candidates=candidates.content)


@app.route("/candidate/<int:uid>/")
def candidate_by_number(uid):
    return render_template('card.html', candidate=candidates.get_candidate(uid))


@app.route("/search/<candidate_name>/")
def candidate_by_name(candidate_name):
    cnt_candidates = len(candidates.get_candidates_by_name(candidate_name))
    return render_template('search.html', cnt_candidates=cnt_candidates, candidates=candidates.get_candidates_by_name(candidate_name))


@app.route("/skill/<skill_name>/")
def candidate_by_skills(skill_name):
    cnt_candidates = len(candidates.get_candidates_by_skill(skill_name))
    return render_template('skill.html', cnt_candidates=cnt_candidates, candidates=candidates.get_candidates_by_skill(skill_name), skill_name=skill_name)


app.run(host='127.0.0.2', port=80)
