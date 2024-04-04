from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime

uri = "mongodb+srv://josemarie:B4wZTxcgHYbPEvkw@atlascluster.45jrjqo.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# db = client["XYZ"]
# users = db["users"]

# details = [
#   {
#     "username": "alice_jones",
#     "email": "alice.jones@example.com",
#     "password": "hashed_password_3",
#     "created_at": datetime.datetime.now(),
#     "address": {
#       "street": "789 Pine St",
#       "city": "Villageton",
#       "zip": "13579",
#       "country": "Testland"
#     }
#   },
#   {
#     "username": "bob_smith",
#     "email": "bob.smith@example.com",
#     "password": "hashed_password_4",
#     "created_at": datetime.datetime.now(),
#     "address": {
#       "street": "101 Elm St",
#       "city": "Hamletville",
#       "zip": "24680",
#       "country": "Demo Country"
#     }
#   },
#   {
#     "username": "sara_davis",
#     "email": "sara.davis@example.com",
#     "password": "hashed_password_5",
#     "created_at": datetime.datetime.now(),
#     "address": {
#       "street": "111 Maple St",
#       "city": "Countryside",
#       "zip": "98765",
#       "country": "Example Republic"
#     }
#   },
#   {
#     "username": "michael_brown",
#     "email": "michael.brown@example.com",
#     "password": "hashed_password_6",
#     "created_at": datetime.datetime.now(),
#     "address": {
#       "street": "222 Birch St",
#       "city": "Suburbia",
#       "zip": "11223",
#       "country": "Sample Republic"
#     }
#   },
#   {
#     "username": "emily_white",
#     "email": "emily.white@example.com",
#     "password": "hashed_password_7",
#     "created_at": datetime.datetime.now(),
#     "address": {
#       "street": "333 Cedar St",
#       "city": "Metropolis",
#       "zip": "44556",
#       "country": "Virtualand"
#     }
#   },
#   {
#     "username": "david_miller",
#     "email": "david.miller@example.com",
#     "password": "hashed_password_8",
#     "created_at": datetime.datetime.now(), 
#     "address": {
#       "street": "444 Oak St",
#       "city": "Cityburg",
#       "zip": "77888",
#       "country": "Modeland"
#     }
#   },
#   {
#     "username": "olivia_lee",
#     "email": "olivia.lee@example.com",
#     "password": "hashed_password_9",
#     "created_at":datetime.datetime.now(), 
#     "address": {
#       "street": "555 Pine St",
#       "city": "Villageburg",
#       "zip": "99000",
#       "country": "Demo Republic"
#     }
#   },
#   {
#     "username": "samuel_clark",
#     "email": "samuel.clark@example.com",
#     "password": "hashed_password_10",
#     "created_at": datetime.datetime.now(),
#     "address": {
#       "street": "666 Elm St",
#       "city": "Hamletburg",
#       "zip": "11222",
#       "country": "Test Republic"
#     }
#   }
# ]


# users.insert_many(details)

# filter = {"email":"samuel.clark@example.com" }
# result = users.find()
# for i in result:
#     print(list(i))
    

#  sorting :
    
# db = client["XYZ"]
# users = db["users"]

# result = users.find().sort("username")

# for i in result:
#     print(i,"\n")

# result = users.find().sort("username",-1)

# for i in result:
#     print(i,"\n")

#  query:

# filter = { "username": { "$gt": "d" } }

# result = users.find(filter)

# for x in result:
#   print(x,"\n")

#  filtered using regular expressions:

# filter = { "username": { "$regex": "^s" }  }

# result = users.find(filter)

# for x in result:
#   print(x,"\n")

#  Delete one document:

# filter = {"email":"samuel.clark@example.com" }

# users.delete_one(filter)

#  deelte multiple document:

# filter = {"username": { "$regex": "^s" } }

# users.delete_many(filter)
    
# db = client["XYZ"]
# users = db["users"]
#   update_one

# myquery = { "username": "alice_jones" }
# update = { "$set": { "username": "albert_joseph" } }

# users.update_one(myquery, update)

#   update_many

# myquery = {"address.country": {"$regex": "^Testland"}}
# update = {"$set": {"address.country": "Poland"}}
# users.update_many(myquery, update)
    
# import pymongo

# # Connect to MongoDB
# client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["student_database"]
collection = db["students"]

def add_student():
    num_students = int(input("Enter the number of students to add: "))
    students = []
    for i in range(num_students):
        roll_number = input(f"Enter roll number for student {i+1}: ")
        name = input(f"Enter name for student {i+1}: ")
        age = int(input(f"Enter age for student {i+1}: "))
        gender = input(f"Enter gender for student {i+1}: ")
        grade = input(f"Enter grade for student {i+1}: ")
        subjects = input(f"Enter subjects (comma-separated) for student {i+1}: ").split(",")
        student = {
            "roll_number": roll_number,
            "name": name,
            "age": age,
            "gender": gender,
            "grade": grade,
            "subjects": subjects
        }
        students.append(student)

    collection.insert_many(students)
    print("Students added successfully.")

    add_student()

# Implement other functions (view_students, update_student, delete_student, find_one_student, find_many_students, main) here...
    


