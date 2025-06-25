from fastapi import FastAPI
from projects import projects_router
from tasks import tasks_router
from time_tracking import time_router
from team_members import team_router

app = FastAPI()

app.include_router(projects_router)
app.include_router(tasks_router)
app.include_router(time_router)
app.include_router(team_router)