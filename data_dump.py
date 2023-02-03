import pymongo
import pandas as pd
import json 

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH=("/config/workspace/Metro_Interstate_Traffic_Volume.csv")

DATABASE_NAME= "Interstate"

COLLECTION_NAME="Traffic"

if __name__ =="__main__":
    data=pd.read_csv(DATA_FILE_PATH)
    print(F"rows & columns :{data.shape}")

#convert dataframe to json format
    data.reset_index(drop=True,inplace=True)
    json_record=list(json.loads(data.T.to_json()).values())
    print(json_record[0])

#inserting json record into mongodb database
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)