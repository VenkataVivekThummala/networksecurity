import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv('MONGO_DB_URL')

print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import numpy as np
import pandas as pd
import pymongo
from networksecurity.logging.loggger import logging
from networksecurity.exception.exception import NetworkSecurityEXception

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityEXception(e,sys)

    def cv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv('/home/venkata/Documents/Networksecurity/Network_Data/PhishingData.csv')        
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityEXception(e,sys)

    def insert_data_mongo(self,records,collection,database):
        try:
            self.database=database
            self.records=records
            self.collection=collection

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]

            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityEXception(e,sys)     

if __name__=="__main__":
    File_Path="/home/venkata/Documents/Networksecurity/Network_Data/PhishingData.csv"
    Database="vivek"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.cv_to_json_convertor(file_path=File_Path)
    no_of_records=networkobj.insert_data_mongo(records,database=Database,collection=Collection)
    print(records)
    print(no_of_records)
  
