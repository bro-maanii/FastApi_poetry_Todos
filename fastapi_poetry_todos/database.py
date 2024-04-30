from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://alie15425:WgFoO1ylnI7d@ep-noisy-bread-a15xrk5r.ap-southeast-1.aws.neon.tech/FastApi_Todo?sslmode=require"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
