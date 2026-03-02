from fastapi import APIRouter, HTTPException
from app.models.match import MatchCreate, Match
import uuid

router = APIRouter()

matches_db = {}

# CREATE
@router.post("/", response_model=Match, status_code=201)
def create_match(match: MatchCreate):
    match_id = str(uuid.uuid4())
    new_match = Match(id=match_id, **match.dict())
    matches_db[match_id] = new_match
    return new_match

# READ ALL
@router.get("/", response_model=list[Match])
def get_matches():
    return list(matches_db.values())

# READ ONE
@router.get("/{matchId}", response_model=Match)
def get_match(matchId: str):
    if matchId not in matches_db:
        raise HTTPException(status_code=404, detail="Match not found")
    return matches_db[matchId]

# DELETE
@router.delete("/{matchId}", status_code=204)
def delete_match(matchId: str):
    if matchId not in matches_db:
        raise HTTPException(status_code=404, detail="Match not found")
    del matches_db[matchId]
    return