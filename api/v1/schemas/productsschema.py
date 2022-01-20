def productEntity(item) -> dict:
    return {
        "pid": item["pid"],
        "pname": item["pname"],
        "ptags": item["ptags"]
    }

def productsEntity(entity) -> list:
    return [productEntity(item) for item in entity]