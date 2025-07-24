from __future__ import annotations
from src.backend.utils.dataStructures.DoubleLinkedCircularList import DoubleLinkedCircularList
from src.backend.models.team.TeamSeason import TeamSeason

from typing import TYPE_CHECKING, Optional, Any
if TYPE_CHECKING:
    from src.backend.models.team.Team import Team
    from backend.models.Matchweek import Matchweek
    from src.backend.models.league.League import League
    from src.backend.models.season.Season import Season

class LeagueSeason:
    def __init__(self, id: str, league: League, season: Season):
        self.id = id
        self.league = league
        self.season = season
        self.teams: DoubleLinkedCircularList["Team"] = DoubleLinkedCircularList["Team"]()
        self.table: DoubleLinkedCircularList["Team"] = DoubleLinkedCircularList["Team"]()
        self.matchweeks: DoubleLinkedCircularList["Matchweek"] = DoubleLinkedCircularList["Matchweek"]()

    def add_matchweek(self, matchweek: Matchweek) -> bool:
        try:
            if self.matchweeks.find_node(lambda mw: mw.id == matchweek.id):
                print(f"Matchweek {matchweek.matchweek} already exists in league season {self.id}")
                return False
            self.matchweeks.add(matchweek)
            print(f"Matchweek {matchweek.matchweek} added to league season {self.id}: {matchweek}")
            return True
        except Exception as e:
            print(f"AN ERROR OCCURRED WHILE ADDING THE MATCHWEEK: {e}")
            return False

    def add_team(self, team: Team) -> bool:
        try:
            #Verificamos que el equipo no haya sido añadido antes
            if self.teams.find_node(lambda x: x.id.lower() == team.id.lower()) is not None:
                print(f"The team {team.name} has already been added to the season {self.season.year} of the {self.league.name}")
                return False
            
            #Verificamos que se añada el equipo a la lista de equipos de LeaguSeason
            if self.teams.add(team):
                print(f"The team {team.name} has succesfully been added to the season {self.season.year} of the {self.league.name}")
            else:
                print(f"An error occurred while adding {team.name} to the league season {self.id}")
                return False
            
            #Verificamos que se añada la temporada a la lista de temporadas del equipo
            if team.add_season(TeamSeason(self.id, team, self.season)):
                print(f"The season {self.season.year} has succesfully been added to the team {team.name}")
            else:
                print(f"An error occurred while adding season {self.season.year} to {team}")
                return False
            print(f"The process to add {team.name} to the league season {self.id} finished succesfully")
            return True
        except Exception as e:
            print(f"AN ERROR OCCURRED WHILE ADDING THE TEAM {team.name} TO THE SEASON {self.season.year}: {e}")
            return False
    
    def __str__(self):
        return f"{self.league.name} season {self.season.year}"