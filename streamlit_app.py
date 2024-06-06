import streamlit as st
from psycopg2 import sql
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    DATABASE_URL = st.secrets("DATABASE_URL")
    engine = create_engine(DATABASE_URL)
    return engine

def fetch_bitcoin_data(engine):
    query ="SELECT * FROM bitcoin_data ORDER BY date"
    df=pd.read_sql(query, engine)
    return df

def fetch_bitcoin_news(engine):
    query ="SELECT * FROM bitcoin_news"
    df=pd.read_sql(query, engine)
    return df

