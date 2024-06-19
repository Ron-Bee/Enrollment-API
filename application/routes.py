from application import app

from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/static/images:filename')
def static_files(filename):
   return send_from_directory(app.config['STATIC_FOLDER'], filename)