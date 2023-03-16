# http://books.toscrape.com Webscrapper Learning Project

## About
This project was started as way to practise and learn basic webcrawlling and webscrapping using Python as well as a way to learn how to use GitHub. This project currently uses Panda and BeautifulSoup Python Module. I intend to work on this project further and use a real website like IMDB. This project was inspired by my career aspiration in Data Analysis.

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
