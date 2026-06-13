from flask import Flask, render_template
from models import db, Project

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def dashboard():
    projects = Project.query.all()
    return render_template('dashboard.html', projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
