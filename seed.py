from app import app
from models import db, Project

with app.app_context():
    p = Project(
        title="Exploratory Data Analysis (EDA) Project",
        description="Analyze a dataset to uncover patterns and trends.",
        due_date="22 Jun 2026",
        status="Available"
    )

    db.session.add(p)
    db.session.commit()

print("Project Added!")
