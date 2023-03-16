import openpyxl
from collections import defaultdict

# Define a dictionary to map string ratings to integers
rating_dict = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five":5}

# Open the workbook
workbook = openpyxl.load_workbook('book_info.xlsx')

# Select the sheet you want to read from
sheet = workbook.active

# Define a dictionary to store the categories and their counts
categories = defaultdict(list)

# Iterate through each row in the sheet
for row in sheet.iter_rows(min_row=2, values_only=True):
    # Extract the category and rating from the row
    category = row[0]
    rating_str = row[2]  # Get the string rating
    rating = rating_dict[rating_str]  # Convert the string rating to an integer using the rating_dict
    
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

# Print the sorted categories and their average ratings and book counts, with a divider between each category
for category, rating, book_count, inconclusive in sorted_categories:
    if inconclusive:
        # If the category is inconclusive, include the inconclusive label in the bracket
        print(f"{category}: {rating:.2f} average rating ({book_count} book/s {inconclusive})")
        print("----------------------------------------")
    else:
        print(f"{category}: {rating:.2f} average rating ({book_count} book/s)")
        print("----------------------------------------")

