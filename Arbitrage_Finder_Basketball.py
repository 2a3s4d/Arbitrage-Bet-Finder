import requests
from datetime import datetime

if __name__ == "__main__":
    #r = requests.get("https://api.the-odds-api.com/v4/sports/soccer_epl/odds/?apiKey=7703d0f1893451885704e2a99245bff5&regions=us&markets=h2h&oddsFormat=decimal")
    
    canBookies = ["sport888", "leovegas", "draftkings", "pointsbetus", "unibet", "fanduel", "betmgm"]

    maxHomeWin = 0
    maxHomeBookie = ""

    maxAwayWin = 0
    maxAwayBookie = ""

    maxDraw = 0
    maxDrawBookie = ""
    
    printed = False
    
    All = True
    leagues = ["basketball_nba", "basketball_wnba", "basketball_ncaab", "basketball_euroleague"]
    for league in leagues:
        url = "https://api.the-odds-api.com/v4/sports/%s/odds/?apiKey=7703d0f1893451885704e2a99245bff5&regions=us&markets=h2h&oddsFormat=decimal" %(league)
        r = requests.get(url)
        a = r.json()
        
        for games in a: 
            for bookmakers in games["bookmakers"]:
                #print(bookmakers)
                if (All or datetime.today().strftime('%Y-%m-%d') != games["commence_time"][0:10]):
                    if (maxHomeWin < bookmakers["markets"][0]["outcomes"][0]["price"]):
                            maxHomeBookie = bookmakers["title"]
                            maxHomeWin = bookmakers["markets"][0]["outcomes"][0]["price"]   
                    if (maxAwayWin < bookmakers["markets"][0]["outcomes"][1]["price"]):
                            maxAwayBookie = bookmakers["title"]
                            maxAwayWin = bookmakers["markets"][0]["outcomes"][1]["price"]
                    #print(a["description"])
            if (maxHomeWin != 0 and maxAwayWin != 0):
                if ((1 - ((1 / maxHomeWin) +  (1 / maxAwayWin))) * 100 > 0):
                    print("%s vs %s at: %s" %(bookmakers["markets"][0]["outcomes"][0]["name"], bookmakers["markets"][0]["outcomes"][1]["name"], games["commence_time"][0:10]))
                    print("Return: %s%s" %(round((1 - ((1 / maxHomeWin) +  (1 / maxAwayWin))) * 100, 2), "%"))
                    print("Home%sAway%s" %(" " * (len(maxHomeBookie) + 4)," " * (len(maxAwayBookie) + 4)))
                    print("%s: %s | %s: %s\n" %(maxHomeBookie, maxHomeWin, maxAwayBookie, maxAwayWin))
                    #if ((maxHomeBookie in canBookies) and (maxAwayBookie in canBookies) and (maxDrawBookie in canBookies)):
                    #print("Not in Canada")

            maxHomeWin = 0
            maxAwayWin = 0
            maxHomeBookie = ""
            maxAwayBookie = ""


