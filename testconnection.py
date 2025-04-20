from pymongo import MongoClient

uri = "mongodb+srv://mkitimbo:txaHdneje2CZmkOt@kmt.tslnr0v.mongodb.net/income_db?retryWrites=true&w=majority&tls=true"
client = MongoClient(uri)

try:
    db = client["income_db"]
    print("Connection successful:", db.list_collection_names())
except Exception as e:
    print("Connection failed:", e)