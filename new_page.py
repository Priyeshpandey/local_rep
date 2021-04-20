import requests as req


def getTotalGoals(team, year):
    count=0
    # Get count for team as team1
    url1 = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page=1'
    resp = req.get(url1)
    data = resp.json()
    total_pages = data['total_pages']
    for i in range(1, total_pages+1):
        url = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={i}'
        new_resp = req.get(url=url)
        new_data = new_resp.json()
        for item in new_data['data']:
            count+=int(item['team1goals'])
    # Get count for team as team2
    url2 = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page=1'
    resp = req.get(url2)
    data = resp.json()
    total_pages = data['total_pages']
    for i in range(1, total_pages + 1):
        url = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={i}'
        new_resp = req.get(url=url)
        new_data = new_resp.json()
        for item in new_data['data']:
            count += int(item['team2goals'])
    return count

def getWinnerTotalGoals(competition, year):
    count = 0
    # Write your code here
    #Find winner of given competition,year
    url = f'https://jsonmock.hackerrank.com/api/football_competitions?name={competition}&year={year}'
    response = req.get(url)
    response_json = response.json()
    winner_team = response_json['data'][0]['winner']
    #Count goals of winning team in given competition as team1
    url1 = f'https://jsonmock.hackerrank.com/api/football_matches?competition=' \
           f'{competition}&year={year}&team1={winner_team}&page=1'
    resp = req.get(url1)
    data = resp.json()
    total_pages = data['total_pages']
    for i in range(1, total_pages + 1):
        url = f'https://jsonmock.hackerrank.com/api/football_matches?competition=' \
           f'{competition}&year={year}&team1={winner_team}&page={i}'
        new_resp = req.get(url=url)
        new_data = new_resp.json()
        for item in new_data['data']:
            count += int(item['team1goals'])
    #Count goals of winning team in given competition as team2
    url2 = f'https://jsonmock.hackerrank.com/api/football_matches?competition=' \
           f'{competition}&year={year}&team2={winner_team}&page=1'
    resp = req.get(url2)
    data = resp.json()
    total_pages = data['total_pages']
    for i in range(1, total_pages + 1):
        url = f'https://jsonmock.hackerrank.com/api/football_matches?competition=' \
              f'{competition}&year={year}&team2={winner_team}&page={i}'
        new_resp = req.get(url=url)
        new_data = new_resp.json()
        for item in new_data['data']:
            count += int(item['team2goals'])
    return count

if __name__=='__main__':
    print(getWinnerTotalGoals('UEFA Champions League', 2011))