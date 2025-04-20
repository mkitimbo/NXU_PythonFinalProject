from pymongo import MongoClient

uri = "mongodb+srv://mkitimbo:txaHdneje2CZmkOt@kmt.tslnr0v.mongodb.net/income_db?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client["income_db"]

# Test a simple query
print(db.list_collection_names())