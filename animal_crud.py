from pymongo import MongoClient

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        
            ## Login Information
        USER = 'aacuser'
        PASS = 'SNHU419'
        HOST = '127.0.0.1'
        PORT = 27017
        DB = 'acc'
        COL = 'animals'
        CONNECTION = "mongodb://127.0.0.1:27017"

        #self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.client = MongoClient(CONNECTION)
        self.database = self.client[DB]
        self.collection = self.database[COL]
      
            ## Create Function
    def create(self, data):
        if data is not None:
            self.collection.insert_one(data)  
        else:
            raise Exception("Error: Nothing to save, because data parameter is empty")

            ## Read Function
    def read(self, query):
        if query is not None:
            result = list(self.collection.find(query))
            return result
        else:
            raise Exception("Error: Nothing to query, because query is empty.")

            ## Update Function                       
    def update(self, update_query, update_data):
        if update_query is not None and update_data is not None:
            self.collection.update_one(update_query, {"$set": update_data})
        else:
            raise Exception("Error: Nothing to update, because data or query is empty.")

            ## Delete Function
    def delete(self, query):
        if query is not None:
            self.collection.delete_one(query)
        else:
            raise Exception("Error: Nothing to delete, because the query is empty.")                   