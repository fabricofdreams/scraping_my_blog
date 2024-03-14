import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Define the URL of the blog you want to scrape
url = 'https://www.frobledo.com/blog/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the titles and views for each posts on the page
titles = soup.find_all(
    'a', class_='d-block text-reset text-decoration-none o_blog_post_title my-0 h5')
views = soup.find_all(
    'b', class_='text-nowrap ps-2')

titles_tuple = tuple(title.get_text() for title in titles)
views_tuple = tuple(view.get_text() for view in views)

result_dict = dict(zip(titles_tuple, views_tuple))

today_date = datetime.now().date()

# Specify the filename
filename = f'''{today_date}_data.csv'''


with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    # Create a csv writer object
    csv_writer = csv.writer(csvfile)

    # Write the header row
    csv_writer.writerow(['date', 'post', 'views'])

    # Write the data rows
    for title, views in result_dict.items():
        csv_writer.writerow([today_date, title, views])

print(f"CSV file '{filename}' has been created successfully.")
