#returns menu items for a day, as well as how many menu items there are in a menu station
import requests
from bs4 import BeautifulSoup

def get_menu_items(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser') 
    mealTimes = soup.find_all('div', class_= ['c-tab', 'is-active'])
    array1 = []
    array2 = []
    final = []
    menuItemsPerStation = []
    menuItemsPerMealTime = []
    for t in range(len(mealTimes)):
        elements1 = mealTimes[t].find_all('div', id=lambda x: x and x.startswith('menu-station-data'))
        array1 += elements1
        menuItemsPerMealTime.append(len(elements1))
    for t in range(len(array1)):
        elements2 = array1[t].find_all('li', class_=lambda x: x and 'menu-item' in x)
        array2 += elements2
        menuItemsPerStation.append(len(elements2))
    for item in array2:
        final.append(item.get_text(strip = True))
    return final, menuItemsPerStation
