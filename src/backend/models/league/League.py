from __future__ import annotations
from src.backend.utils.dataStructures.DoubleLinkedCircularList import DoubleLinkedCircularList

from typing import TYPE_CHECKING, Optional, Any
if TYPE_CHECKING:
    from src.backend.models.team.Team import Team
    from backend.models.league.LeagueMatch import LeagueMatch
    from src.backend.models.league.LeagueSeason import LeagueSeason
    from src.backend.models.league.League import League

class League:
    def __init__(self, name: str, id: str, country: str):
        self.name = name
        self.id = id
        self.country = country
        self.seasons: DoubleLinkedCircularList["LeagueSeason"] = DoubleLinkedCircularList["LeagueSeason"]()

    def add_season(self, leagueSeason: LeagueSeason) -> bool:
        if self.seasons.find_node(lambda x: x.id.lower() == leagueSeason.id.lower()):
            print(f"The season {leagueSeason.id} has already been added to the league {self.name}")
            return False
        if self.seasons.add(leagueSeason):
            print(f"The season {leagueSeason.id} has succesfully been added to the league {self.name}")
            return True
        else:
            print(f"An error has ocurred while adding season {leagueSeason.id} to the league {self.name}")
            return False
