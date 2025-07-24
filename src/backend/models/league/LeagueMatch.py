from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Callable, Any
if TYPE_CHECKING:
    from models.league.League import League
    from models.team.Team import Team

class LeagueMatch:
    def __init__(self, id: str,team1: Team, team2: Team, score1: int = 0, score2: int = 0):
        self.id = id
        self.team1 = team1
        self.team2 = team2
        self.score1 = score1
        self.score2 = score2
        self.league: Optional["League"] = None
        self.journey: Optional[int] = None

    def update_score(self, score1: int, score2: int):
        self.score1 = score1
        self.score2 = score2
        
    @property
    def team1(self):
        return self._team1

    @team1.setter
    def team1(self, value: Team):
        self._team1 = value

    @property
    def team2(self):
        return self._team2

    @team2.setter
    def team2(self, value: Team):
        self._team2 = value

    @property
    def score1(self):
        return self._score1

    @score1.setter
    def score1(self, value: int):
        self._score1 = value

    @property
    def score2(self):
        return self._score2

    @score2.setter
    def score2(self, value: int):
        self._score2 = value
        
    def __str__(self) -> str:
        return f"{self.team1.name} {self.score1} - {self.score2} {self.team2.name}"