from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Callable, Any
import datetime

if TYPE_CHECKING:
    from src.backend.models.league.League import League
    from src.backend.models.team.Team import Team
    from src.backend.models.league.LeagueSeason import LeagueSeason
    from src.backend.models.Matchweek import Matchweek

class LeagueMatch:
    def __init__(self, id: str, home: Team, away: Team, season: LeagueSeason, matchweek: Matchweek, date: datetime.date):
        self.id = id
        self.home = home
        self.away = away
        self.season = season
        self.matchweek = matchweek
        self.date = date
        
        #Initialize statistics
        self.home_goals = 0
        self.away_goals = 0
        self.home_corners = 0
        self.away_corners = 0
        self.home_yc = 0
        self.away_yc = 0
        self.home_rc = 0
        self.away_rc = 0

    def update_statistics(self, score1: int, score2: int):
        self.score1 = score1
        self.score2 = score2

    def __str__(self) -> str:
        return f"{self.home.name} vs {self.away.name}"

