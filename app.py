import logging
from flask import Flask, render_template, request, url_for, redirect
from vertex_prompt import run_vertex_ai

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", power_verb_list="")


@app.route('/api/powerverb', methods=['POST'])
def change_to_power_verb():
    user_input = request.form['userinput']
    power_verb_list = run_vertex_ai(user_input)
    app.logger.info(power_verb_list)
    return render_template("index.html", power_verb_list=power_verb_list)


if __name__ == "__main__":
    app.run(debug=True)
