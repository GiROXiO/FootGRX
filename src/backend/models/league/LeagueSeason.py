from __future__ import annotations
from src.backend.utils.dataStructures.DoubleLinkedCircularList import DoubleLinkedCircularList
from src.backend.models.team.TeamSeason import TeamSeason
from src.backend.models.Matchweek import Matchweek
from src.backend.models.league.LeagueMatch import LeagueMatch
from src.backend.models.team.TeamMatch import TeamMatch

from typing import TYPE_CHECKING, Optional, Any
if TYPE_CHECKING:
    from src.backend.models.team.Team import Team
    from src.backend.models.league.League import League
    from src.backend.models.season.Season import Season
    from src.backend.models.Matchweek import Matchweek
    from src.backend.models.league.LeagueMatch import LeagueMatch
    from src.backend.models.team.TeamMatch import TeamMatch

class LeagueSeason:
    def __init__(self, id: str, league: League, season: Season):
        self.id = id
        self.league = league
        self.season = season
        self.teams: DoubleLinkedCircularList["Team"] = DoubleLinkedCircularList["Team"]()
        self.table: DoubleLinkedCircularList["Team"] = DoubleLinkedCircularList["Team"]()
        self.matchweeks: DoubleLinkedCircularList["Matchweek"] = DoubleLinkedCircularList["Matchweek"]()

    def create_matchweeks(self) -> bool:
        try:
            for i in range(1,39):
                id = f"{self.league.id}{self.season.year}MW{i:02}"
                self.add_matchweek(Matchweek(id, self, i))
            print(f"MATCHWEEKS CREATED SUCCESFULLY")
            return True
        except Exception as e:
            print(f"AN ERROR OCCURRED WHILE THE CREATION OF MATCHWEEKS: {e}")
            return False

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

    def add_match(self, home: Team, away: Team, matchweek: Matchweek, date: datetime.date) -> bool:
        try:
            #Verificamos que el matchweek exista en la LeagueSeason
            if self.matchweeks.find_node(lambda x: x.id == matchweek.id) is None:
                print(f"The matchweek {matchweek.id} does not exist in this season")
                return False
            
            #Creamos el LeagueMatch
            id = f"{matchweek.id}_{home.id}x{away.id}"
            match: LeagueMatch = LeagueMatch(id, home, away, self, matchweek, date)
            
            #Verificamos que el Match no haya sido añadido ya a la Matchweek
            if self.matchweeks.find_node(lambda x: x.id == matchweek.id).get_value().matches.find_node(lambda x: x.id == match.id):
                print(f"The match {match.id} has already been added to the matchweek {matchweek.id}")
                return False
            
            if self.matchweeks.find_node(lambda x: x.id == matchweek.id).get_value().add_match(match):
                print(f"THE MATCH {match.id} WAS SUCCESFULLY ADDED TO MATCHWEEK {matchweek.id}")
            else:
                print(f"THE MATCH {match.id} COULD NOT BE ADDED TO MATCHWEEK {matchweek.id}")
                return False
            
            #Creamos los TeamMatch para cada equipo
            home_match = TeamMatch(id, home, away, home.seasons.find_node(lambda x: x.id == self.id).get_value(), matchweek, date, True)
            away_match = TeamMatch(id, away, home, away.seasons.find_node(lambda x: x.id == self.id).get_value(), matchweek, date, False)
            
            #Añadimos los partidos a sus equipos
            if not home.seasons.find_node(lambda x: x.id == self.id).get_value().add_match(home_match):
                print(f"COULD NOT ADD MATCH {home_match.id} TO {home.name}")
                return False
            if not away.seasons.find_node(lambda x: x.id == self.id).get_value().add_match(away_match):
                print(f"COULD NOT ADD MATCH {away_match.id} TO {away.name}")
                return False
            
            #Finalizamos el proceso
            print(f"THE PROCESS TO CREATE AND ADD MATCH {id} FINISH SUCCESFULLY")
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
            print(f"THE PROCESS TO ADD {team.name} TO THE LEAGUE SEASON {self.id} FINISHED SUCCESFULLY")
            return True
        except Exception as e:
            print(f"AN ERROR OCCURRED WHILE ADDING THE TEAM {team.name} TO THE SEASON {self.season.year}: {e}")
            return False

    def find_matchweeks(self, index: int):
        matchweek = self.matchweeks.find_node(lambda x: x.matchweek == index)
        if matchweek is not None:
            return matchweek
        
        print(f"MATCHWEEK NOT FOUNDED")
        return None

    def __str__(self):
        return f"{self.league.name} season {self.season.year}"