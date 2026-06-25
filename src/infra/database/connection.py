import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

user = os.getenv("USER")
password = os.getenv("PASSWORD")
host = os.getenv("HOST")
port = os.getenv("PORT")
database = os.getenv("DATABASE")

def conection_db():
    engine = create_engine(
        f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    )

    if engine:    
        with engine.connect() as conn:
            print("Connected to the DB")
    else:
        print("Error to conected to database!")

    return