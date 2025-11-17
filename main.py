from flask import Flask, render_template
from backend import create_app

app = create_app()

app = Flask(__name__, template_folder="frontend/templates",static_folder="frontend/static")

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
