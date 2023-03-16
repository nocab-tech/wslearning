import requests
from bs4 import BeautifulSoup
import pandas as pd

# Make a request to the website
url = 'http://books.toscrape.com'
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the links to all the categories
categories = soup.find('div', class_='side_categories').find_all('a')
category_urls = [f"http://books.toscrape.com/{c['href']}" for c in categories]

# Define a function to scrape book information from a category page
def scrape_category(category_url):
    # Make a request to the first page of the category
    page_url = category_url
    response = requests.get(page_url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get the category name
    category = soup.find('h1').text.strip()

    # Find all the books in the category
    book_info = []
    while True:
        books = soup.find_all('article', class_='product_pod')

        # Extract the book information
        for book in books:
            title = book.find('h3').find('a')['title']
            rating = ' '.join(book.find('p', class_='star-rating')['class']).replace('star-rating', '').strip()
            price = book.find('p', class_='price_color').text.strip()
            availability = book.find('p', class_='availability').text.strip()
            book_info.append({'category': category, 'title': title, 'rating': rating, 'price': price, 'availability': availability})

        # Check if there is a next page
        next_button = soup.find('li', class_='next')
        if next_button is None:
            break

        # Make a request to the next page and update the soup object
        page_url = category_url.replace('index.html', '') + next_button.find('a')['href']
        response = requests.get(page_url)
        soup = BeautifulSoup(response.content, 'html.parser')

    return book_info

# Scrape all categories and books
all_books = []
for category_url in category_urls:
    # Check if the category should be excluded
    if "books_1" in category_url:
        continue

    # Scrape the category and append the resulting book information to all_books
    all_books.extend(scrape_category(category_url))

# Convert the book information to a Pandas DataFrame
df = pd.DataFrame(all_books)

# Write the DataFrame to an Excel file
df.to_excel('book_info.xlsx', index=False)