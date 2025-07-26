from __future__ import annotations
from src.backend.utils.dataStructures.DoubleLinkedCircularList import DoubleLinkedCircularList
import datetime

from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from src.backend.models.team.Team import Team
    from backend.models.team.TeamSeason import TeamSeason
    from models.Matchweek import Matchweek

class TeamMatch:
    def __init__(self, id: str, team: Team, rival: Team, season: TeamSeason, matchweek: Matchweek, date: datetime.date, home: bool):
        self.id = id
        self.team = team
        self.rival = rival
        self.season = season
        self.matchweek = matchweek
        self.date = date
        self.home = home
        
        #Initialize statistics
        self.goals_scored = 0 
        self.goals_received = 0
        self.corners_taken = 0
        self.corners_against = 0
        self.yellow_cards = 0
        self.red_cards = 0

    def __str__(self) -> str:
        if self.home:
            return f"{self.team.name} vs {self.rival.name}"
        else:
            return f"{self.rival.name} vs {self.team.name}"