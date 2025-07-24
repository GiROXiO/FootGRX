from __future__ import annotations
from src.backend.utils.dataStructures.DoubleLinkedCircularList import DoubleLinkedCircularList

from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from src.backend.models.league.League import League
    from src.backend.models.league.LeagueMatch import LeagueMatch
    from src.backend.models.team.TeamSeason import TeamSeason

class Team:
    def __init__(self, name: str, id: str, country: str):
        self.name = name
        self.id = id
        self.country = country
        self.seasons: DoubleLinkedCircularList["TeamSeason"] = DoubleLinkedCircularList["TeamSeason"]()

    def add_season(self, teamSeason: TeamSeason) -> bool:
        try:
            if self.seasons.find_node(lambda x: x.id.lower() == teamSeason.id.lower()):
                print(f"The season {teamSeason.id} has already added to this team")
                return False
            self.seasons.add(teamSeason)
            print(f"The season {teamSeason.id} has succesfully been added to {self.name}")
            return True
        except Exception as e:
            print(f"AN ERROR OCCURRED WHILE ADDING THE SEASON {teamSeason.season.year} TO THE TEAM {self.name}: {e}")
            return False

    def __str__(self) -> str:
        return f"Team {self.name} (ID: {self.id}) in {self.country}"
