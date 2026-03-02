from pydantic import BaseModel

class MatchBase(BaseModel):
    homeTeamId: str
    awayTeamId: str

class MatchCreate(MatchBase):
    pass

class Match(MatchBase):
    id: str
    homeScore: int = 0
    awayScore: int = 0
    status: str = "scheduled"