
def server_chai(flavor):
    print(f"Preparing {flavor} chai")
    try:
        if flavor == "unknown":
            raise ValueError("Given flavour is not available")
    except ValueError as e:
        print("Error : ", e)
    else:
        print(f"Serving {flavor} chai")
    finally:
        print("Next costumer pleas.....")


server_chai("Ginger")
server_chai("unknown")
