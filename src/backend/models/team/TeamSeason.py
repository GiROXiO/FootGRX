from __future__ import annotations
from src.backend.utils.dataStructures.DoubleLinkedCircularList import DoubleLinkedCircularList

from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from src.backend.models.team.Team import Team
    from backend.models.season.Season import Season
    from backend.models.team.TeamMatch import TeamMatch

class TeamSeason:
    def __init__(self, id: str, team: "Team", season: "Season"):
        self.id = id
        self.team = team
        self.season = season
        
        #Initialize statistics
        self.total_goals_scored = 0 
        self.total_goals_received = 0
        self.total_corners_taken = 0
        self.total_corners_against = 0
        self.total_yellow_cards = 0
        self.total_red_cards = 0
        self.total_wins = 0
        self.total_draws = 0
        self.total_losses = 0
        self.total_leaguepoints = 0
        self.matches: DoubleLinkedCircularList["TeamMatch"] = DoubleLinkedCircularList["TeamMatch"]()

    def add_match(self, match: TeamMatch) -> bool:
        if self.matches.find_node(lambda x: x.id==match.id) is not None:
            print("The match has already added")
            return False
        self.matches.add(match)
        print(f"MATCH {match.id} ADDED SUCCESFULY TO {self.team.name} IN SEASON {self.id}")
        return True

    def __str__(self):
        return f"Seaon {self.season.year} of the team {self.team.name}"