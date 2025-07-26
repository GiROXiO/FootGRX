from src.backend.utils.nodes.Node import Node
from src.backend.utils.dataStructures.DoubleLinkedCircularList import DoubleLinkedCircularList

from src.backend.models.league.League import League
from src.backend.models.league.LeagueSeason import LeagueSeason
from src.backend.models.league.LeagueMatch import LeagueMatch
from src.backend.models.team.Team import Team
from src.backend.models.Matchweek import Matchweek
from src.backend.models.season.Season import Season
import datetime

def main():
    #Creamos una temporada
    season2024_25 = Season("2024_25")
    
    #Creamos la Premier League
    premierLeague = League("Premier League", "PRE", "England")
    
    #Creamos la temporada 2024/25 de la Premier League
    premier2024_25 = LeagueSeason("PRE2024_25", premierLeague, season2024_25)
    
    #Añadimos la temporada 2024/25 a la temporada y a la Premier League
    season2024_25.add_league(premier2024_25)
    premierLeague.add_season(premier2024_25)
    
    #Obtenemos la temporada 2024/25 de la Premier League
    premier2024_25T = premierLeague.seasons.find_node(lambda x: x.id.lower() == "PRE2024_25".lower())
    
    if premier2024_25T:
        print(f"Se encontro la temporada {premier2024_25T.get_value().id}")
    else:
        print(f"\nERROR while searching")
    
    #Creamos los equipos de la Premier League 2024/25
    liverpool = Team("Liverpool", "LIV", "England")
    arsenal = Team("Arsenal", "ARS", "England")
    manCity = Team("Manchester City", "MCI", "England")
    chelsea = Team("Chelsea", "CHE", "England")
    newcastle = Team("Newcastle", "NEW", "England")
    astVilla = Team("Aston Villa", "AVL", "England")
    notForest = Team("Nottingham forest", "NFO", "England")
    brighton = Team("Brighton", "BHA", "England")
    bournemouth = Team("Bournemouth", "BOU", "England")
    brentford = Team("Brentford", "BRE", "England")
    fulham = Team("Fulham", "FUL", "England")
    cryPalace = Team("Crystal Palace", "CRY", "England")
    everton = Team("Everton", "EVE", "England")
    westHam = Team("West Ham", "WHU", "England")
    manUnited = Team("Manchester United", "MUN", "England")
    wolves = Team("Wolverhampton Wanderers", "WOL", "England")
    tottenham = Team("Tottenham Hotspur", "TOT", "England")
    leicester = Team("Leicester City", "LEI", "England")
    ipswich = Team("Ipswich Town", "IPS", "England")
    southampton = Team("Southampton", "SOU", "England")
    
    #Creamos las jornadas
    premier2024_25.create_matchweeks()
    
    #Añadimos los equipos a la temporada
    if premier2024_25:
        premier2024_25.add_team(liverpool)
        premier2024_25.add_team(arsenal)
        premier2024_25.add_team(manCity)
        premier2024_25.add_team(chelsea)
        premier2024_25.add_team(newcastle)
        premier2024_25.add_team(astVilla)
        premier2024_25.add_team(notForest)
        premier2024_25.add_team(brighton)
        premier2024_25.add_team(bournemouth)
        premier2024_25.add_team(brentford)
        premier2024_25.add_team(fulham)
        premier2024_25.add_team(cryPalace)
        premier2024_25.add_team(everton)
        premier2024_25.add_team(westHam)
        premier2024_25.add_team(manUnited)
        premier2024_25.add_team(wolves)
        premier2024_25.add_team(tottenham)
        premier2024_25.add_team(leicester)
        premier2024_25.add_team(ipswich)
        premier2024_25.add_team(southampton)
    
    #Probamos que todo se haya añadido correctamente en la temporada 2024/25
    #season2024_25.leagues.show()
    premierLeague.seasons.show()
    
    #print("\nAca probamos accediendo a la variable premier2024_25")
    premier2024_25.teams.show()
    
    #print("\nAca probamos accediendo directamente a la lista guardada en season2024/25")
    #season2024_25.leagues.find_node(lambda x: x.id.lower() == "PRE2024_25".lower()).get_value().#teams.show()

    #Creamos los partidos de la primera jornada de la temporada
    mw1 = premier2024_25.find_matchweeks(1).get_value()
    
    if mw1:
        premier2024_25.add_match(manUnited, fulham, mw1, datetime.date(2024, 8, 16))
        premier2024_25.add_match(ipswich, liverpool, mw1, datetime.date(2024, 8, 17))
        premier2024_25.add_match(arsenal, wolves, mw1, datetime.date(2024, 8, 17))
        premier2024_25.add_match(everton, brighton, mw1, datetime.date(2024, 8, 17))
        premier2024_25.add_match(newcastle, southampton, mw1, datetime.date(2024, 8, 17))
        premier2024_25.add_match(notForest, bournemouth, mw1, datetime.date(2024, 8, 17))
        premier2024_25.add_match(westHam, astVilla, mw1, datetime.date(2024, 8, 17))
        premier2024_25.add_match(brentford, cryPalace, mw1, datetime.date(2024, 8, 18))
        premier2024_25.add_match(chelsea, manCity, mw1, datetime.date(2024, 8, 18))
        premier2024_25.add_match(leicester, tottenham, mw1, datetime.date(2024, 8, 19))
        print("\n")
        mw1.matches.show()

if __name__ == "__main__":
    main()