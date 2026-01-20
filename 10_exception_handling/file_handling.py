file = open("./order.txt", "w")

try:
    file.write("Make some noise for the desi boysz")
finally:
    file.close()


with open("order_2.txt", "w") as file:
    file.write("Lower the volume ,Police has come")
