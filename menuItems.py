import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def scrape_menu(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            menu_items = []
            menu_items1 = soup.find_all('a', class_=lambda x: x and 'gluten' in x)
            menu_items2 = soup.find_all('a', class_=lambda x: x and 'show-nutrition' in x) 
            if menu_items1 and menu_items2:
                for menu_item in menu_items1:
                    menu_items.append(menu_item.get_text(strip=True))
                for menu_item in menu_items2:
                    menu_items.append(menu_item.get_text(strip=True))
                print(menu_items)
            else:
                print("No menu items found with the specified setup.")
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

current_date = datetime.now().strftime("%Y-%m-%d")
original_url = "https://dining.unc.edu/locations/chase/?date=2024-1-8"
new_url = original_url.replace("2023-11-16", current_date)

scrape_menu(new_url)
