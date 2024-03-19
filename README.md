# Blog Scraper and CSV Exporter

This Python script is designed to scrape blog post titles and their view counts from a specified blog URL and export the data into a CSV file. The script uses `requests` to fetch the webpage, `BeautifulSoup` from `bs4` for parsing HTML, and the `csv` module to write the data into a CSV file.

## Features

- Fetches webpage content using HTTP requests.
- Parses HTML content to extract blog post titles and views.
- Exports the extracted data into a CSV file with a timestamp.

## Requirements

To run this script, you'll need Python installed on your machine along with the following Python packages:

- `requests`
- `beautifulsoup4`

You can install these packages using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Modify the `url` variable in the script to the blog you want to scrape.

   ```python
   url = 'https://www.example.com/blog/'
   ```

2. Run the script:

   ```bash
   python read.py
   ```

3. The script will create a CSV file named with the current date, containing the blog post titles and view counts.

## Output

The CSV file will be named in the format `YYYY-MM-DD_data.csv` and will contain three columns:

- `date`: The date when the script was run.
- `post`: The title of the blog post.
- `views`: The view count of the blog post.

## Disclaimer

This script is for educational purposes only. Please ensure you have permission to scrape the website and you comply with the website's terms of service or robots.txt file.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.


