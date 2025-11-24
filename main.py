from flask import Flask, render_template
from backend import create_app
from backend.database.db import db   

app = create_app()



@app.route('/')
def base():
    return render_template("base.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/test-db")
def test_db():
    try:
        result = db.session.execute(db.text("SELECT NOW()")).scalar()
        return f"Database connected! Server time: {result}"
    except Exception as e:
        return f"Database error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
