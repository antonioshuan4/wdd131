import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Lee un archivo CSV y retorna un diccionario con los datos."""
    products_dict = {}

    with open(filename, "rt", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            if len(row) > 0: 
                key = row[key_column_index]
                products_dict[key] = row

    return products_dict


def main():
    try:
        products_dict = read_dictionary("products.csv", 0)

        print("Inkom Emporium")
        print("--------------------------------")

        total_items = 0
        subtotal = 0

        with open("request.csv", "rt", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                product_id = row[0]
                quantity = int(row[1])

                product = products_dict[product_id]

                name = product[1]
                price = float(product[2])

                print(f"{name}: {quantity} @ {price}")

                total_items += quantity
                subtotal += price * quantity

        sales_tax_rate = 0.06
        sales_tax = subtotal * sales_tax_rate
        total = subtotal + sales_tax

        print("--------------------------------")
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")

        print("--------------------------------")
        print("Thank you for shopping at the Inkom Emporium.")

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