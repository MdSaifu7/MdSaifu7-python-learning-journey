def serve_chai(flavour):
    if flavour not in ["ginger", "masala", "cardamom"]:
        raise ValueError("Unsupported Chai flavour")
    print("serving {flavour} chai")


serve_chai("ginger")
serve_chai("mint")
