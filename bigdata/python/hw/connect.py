import pandas as pd
import sqlalchemy as sql
from sqlalchemy import create_engine
from sqlalchemy import text

print(sql.__version__)
engine = create_engine('mysql+pymysql://root:password123!@localhost:3306', echo=True)

def check_for_db():
    with engine.connect() as conn:
        res = conn.execute(text("CREATE DATABASE IF NOT EXISTS test;"))
        print(res.closed)

check_for_db()


