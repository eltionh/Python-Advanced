from fastapi import FastAPI
from models import Developer, Project

app = FastAPI()

@app.post("/developers")
def create_developer(developer: Developer):
    return {"message": "Developer created", "developer": developer}

@app.post("/projects")
def create_project(project: Project):
    return {"message": "Project created", "developer": project}

@app.get("/projects")
def get_projects():
    sample_project = Project(
        title="Test",
        description= "This is a test project",
        languages = ["Python", "JavaScript"],
        lead_developer=Developer(name="John Doe", experience=5)

    )

    return {"projects": [sample_project]}