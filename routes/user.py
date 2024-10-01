from fastapi import APIRouter
from models.user import User
from config.db import connect
from schemas.user import serializeDict, serializeList
from bson import ObjectId

#ObjectID -> converts string into a MongoDB ObjectId to uniquely identify each user

user = APIRouter() # creates routes for different endpoints

# fetch all users from database
@user.get('/')
async def find_all_user():
    # Retrieve all user documents from mongodb and return all users
    return serializeList(connect.local.user.find())

# fetch a single user by their unique MongoDB _id
@user.get('/{id}')
async def find_one_user(id):
    # Retrieve a user by id
    return serializeDict(connect.local.user.find_one({"_id": ObjectId(id)}))

# add a new user to the database
@user.post('/')
async def create_user(user: User):
    # Insert a new user and return the updated user list
    connect.local.user.insert_one(dict(user))
    # after inserting, all the users are fetched and returned 
    return serializeList(connect.local.user.find())

# update an existing user's information
@user.put('/{id}')
async def update_user(id, user: User):
    # Update the user with the given id and return the updated user
    connect.local.user.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })
    return serializeDict(connect.local.user.find_one({"_id": ObjectId(id)}))

# delete a user from the database
@user.delete('/{id}')
async def delete_user(id, user:User):
    # Delete the user with the given id and return the deleted user
    return serializeDict(connect.local.user.find_one_and_delete({"_id": ObjectId(id)}))

    


    

