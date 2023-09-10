import requests

if __name__ == "__main__":
    #r = requests.get("https://api.the-odds-api.com/v4/sports/soccer_epl/odds/?apiKey=7703d0f1893451885704e2a99245bff5&regions=us&markets=h2h&oddsFormat=decimal")

    
    leagues = ["soccer_argentina_primera_division", "soccer_australia_aleague", "soccer_austria_bundesliga", "soccer_belgium_first_div", 
               "soccer_chile_campeonato", "soccer_conmebol_copa_libertadores", "soccer_denmark_superliga", "soccer_efl_champ", 
               "soccer_england_league1", "soccer_england_league2", "soccer_epl", "soccer_fa_cup", "soccer_france_ligue_one", 
               "soccer_france_ligue_two", "soccer_germany_bundesliga", "soccer_germany_bundesliga2", "soccer_germany_liga3", 
               "soccer_greece_super_league", "soccer_italy_serie_a", "soccer_italy_serie_b", "soccer_japan_j_league", "soccer_korea_kleague1",
               "soccer_league_of_ireland", "soccer_mexico_ligamx", "soccer_netherlands_eredivisie", "soccer_norway_eliteserien", 
               "soccer_poland_ekstraklasa", "soccer_portugal_primeira_liga", "soccer_spain_la_liga", "soccer_spain_segunda_division",
               "soccer_spl", "soccer_sweden_allsvenskan", "soccer_sweden_superettan", "soccer_switzerland_superleague",
               "soccer_turkey_super_league", "soccer_uefa_champs_league", "soccer_uefa_europa_conference_league",
               "soccer_uefa_europa_league", "soccer_uefa_nations_league", "soccer_usa_mls"]
    
    canBookies = ["sport888", "leovegas", "draftkings", "pointsbetus", "unibet", "fanduel", "betmgm"]

    maxHomeWin = 0
    maxHomeBookie = ""

    maxAwayWin = 0
    maxAwayBookie = ""

    maxDraw = 0
    maxDrawBookie = ""
    
    printed = False
    Filter = True # if betfair is filtered
    #leagues = ["soccer_epl"]
    for league in leagues:
        url = "https://api.the-odds-api.com/v4/sports/%s/odds/?apiKey=7703d0f1893451885704e2a99245bff5&regions=us&markets=h2h&oddsFormat=decimal" %(league)
        r = requests.get(url)
        a = r.json()
        for games in a: 
            for bookmakers in games["bookmakers"]:
                #print(bookmakers)
                if (Filter or bookmakers["title"] != "Betfair"):
                    if (maxHomeWin < bookmakers["markets"][0]["outcomes"][0]["price"]):
                        maxHomeBookie = bookmakers["title"]
                        maxHomeWin = bookmakers["markets"][0]["outcomes"][0]["price"]

                    if (maxAwayWin < bookmakers["markets"][0]["outcomes"][1]["price"]):
                        maxAwayBookie = bookmakers["title"]
                        maxAwayWin = bookmakers["markets"][0]["outcomes"][1]["price"]

                    if (maxDraw < bookmakers["markets"][0]["outcomes"][2]["price"]):
                        maxDrawBookie = bookmakers["title"]
                        maxDraw = bookmakers["markets"][0]["outcomes"][2]["price"]
            
                #print(a["description"])
            if ((1 - ((1 / maxHomeWin) +  (1 / maxAwayWin) +  (1 / maxDraw))) * 100 > 0):
                print("%s vs %s" %(bookmakers["markets"][0]["outcomes"][0]["name"], bookmakers["markets"][0]["outcomes"][1]["name"]))
                print("Return: %s%s" %(round((1 - ((1 / maxHomeWin) +  (1 / maxAwayWin) +  (1 / maxDraw))) * 100, 2), "%"))
                print("Home%sAway%sDraw" %(" " * (len(maxHomeBookie) + 4)," " * (len(maxAwayBookie) + 4)))
                print("%s: %s | %s: %s | %s: %s \n" %(maxHomeBookie, maxHomeWin, maxAwayBookie, maxAwayWin, maxDrawBookie, maxDraw))
                #if ((maxHomeBookie in canBookies) and (maxAwayBookie in canBookies) and (maxDrawBookie in canBookies)):
                 #   print("Not in Canada")
            
            maxHomeWin = 0
            maxAwayWin = 0
            maxDraw = 0
            maxHomeBookie = ""
            maxAwayBookie = ""
            maxDrawBookie = ""

    '''
    url = "https://api.the-odds-api.com/v4/sports/soccer/odds/?apiKey=7703d0f1893451885704e2a99245bff5&regions=us&markets=h2h&oddsFormat=decimal"
    r = requests.get(url)
    a = r.json()
    for games in a: 
        for bookmakers in games["bookmakers"]:
            #print(bookmakers)
            if (Filter or bookmakers["title"] != "Betfair"):
                if (maxHomeWin < bookmakers["markets"][0]["outcomes"][0]["price"]):
                    maxHomeBookie = bookmakers["title"]
                    maxHomeWin = bookmakers["markets"][0]["outcomes"][0]["price"]

                if (maxAwayWin < bookmakers["markets"][0]["outcomes"][1]["price"]):
                    maxAwayBookie = bookmakers["title"]
                    maxAwayWin = bookmakers["markets"][0]["outcomes"][1]["price"]

                if (maxDraw < bookmakers["markets"][0]["outcomes"][2]["price"]):
                    maxDrawBookie = bookmakers["title"]
                    maxDraw = bookmakers["markets"][0]["outcomes"][2]["price"]
            
                #print(a["description"])
        if ((1 - ((1 / maxHomeWin) +  (1 / maxAwayWin) +  (1 / maxDraw))) * 100 > 0):
            print("%s vs %s" %(bookmakers["markets"][0]["outcomes"][0]["name"], bookmakers["markets"][0]["outcomes"][1]["name"]))
            print("Return: %s%s" %(round((1 - ((1 / maxHomeWin) +  (1 / maxAwayWin) +  (1 / maxDraw))) * 100, 2), "%"))
            print("Home%sAway%sDraw" %(" " * (len(maxHomeBookie) + 4)," " * (len(maxAwayBookie) + 4)))
            print("%s: %s | %s: %s | %s: %s \n" %(maxHomeBookie, maxHomeWin, maxAwayBookie, maxAwayWin, maxDrawBookie, maxDraw))
            #if ((maxHomeBookie in canBookies) and (maxAwayBookie in canBookies) and (maxDrawBookie in canBookies)):
             #   print("Not in Canada")
            
        maxHomeWin = 0
        maxAwayWin = 0
        maxDraw = 0
        maxHomeBookie = ""
        maxAwayBookie = ""
        maxDrawBookie = ""
    '''

