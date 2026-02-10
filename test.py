from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
client.admin.command("ping")

db = client["dynamic_query_db"]
collection = db["employee_report"]

print(collection.count_documents({}))
