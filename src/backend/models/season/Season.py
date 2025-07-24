from __future__ import annotations
from src.backend.utils.dataStructures.DoubleLinkedCircularList import DoubleLinkedCircularList

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.backend.models.league.LeagueSeason import LeagueSeason

class Season:
    def __init__(self, year: str):
        self.year = year
        self.leagues: DoubleLinkedCircularList["LeagueSeason"] = DoubleLinkedCircularList["LeagueSeason"]()

    def add_league(self, leagueSeason: LeagueSeason):
        if self.leagues.find_node(lambda x: x.id.lower() == leagueSeason.id.lower()):
            print(f"The season {leagueSeason.id} has already been added to the season {self.year}")
            return False
        if self.leagues.add(leagueSeason):
            print(f"The league {leagueSeason.league.name} has succesfully been added to the season {self.year}")
            return True
        else:
            print(f"An error has ocurred while adding league {leagueSeason.league.name} to the season {self.year}")
            return False

    def __str__(self) -> str:
        return f"Season {self.year} with {self.leagues.get_size()} leagues"