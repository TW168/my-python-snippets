import pandas as pd
import sqlalchemy
import configparser
from datetime import datetime

def get_db_connection(database_name, section=None):
    """
    Establish a connection to a MySQL database using SQLAlchemy and Pandas,
    reading parameters from a .config.ini file.
    
    Parameters:
        database_name (str): The target database to connect to.
        section (str, optional): The section in the .config.ini file to read connection parameters from.
                                 If None, it defaults to the first available section.
    
    Returns:
        sqlalchemy.engine.base.Engine: A SQLAlchemy engine object.
    """
    # Read database configuration from .config.ini
    config = configparser.ConfigParser()
    config.read(".config.ini")
    
    # If section is None, use the first available section
    if section is None:
        section = config.sections()[0] if config.sections() else None
    
    if not section or section not in config:
        raise ValueError(f"Section '{section}' not found in configuration file.")
    
    user = config.get(section, "user")
    password = config.get(section, "password")
    host = config.get(section, "host")
    port = config.get(section, "port", fallback="3306")
    
    # Create connection string
    connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database_name}"
    
    # Create SQLAlchemy engine
    engine = sqlalchemy.create_engine(connection_string)

    # Print connection message with timestamp
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{current_time}] Connected to database '{database_name}' using section '{section}'")
    return engine

def fetch_data(query, database_name, section=None):
    """
    Fetch data from a given MySQL database and return it as a Pandas DataFrame.
    
    Parameters:
        query (str): SQL query to execute.
        database_name (str): The database from which to fetch data.
        section (str, optional): The section in the .config.ini file to read connection parameters from.
                                 If None, it defaults to the first available section.
    
    Returns:
        pd.DataFrame: A Pandas DataFrame containing the query results.
    """
    engine = get_db_connection(database_name, section)
    return pd.read_sql(query, con=engine)



# Example usage:
# qry = f"SELECT * FROM ipg_ez limit 100"
# df = fetch_data(qry, database_name="ws_hub")
# print(df.head())
