import openpyxl
from collections import defaultdict

# Open the workbook
workbook = openpyxl.load_workbook('book_info.xlsx')

# Select the sheet you want to read from
sheet = workbook.active

# Define a dictionary to store the categories and their prices
categories = defaultdict(list)

# Iterate through each row in the sheet
for row in sheet.iter_rows(min_row=2, values_only=True):
    # Extract the category and price from the row
    category = row[0]
    price_str = row[3]
    # Strip the "£" sign from the price string and convert it to a float
    price = float(price_str.strip('£'))
    
    # Add the price to the list for the category
    categories[category].append(price)

# Calculate the average price and book count for each category
category_info = []
for category, prices in categories.items():
    book_count = len(prices)
    if book_count < 5:
        # If the category has less than 5 books, mark it as inconclusive
        category_info.append((category, sum(prices) / book_count, book_count, "inconclusive data"))
    else:
        # Otherwise, calculate the average price and book count as normal
        category_info.append((category, sum(prices) / book_count, book_count, None))

# Sort the categories by average price, in descending order
sorted_categories = sorted(category_info, key=lambda x: x[1], reverse=True)

# Print the sorted categories and their average prices and book counts, with a divider between each category
for category, price, book_count, inconclusive in sorted_categories:
    if inconclusive:
        # If the category is inconclusive, include the inconclusive label in the bracket
        print(f"{category}: £{price:.2f} average price ({book_count} book/s {inconclusive})")
    else:
        print(f"{category}: £{price:.2f} average price ({book_count} book/s)")
    print("--------------------")