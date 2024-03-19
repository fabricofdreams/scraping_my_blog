import csv
from app import scrape_blog
from datetime import datetime

# Blog url
base_url = "https://frobledo.com/blog/blog-1/page/"


# Get all posts
all_posts = scrape_blog(base_url)
# print(f"Scraped {len(all_posts)} posts.")
print(all_posts)


# Specify the filename
today_date = datetime.now().date()
filename = f'''{today_date}_data.csv'''

# Extracting keys and values
title = [item[0] for item in all_posts]
view = [item[1] for item in all_posts]

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['date', 'post', 'views']

    # Create a csv writer object
    csv_writer = csv.DictWriter(csvfile, fieldnames)

    # Write the header row
    csv_writer.writeheader()

    # Write the data rows
    for title, views in zip(title, view):
        csv_writer.writerow(
            {'date': today_date, 'post': title, 'views': views})

print(f"CSV file '{filename}' has been created successfully.")
