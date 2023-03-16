import openpyxl
import pandas as pd
from collections import defaultdict

# Load the xlsx file into a pandas dataframe
df = pd.read_excel('book_info.xlsx')

# Get the top and bottom 3 categories by count
top_categories = df['category'].value_counts().head(3)
bottom_categories = df['category'].value_counts().tail(3)

print('''Book Count Overview
----------------------------------------
Top 3:
''')

# Print the top categories and their counts
for category, count in top_categories.items():
    print(f"{category}: {count} books")
    print("----------------------------------------")

print('''
Bottom 3:
''')

# Print the bottom categories and their counts
for category, count in bottom_categories.items():
    print(f"{category}: {count} books")
    print("----------------------------------------")

# Define a dictionary to map string ratings to integers
rating_dict = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five":5}

# Define a dictionary to store the categories and their ratings
categories = defaultdict(list)

# Iterate through each row in the dataframe
for index, row in df.iterrows():
    # Extract the category and rating from the row
    category = row['category']
    rating_str = row['rating']
    rating = rating_dict[rating_str]
    
    # Add the rating to the list for the category
    categories[category].append(rating)

# Calculate the average rating and book count for each category
category_info = []
for category, ratings in categories.items():
    book_count = len(ratings)
    if book_count < 5:
        # If the category has less than 5 books, mark it as inconclusive
        category_info.append((category, sum(ratings) / book_count, book_count, "inconclusive data"))
    else:
        # Otherwise, calculate the average rating and book count as normal
        category_info.append((category, sum(ratings) / book_count, book_count, None))

# Sort the categories by average rating, in descending order
sorted_categories = sorted(category_info, key=lambda x: x[1], reverse=True)

# Filter out the inconclusive categories and keep only the top and bottom 3 rated categories
top_rated = [c for c in sorted_categories if not c[3]][0:3]
bottom_rated = [c for c in sorted_categories if not c[3]][-3:]

print('''Category Average Rating Overview (Inclusive Data Not Included)
----------------------------------------
Top 3:
''')

# Print the top rated categories and their average ratings and book counts
for category, rating, book_count, inconclusive in top_rated:
    print(f"{category}: {rating:.2f} average rating ({book_count} book/s)")
    print("----------------------------------------")

print('''
Bottom 3:
''')

# Print the bottom rated categories and their average ratings and book counts
for category, rating, book_count, inconclusive in bottom_rated:
    print(f"{category}: {rating:.2f} average rating ({book_count} book/s)")
    print("----------------------------------------")

# Assume all books are in stock initially
all_books_in_stock = True

# Iterate over each row in the dataframe
for index, row in df.iterrows():
    category = row['category']
    title = row['title']
    availability = row['availability']
    
    # Check if availability is not "In Stock"
    if availability != "In stock":
        # Print the category, title, and a message indicating that the item is out of stock
        print(category, title, "Is out of stock")
        
        # Update the all_books_in_stock flag to False
        all_books_in_stock = False

# Check if all_books_in_stock is still True
if all_books_in_stock:
    print("All books in stock")
