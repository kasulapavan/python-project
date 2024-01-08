from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Replace "your_host" with the actual host, and "sense_db" with your database name
host = "localhost"
database_name = "python_project_db"
user = "postgres"
password = "thrymr@123"

# URL-encode the password
encoded_password = quote_plus(password)

# Creating the connection string
dsn = f"postgresql://{user}:{encoded_password}@{host}/{database_name}"

# Creating the SQLAlchemy engine
engine = create_engine(dsn, echo=True)

Base = declarative_base()
SessionLocal = sessionmaker(engine)