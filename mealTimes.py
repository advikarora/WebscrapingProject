#returns the meal times for the day
import requests
from bs4 import BeautifulSoup

def get_meal_times(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser') 
    meal_times = soup.find_all('div', class_='c-tabs-nav__link-inner')
    meal_times_stripped = [element.text.strip() for element in meal_times]
    return meal_times_stripped
