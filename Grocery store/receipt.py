# receipt.py
# Enhancement: This program prints a return-by date (30 days later at 9:00 PM)

import csv
from datetime import datetime, timedelta


def read_dictionary(filename, key_column_index):
    """Reads a CSV file into a dictionary"""
    products_dict = {}

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        for row in reader:
            key = row[key_column_index]
            products_dict[key] = row

    return products_dict


def main():
    try:
        # Read products dictionary
        products_dict = read_dictionary("products.csv", 0)

        print("Inkom Emporium")

        total_items = 0
        subtotal = 0

        # Read request file
        with open("request.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header

            for row in reader:
                product_id = row[0]
                quantity = int(row[1])

                # Lookup product (may raise KeyError)
                product = products_dict[product_id]

                name = product[1]
                price = float(product[2])

                print(f"{name}: {quantity} @ {price:.2f}")

                total_items += quantity
                subtotal += quantity * price

        # Totals
        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax

        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")

        print("Thank you for shopping at the Inkom Emporium.")

        # Current date and time
        now = datetime.now()
        print(now.strftime("%a %b %d %H:%M:%S %Y"))

        # ✅ Enhancement: Return-by date (30 days later at 9 PM)
        return_date = now + timedelta(days=30)
        return_date = return_date.replace(hour=21, minute=0, second=0)
        print("Return by:", return_date.strftime("%a %b %d %I:%M %p %Y"))

    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)

    except PermissionError:
        print("Error: permission denied")

    except KeyError as e:
        print("Error: unknown product ID in the request.csv file")
        print(e)


# Run program
if __name__ == "__main__":
    main()