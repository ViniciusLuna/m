from pymongo import MongoClient

connection_string = "mongodb://mongodb0.example.com:27017"

#connection_string = "mongodb://localhost:27017"

client = MongoClient (connection_string)

db_connection = client["meuBanco"]
collection = db_connection.get_collection("minhaCollection")