import pymongo

client = pymongo.MongoClient('****')

db = client['test_streamlit']

collection = db['wages']

data = {'name':'Artan',
        'city':'Prizren',
        'profession':'instructor'}

result = collection.insert_one(data)

print(f'Inserted document id {result.inserted_id}')

# query_result = collection.find_one({'name':'Egzon'})
# print('Query result',query_result['city'])

# update_result = collection.update_one({'name':'Egzon'},{'$set':{'city':'Lipjan'}})
# print('Modified documents', update_result.modified_count)

# delete_result = collection.delete_one({'city':'Lipjan'})
# print('Deleted items',delete_result.deleted_count)