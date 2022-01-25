from pymongo import MongoClient

connection = MongoClient("mongodb://root:rootpassword@mymongo:27017").local
# db = MongoClient('mongo:27017/').mydatabase

# connection = MongoClient('mymongo:27017/').local