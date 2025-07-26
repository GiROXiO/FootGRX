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

    def add_match(self, match: LeagueMatch):
        try:
            if self.matches.find_node(lambda x: x.id.lower() == match.id.lower()):
                print(f"The match {match.id} has already been added to the matchweek {self.id}")
                return False
            self.matches.add(match)
            print(f"THE MATCH {match.id} WAS SUCCESFULLY ADDED TO THE MATCHWEEK {self.id}")
            return True
        except Exception as e:
            print(f"AN ERROR OCCURRED WHILE ADDING THE MATCH: {e}")
            return False

    def __str__(self):
        return f"Matchweek {self.matchweek} of the league {self.league.league.name} on season {self.league.season.year}"