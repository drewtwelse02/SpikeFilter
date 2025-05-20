from Notification import Info
import os
import DBHandler
import asyncio
class MsgHandler:
    # Instance attributes
    def __init__(self,):
        self.q          = asyncio.Queue()
        Info("Message Handler Started")

    def filter_message(self,message,db_handler):
        self.message_to_process =  message.split(",")
        #Check message type (Spike or headline) -> 6=Spike 7=news 
        if (len(self.message_to_process) == 6 ):
            headline_search_result  = db_handler.find_headline(self.message_to_process)
            if(headline_search_result):
                Info(f"Spike Detected on {self.message_to_process[0]} \n Possible Headline : {headline_search_result['Title']}")
            else:
                Info(f"Nothing is found for {self.message_to_process}")
        elif(len(self.message_to_process)== 7):
            #Info(" Headline Detected. Searching for an existing title in the DB ")
            if db_handler.find_existing_headline(self.message_to_process):
               Info("Headline Already Recorded")
            else:
                db_handler.insert_headline(message)
                self.add_to_queue()
    def add_to_queue(self):
        print(self.q.maxsize)