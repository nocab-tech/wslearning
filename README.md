# http://books.toscrape.com Webscraper Learning Project

## About
This project was started as way to practise and learn basic webcrawling and webscraping using Python as well as a way to learn how to use GitHub. This project currently uses Panda and BeautifulSoup Python Module. I intend to work on this project further and use a real website like IMDB. This project was inspired by my career aspiration in Data Analysis. I tried to simulate an actual workload in the project. Demonstrating the Creation of a Database and Processing of the Database.

## File Descriptions
Web_Scraper.py - The Main Scraper and Crawller.
Brief_Overview.py - A Small Script to give a Brief Overview of all information gathered.
Book_Stock.py - Checks if there is any books currently out of stock.
Book_Count.py - This counts all books in each category
Average_Rating - Shows the Average Ratings of the books in each category
Average_Price - Shows the Average Price of the books in each category

## How does it work?

It will request information from http://books.toscrape.com and will find all available categories. This will then be used to scrape the book information in each catergory seperately. Included are some scripts that can be used to read the information scrapped easier.

## Basic Rundown of the main portions of the code

This code below is used to find all the category urls to be scrapped later on in the code.
```python
def scrape_category(category_url):
    ## Make a request to the first page of the category
    page_url = category_url
    response = requests.get(page_url)

    ## Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    ## Get the category name
    category = soup.find('h1').text.strip()
            
```

This code below will scrape all information from each category of each book in different categories. It also contains a check to see if there is another page to be scraped.

```python
 ## Extract the book information
        for book in books:
            title = book.find('h3').find('a')['title']
            rating = ' '.join(book.find('p', class_='star-rating')['class']).replace('star-rating', '').strip()
            price = book.find('p', class_='price_color').text.strip()
            availability = book.find('p', class_='availability').text.strip()
            book_info.append({'category': category, 'title': title, 'rating': rating, 'price': price, 'availability': availability})

        ## Checks if there is a next page
        next_button = soup.find('li', class_='next')
        if next_button is None:
            break
                
```
