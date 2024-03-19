import requests
from bs4 import BeautifulSoup


def scrape_blog(base_url):
    all_posts = []

    page_number = 1
    while True:
        url = f"{base_url}/{page_number}"
        print(url)
        response = requests.get(url)
        if response.status_code != 200:
            break  # Assuming 404 or other status code means end of pagination
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the titles and views for each posts on the page
        titles = soup.find_all(
            'a', class_='d-block text-reset text-decoration-none o_blog_post_title my-0 h5')
        views = soup.find_all(
            'b', class_='text-nowrap ps-2')

        titles_tuple = tuple(title.get_text() for title in titles)
        views_tuple = tuple(view.get_text() for view in views)

        posts = list(zip(titles_tuple, views_tuple))
        if not posts:
            break  # No more posts found, exit loop
        all_posts.extend(posts)
        page_number += 1

    return all_posts
