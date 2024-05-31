import os
import sys
from src.mlproject.logger import logging
from src.mlproject.exception import CustomerException
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_data_from_sql():
    logging.info("Reading SQL database started")
    try:
        mydb = pymysql.connect(
            host = host,
            user = user,
            password = password,
            db = db
        )
        logging.info("Connection Established", mydb)
        df = pd.read_sql_query('Select * from students', mydb)
        return df
        print(df.head())
        
    except Exception as e:
        raise CustomerException(e)