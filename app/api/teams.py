from fastapi import APIRouter, HTTPException
from app.models.team import TeamCreate, TeamUpdate, Team
import uuid

router = APIRouter()

# In-memory storage
teams_db = {}

# CREATE
@router.post("/", response_model=Team, status_code=201)
def create_team(team: TeamCreate):
    team_id = str(uuid.uuid4())
    new_team = Team(id=team_id, **team.dict())
    teams_db[team_id] = new_team
    return new_team

# READ ALL
@router.get("/", response_model=list[Team])
def get_teams():
    return list(teams_db.values())

# READ ONE
@router.get("/{teamId}", response_model=Team)
def get_team(teamId: str):
    if teamId not in teams_db:
        raise HTTPException(status_code=404, detail="Team not found")
    return teams_db[teamId]

# UPDATE
@router.put("/{teamId}", response_model=Team)
def update_team(teamId: str, team: TeamUpdate):
    if teamId not in teams_db:
        raise HTTPException(status_code=404, detail="Team not found")
    updated_team = Team(id=teamId, **team.dict())
    teams_db[teamId] = updated_team
    return updated_team

# DELETE
@router.delete("/{teamId}", status_code=204)
def delete_team(teamId: str):
    if teamId not in teams_db:
        raise HTTPException(status_code=404, detail="Team not found")
    del teams_db[teamId]
    return