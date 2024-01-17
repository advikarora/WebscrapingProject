import requests
from bs4 import BeautifulSoup

def scrape_menu(url):
    try:
        # Send an HTTP request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all <div> tags with class "menu-station"
            menu_stations = soup.find_all('div', class_='menu-station')

            # Check if any menu stations are found
            if menu_stations:
                for menu_station in menu_stations:
                    # Find the <h4> tag with class "toggle-menu-station-data" within the menu station
                    station_name_tag = menu_station.find('h4', class_='toggle-menu-station-data')

                    # Check if <h4> tag is found before extracting text
                    if station_name_tag:
                        station_name = station_name_tag.text.strip()
                        print(f"Menu Station: {station_name}")

            # Ask the user for input on which menu station they want to view
            user_input = input("Enter the name of the menu station you want to view: ")

            # Find the menu station with the user-inputted name
            selected_menu_station = soup.find('h4', text=user_input)

            # Check if the selected menu station is found
            if selected_menu_station:
                # Find all <a> tags with class starting with "show-nutrition allergen" within the selected menu station
                menu_items = selected_menu_station.find_next('div', class_='menu-station').find_all('a', class_=lambda x: x and x.startswith('show-nutrition allergen'))

                # Check if any menu items are found within the selected menu station
                if menu_items:
                    for menu_item in menu_items:
                        # Extract and print the text content of each menu item
                        print(menu_item.get_text(strip=True))
                else:
                    print("No menu items found within the selected menu station.")
            else:
                print(f"No menu station found with the name '{user_input}'.")
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
menu_url = "https://dining.unc.edu/locations/chase/?date=2023-11-16"  # Replace with your actual URL
scrape_menu(menu_url)
