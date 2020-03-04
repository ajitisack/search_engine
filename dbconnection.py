import pyodbc
import pandas as pd

DBSERVER = "cil-sql-syst\INST101"
DBNAME = "d5bsc1"
SCHEMA = "[nt0001\\bd3043]"

def create_db_conn(database="MSSQL"):
    """ Create a connection to SQL Server and return connection string """
    conn_string = "Driver={SQL Server Native Client 11.0};Server=" + DBSERVER + ";Database=" + DBNAME + ";Trusted_Connection=yes;"
    conn = pyodbc.connect(conn_string)
    return conn

    