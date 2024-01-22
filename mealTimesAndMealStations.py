#prints out the menu stations for each meal time
import mealTimes
import menuStations
import menuItems
from datetime import datetime, timedelta

current_date = datetime.now().strftime("%Y-%m-%d") 
original_url = "https://dining.unc.edu/locations/chase/?date=2023-11-16"
new_url = original_url.replace("2023-11-16", current_date)

menuStations, menuStationsPerMealTime = menuStations.get_menu_stations(new_url)
mealTimes = mealTimes.get_meal_times(new_url)
menuItems, menuItemsPerStation = menuItems.get_menu_items(new_url)

index = 0
index1 = 0
mealNum = 0
stationNum = 0

for mealTime in mealTimes:
    print("Meal Time: " + mealTime)
    print()
    for x in range (menuStationsPerMealTime[mealNum]):
        print("Menu Station: " + menuStations[index])
        print()
        index += 1
        for x in range (menuItemsPerStation[stationNum]):
            print(menuItems[index1])
            index1 += 1
        print()
        stationNum += 1
    print()
    mealNum +=1
