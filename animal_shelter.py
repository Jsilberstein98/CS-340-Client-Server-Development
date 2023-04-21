from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for animal collection in MongoDB"""
    
    def __init__(self,username,password):
        #initialize the mongo client to access mongo Databases and collections
        self.client = MongoClient('mongodb://%s:%s@127.0.0.1:47909/AAC'%(username, password))
        self.database = self.client['AAC']

        
    #C in CRUD 
    def create(self,data):
        if data is not None:
            if data:
                self.database.animals.insert(data) #data should be directory
                return True
        else:
            return False
          
        
    #R in CRUD
    def read(self,search):
        try:
            searchResult = self.database.animals.find(search,{"_id":False})
            print(searchResult)
            return searchResult
        except Exception as e:
            return str(e)
    
    #U in CRUD    
    def update(self,search,replace):
        try:
            result = self.database.animals.update_many(search,replace)
            return self.read(search)
        except Exception as e:
            return str(e)
            
     #D in CRUD
    def delete(self,search):
        try:
            result = self.database.delete_many(search)
            return result.raw_result
        except Exception as e:
            return str(e)
