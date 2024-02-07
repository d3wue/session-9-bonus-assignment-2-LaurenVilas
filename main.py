import requests
import bs4

userAgent = { # Define the user agent telling the Website we are using Google Chrome to avoid getting blocked
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}


while True: # Start indefinit loop
    print("1. Show available Teams")
    print('2. Select team and show high level information on the team') # Print menu
    print("3. Stop the programm")
    userInput = int(input("Enter your option \n >>>")) # Get user selection
    if userInput == 1: # Check user selection
        url = f'https://www.transfermarkt.com/bundesliga/startseite/wettbewerb/L1'
        r = requests.get(url, headers=userAgent)
        if r.status_code == 200: # Check if status code is 200
            htmlText = r.text
            htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser')
            table = htmlDocument.find("table", {"class": "items"}).find("tbody")
            teams=table.find_all("tr")

            for team in teams:
            #team=teams[0]
                teamName=team.find("td",{"class":"hauptlink no-border-links"}).get_text().strip()
                
                print(f"{teamName}")

    if userInput == 2:
        choice = int(input("index of the team\n >>>"))  
        team=teams[choice]
        teamName=team.find("td",{"class":"hauptlink no-border-links"}).get_text().strip()
        info=team.find_all("td",{"class": "zentriert"})
        squad=info[1].text
        age=info[2].text
        foreigners=info[3].text
        info1=team.find_all("td",{"class":"rechts"})
        averageMarketValue=info1[0].text
        totalMarketValue=info1[1].text
        print(f"{teamName}, Spieleranzahl: {squad}, Durchschnittsalter: {age} Ausländer: {foreigners}, Durchschnittsmarktwert: {averageMarketValue}, Gesamtmarktwert: {totalMarketValue}")    

    if userInput == 3: 
        break   