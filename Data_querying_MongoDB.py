from pymongo import MongoClient
import subprocess
import json

db_name = 'Project_2_Udacity'

client = MongoClient('localhost:27017')
db = client[db_name]

 file1 = "Seattle.osm.json"

# Build mongoimport command
collection = file1[:file1.find('.')]
mongoimport_cmd = 'mongoimport -h 127.0.0.1:27017 ' + \
                  '--db ' + db_name + \
                  ' --collection ' + collection + \
                  ' --file ' + file2

# Drop collection (if it's already running)
if collection in db.list_collection_names():
    print 'Dropping collection: ' + collection
    db[collection].drop()

# Execute the command
print 'Executing: ' + mongoimport_cmd
subprocess.call(mongoimport_cmd.split())


# Displays the names of the collection
db.list_collection_names()

# Displays the colletion statistics
db.command("collstats","Seattle")

# Displays on item in the document
Seattle_region.find_one()

# Displays number of documents
Seattle_region.count_documents()

# Displays number of nodes
Seattle_region.count_documents({'type':'node'}).count()

# Displays number of ways
Seattle_region.count_documents({'type':'way'})

# Displays the number of users
len(Seattle_region.distinct('created.user'))

# Creates a list of users
list_users = Seattle_region.distinct('created.user')

# Display some user names
print sorted(list_users)[:50]

# Displays number of documents created by a specific users
Seattle_region.count_documents({"created.user": "Adam Schneider"})

# Displays documents created by specific user
for element in Seattle_region.find({"created.user": "Adam Schneider"}).sort("timestamp"):
    print element

# Displays list of the top three users
top_users = Seattle_region.aggregate([
    { "$group" : {"_id" : "$created.user", "count" : { "$sum" : 1} } },
    { "$sort" : {"count" : -1} }, { "$limit" : 3 }
] )
list(top_users)


# Count users with one post
onetime_users = Seattle_region.aggregate( [
    { "$group" : {"_id" : "$created.user", "count" : { "$sum" : 1} } },
    { "$group" : {"_id" : "$count", "num_users": { "$sum" : 1} } },
    { "$sort" : {"_id" : 1} }, { "$limit" : 1}
] )
list(onetime_users)


# Create a list of 10 users with one post
list_onetime_users = Seattle_region.aggregate([
    { "$group" : {"_id" : "$created.user", "count" : { "$sum" : 1} } },
    { "$sort" : {"count" : 1} }, { "$limit" : 10 }
] )
print list(list_onetime_users)

# Create a list of 3 most common places
places = Seattle_region.aggregate( [
    { "$match" : { "address.place" : { "$exists" : 1} } },
    { "$group" : { "_id" : "$address.place", "count" : { "$sum" : 1} } },
    { "$sort" : { "count" : -1}}, {"$limit":3}
] )
list(places)

# Create a list of 3 most common zipcodes
top_zipcodes = Seattle_region.aggregate( [
    { "$match" : { "address.postcode" : { "$exists" : 1} } },
    { "$group" : { "_id" : "$address.postcode", "count" : { "$sum" : 1} } },
    { "$sort" : { "count" : -1}}, {"$limit": 3}
] )
list(top_zipcodes)

# Count zipcodes with one document
onetime_zipcodes = Seattle_region.aggregate( [
    { "$group" : {"_id" : "$address.postcode", "count" : { "$sum" : 1} } },
    { "$group" : {"_id" : "$count", "count": { "$sum" : 1} } },
    { "$sort" : {"_id" : 1} }, { "$limit" : 1}
] )
list(onetime_zipcodes)
