from fastapi import FastAPI
from app.api import teams, matches

app = FastAPI(title="Football Simulator API")

app.include_router(teams.router, prefix="/teams", tags=["Teams"])
app.include_router(matches.router, prefix="/matches", tags=["Matches"])