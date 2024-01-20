#prints all menu stations for the current day
import requests
from bs4 import BeautifulSoup


def get_menu_stations(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser') 
    mealTimes = soup.find_all('div', class_= ['c-tab', 'is-active'])
    array = []
    final = []
    stationsPerMealTime = []
    for t in range(len(mealTimes)):
        elements = mealTimes[t].find_all('h4', class_='toggle-menu-station-data')
        array += elements
        stationsPerMealTime.append(len(elements))
    for station in array:
        final.append(station.get_text(strip = True))
    return final, stationsPerMealTime



""""
#prints all menu stations for the current day
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def get_menu_stations(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser') 
    mealTimes = soup.find_all('div', class_= ['c-tab', 'is-active'])
    array = []
    stationsPerMealTime = []
    for t in range(len(mealTimes)):
        elements = mealTimes[t].find_all('h4', class_='toggle-menu-station-data')
        array += elements
        stationsPerMealTime.append(len(elements))
    for station in array:
        print(station.get_text(strip = True))
    print(stationsPerMealTime)

current_date = datetime.now().strftime("%Y-%m-%d") 
original_url = "https://dining.unc.edu/locations/chase/?date=2023-11-16"
new_url = original_url.replace("2023-11-16", current_date)
get_menu_stations(new_url)
"""