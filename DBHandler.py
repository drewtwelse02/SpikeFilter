from Notification import Error,Info,Warning
from pymongo import MongoClient
import bson
import os
class DB:
    def __init__(self,):
        print("DB Called")
        # Get creds 
        conn_string = os.environ["SpikeScanner_conn_string"]
        self.client     = MongoClient(conn_string)
        if ("AllHeadlines" in self.client["AllHeadlinesDB"].list_collection_names()):
            self.headlines_coll = self.client["AllHeadlinesDB"]["AllHeadlines"]      
        else :
            Error("Database does not exist ")

    def find_headline(self,message):
        search_result = self.headlines_coll.find_one({"Symbol": message[0]})
        if search_result:
            return search_result
    def find_existing_headline(self,message):
        ext_hdl_result = self.headlines_coll.find_one({"Title":message[1]})
        if ext_hdl_result:
            return True
        else:
            return False
        
    def insert_headline(self,headline):
        split_headline = headline.split(",")
        m = {"Symbol"  : split_headline[0],
             "Title"   : split_headline[1],
             "Exchange": split_headline[2],
             "Datetime": split_headline[3],
             "Unix"    : split_headline[4],
             "Source"  : split_headline[5]
             }
        r = self.headlines_coll.insert_one(m)
        Warning(f"New Document inserted in the Collection - {r.inserted_id} ")

        