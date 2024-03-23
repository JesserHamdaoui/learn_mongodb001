from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://JesserHamdaoui:{password}@learnmangodb001.3pe17pa.mongodb.net/?retryWrites=true&w=majority&appName=learnMangoDB001"

client = MongoClient(connection_string)

test_db = client.learnMongoDB001

def insert_test_doc():
    collection = test_db.test
    test_document = {
        'name': "Jesser",
        'age': 60
    }
    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id)

production = client.production
person_collection = production.person_collection
def create_documents():
    names = ["Jesser", "Ranim", "Azer", "Rimes", "Ayoub"]
    ages = [60, 61, 50, 1, 10]

    docs = []
    for name, age in zip(names, ages):
        doc = {'name': name, 'age': age}
        docs.append(doc)
        # person_collection.insert_one(doc)
    person_collection.insert_many(docs)

create_documents()