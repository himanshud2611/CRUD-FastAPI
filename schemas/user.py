def userEntity(item) -> dict:
    return{
        "id" : str(item["_id"]),
        "name" : item["name"],
        "email" : item["email"],
        "password" : item["password"]
    }

def usersEntity(entity) -> list:
    return[userEntity(item) for item in entity]

#Important!!!
#handle formatting the MongoDB data to make it serialize i JSON format
#converts every model to dict
def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i=='_id'}, 
            **{i: a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
