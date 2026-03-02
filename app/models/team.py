from pydantic import BaseModel
from typing import Optional

class TeamBase(BaseModel):
    name: str
    league: Optional[str] = None
    attackRating: float
    defenseRating: float
    midfieldRating: float
    formScore: Optional[float] = 0
    externalRanking: Optional[float] = 0

class TeamCreate(TeamBase):
    pass

class TeamUpdate(TeamBase):
    pass

class Team(TeamBase):
    id: str