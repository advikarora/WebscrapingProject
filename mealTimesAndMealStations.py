#prints out the menu stations for each meal time
import mealTimes
import menuStations
from datetime import datetime, timedelta

current_date = datetime.now().strftime("%Y-%m-%d") 
original_url = "https://dining.unc.edu/locations/chase/?date=2023-11-16"
new_url = original_url.replace("2023-11-16", current_date)

menuStations, menuStationsPerMealTime = menuStations.get_menu_stations(new_url)
mealTimes = mealTimes.get_meal_times(new_url)
mealNum = 0

for mealTime in mealTimes:
    print("Meal Time: " + mealTime)
    print()
    print("Menu Stations for this Meal Time: ")
    for x in range (menuStationsPerMealTime[mealNum]):
        print(menuStations[x])
    print()
