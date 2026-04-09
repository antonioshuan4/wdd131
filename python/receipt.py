import csv
from datetime import datetime


def read_dictionary(filename, key_column_index):
    """Reads a CSV file and returns a dictionary."""
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
        # Read product catalog
        products_dict = read_dictionary("products.csv", 0)

        print("Inkom Emporium")

        total_items = 0
        subtotal = 0

        # Read customer request
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

                print(f"{name}: {quantity} @ {price}")

                total_items += quantity
                subtotal += price * quantity

        # Calculations
        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax

        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")

        print("Thank you for shopping at the Inkom Emporium.")

        # Current date and time
        current_date = datetime.now()
        print(current_date.strftime("%a %b %d %H:%M:%S %Y"))

    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)

    except PermissionError:
        print("Error: permission denied")

    except KeyError as e:
        print("Error: unknown product ID in the request.csv file")
        print(e)


if __name__ == "__main__":
    main()