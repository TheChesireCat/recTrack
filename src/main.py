from bs4 import BeautifulSoup as bs
import requests
import datetime
import csv
import re
import pytz

base_url = "https://recreation.northeastern.edu/"
base_content = requests.get(base_url).content
base_soup = bs(base_content, "html.parser")
embed_elements = base_soup.find_all("embed")

data_url = embed_elements[0].get("src")
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
data_content = requests.get(data_url, headers=headers)
data_soup = bs(data_content.content, "html.parser")

location_divs = data_soup.find_all('div', {'class': 'col-md-3 col-sm-6'})

# Define Boston time zone
boston_tz = pytz.timezone('America/New_York')

# Open the file in append mode
with open('output.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    # Check if file is empty before writing headers
    if file.tell() == 0:
        writer.writerow(["timestamp_scrape", "percentage", "location_name", "last_count", "updated", "open_boolean"])
    
    for location_div in location_divs:
        try:
            percentage_chart = location_div.find('div', {'class': 'circleChart'})
            percentage = percentage_chart.get('data-percent') if percentage_chart else None

            location_info = location_div.find('div', {'style': 'text-align:center;'})
            location_name = next(location_info.stripped_strings) if location_info else None

            open_status_span = location_div.find('span')
            open_status = open_status_span.get_text(strip=True) if open_status_span else None

            last_count_search = re.search(r"Last Count: (\d+)", location_div.get_text())
            last_count = last_count_search.group(1) if last_count_search else None

            updated_search = re.search(r"Updated: (.*)", location_div.get_text())
            updated = updated_search.group(1) if updated_search else None

            open_boolean = True if "(Open)" in location_info.decode_contents() else False
            # Use Boston time for the timestamp
            writer.writerow([datetime.datetime.now(boston_tz), percentage, location_name, last_count, updated, open_boolean])
        except Exception as e:
            print(f"Error while processing a location: {e}")
