import mealTimes
import menuStations
import menuItems
from datetime import datetime, timedelta

class MenuItem:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class MenuStation:
    def __init__(self, name):
        self.name = name
        self.menu_items = []

    def add_menu_item(self, menu_item):
        self.menu_items.append(menu_item)
    
    def menu_item_references(self):
        return self.menu_items
    
    def menu_item_strings(self):
        return [str(obj) for obj in self.menu_items]

    def __str__(self):
        return (self.name)

class MealTime:
    def __init__(self, name):
        self.name = name
        self.menu_stations = []

    def add_menu_station(self, menu_station):
        self.menu_stations.append(menu_station)

    def menu_station_references(self):
        return self.menu_stations

    def menu_station_strings(self):
        return [str(obj) for obj in self.menu_stations]

    def __str__(self):
        return (self.name)

current_date = datetime.now().strftime("%Y-%m-%d") 
original_url = "https://dining.unc.edu/locations/chase/?date=2023-11-16"
new_url = original_url.replace("2023-11-16", current_date)

menuStations, menuStationsPerMealTime = menuStations.get_menu_stations(new_url)
mealTimes = mealTimes.get_meal_times(new_url)
menuItems, menuItemsPerStation = menuItems.get_menu_items(new_url)


index = 0
mealNum = 0
stationNum = 0
mealTimeObjects = []

for x in range(len(mealTimes)):
    mealTimeObjects.append(MealTime(mealTimes[x]))
    for t in range(menuStationsPerMealTime[x]):
        mealTimeObjects[x].add_menu_station(MenuStation(menuStations[index]))
        index += 1
    mealNum += 1

index = 0
stationNum = 0

for x in range(len(mealTimeObjects)):
    for station in mealTimeObjects[x].menu_station_references():
        for t in range(menuItemsPerStation[stationNum]):
            station.add_menu_item(MenuItem(menuItems[index]))
            index += 1
        stationNum += 1

print("Meal Times today: ")
print([str(obj) for obj in mealTimeObjects])

meal_choice_num = int(input("Enter the number of the meal time you'd like to view: "))
meal_choice = mealTimeObjects[meal_choice_num - 1]

print("Menu Stations for this Meal Time: ")
print(meal_choice.menu_station_strings())

menu_station_num = int(input("Enter the number of the menu station you'd like to view: "))
temp = meal_choice.menu_station_references()

print("Menu items for this station: ")
print(temp[menu_station_num - 1].menu_item_strings())
