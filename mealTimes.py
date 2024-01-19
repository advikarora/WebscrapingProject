#gets the meal times for the day off the cds website
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def get_meal_times(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser') 
        meal_times = soup.find_all('div', class_='c-tabs-nav__link-inner')
        meal_times_stripped = [element.text.strip() for element in meal_times]
        print("Meal Times:", meal_times_stripped)
    else:
        print("Failed to retrieve the webpage. Status Code:", response.status_code)
    
current_date = datetime.now().strftime("%Y-%m-%d")
original_url = "https://dining.unc.edu/locations/chase/?date=2024-1-16"
new_url = original_url.replace("2023-11-16", current_date)
get_meal_times(new_url)
