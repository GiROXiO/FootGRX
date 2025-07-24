from __future__ import annotations
from src.backend.utils.dataStructures.DoubleLinkedCircularList import DoubleLinkedCircularList

from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from src.backend.models.league.LeagueSeason import LeagueSeason
    from src.backend.models.league.LeagueMatch import LeagueMatch
    from src.backend.models.team.TeamSeason import TeamSeason

class Matchweek:
    def __init__(self, id: str, league: LeagueSeason, matchweek: int):
        self.id = id
        self.league = league
        self.matchweek = matchweek
        self.matches: DoubleLinkedCircularList["LeagueMatch"] = DoubleLinkedCircularList["LeagueMatch"]()
    
    def __str__(self):
        return f"Matchweek {self.matchweek} of the league {self.league.league.name} on season {self.league.season.year}"