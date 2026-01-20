def process_order(item, quantity):
    try:
        price = {"masala": 20, "light": 10}[item]
        cost = int(price) * int(quantity)
    except KeyError:
        print("Given item not in the menu")
    except ValueError:
        print("Quantity should be in number")
    else:
        print(f"Bill amount : {cost}")


process_order("masala", 10)
process_order("masala", "ten")
