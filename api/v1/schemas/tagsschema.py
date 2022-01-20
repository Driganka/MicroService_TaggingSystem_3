def tagEntity(item) -> dict:
    return {
        "id": item["id"],
        "uname": item["uname"],
        "utags": item["utags"]
    }

def tagsEntity(entity) -> list:
    return [tagEntity(item) for item in entity]