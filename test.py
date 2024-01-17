import requests
from bs4 import BeautifulSoup

def scrape_menu(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            meal_times_list = []
            mealNum = 0
            meal_times_divs = soup.find_all('div', class_='c-tabs-nav__link-inner')
            for meal_time_div in meal_times_divs:
                meal_time = meal_time_div.text.strip()
                meal_times_list.append(meal_time)  
            meals = soup.find_all('div', class_='c-tab_content')
            if meals:
                for meal in meals:
                    menu_stations = soup.find_all('div', class_='menu-station')
                    if menu_stations:
                        for menu_station in menu_stations:
                            print(meal_times_list[mealNum])
                            mealNum += 1

                            station_name_tag = menu_station.find('h4', class_='toggle-menu-station-data')

                            if station_name_tag:
                                station_name = station_name_tag.text.strip()
                                print(f"Menu Station: {station_name}")
                                menu_items = menu_station.find_all('a', class_=lambda x: x and x.startswith('show-nutrition'))
                                if menu_items:
                                    for menu_item in menu_items:
                                        print(menu_item.get_text(strip=True))
                                else:
                                    print("No menu items found within this menu station.")
                                print()  
                            else:
                                print("No <h4> tag with class 'toggle-menu-station-data' found within this menu station.")
                    else:
                        print("No menu stations found within this meal time.")
                else:
                    print("Nope")
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
menu_url = "https://dining.unc.edu/locations/chase/?date=2023-11-16" 
