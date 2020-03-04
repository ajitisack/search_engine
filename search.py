import sys
import pandas as pd
import dbconnection as db
import tokenizer as ts


def search(search_query):
    """ Searches for normalized words in the search query in tokens table and 
    returns the doc name in the descending order of sum(freq) of query words"""
    keywords = "','".join(ts.tokenizer(search_query))
    db_conn = db.create_db_conn("MSSQL")
    tblname = f"{db.DBNAME}.{db.SCHEMA}.tokens"    
    sql = f""\
    f"SELECT doc, sum(freq) "\
    f"FROM {tblname} "\
    f"where token in ('{keywords}') "\
    f"group by doc "\
    f"order by 2 desc"
    print(sql)
    df = pd.read_sql_query(sql, db_conn)
    return(df)


def main():
    search(sys.argv[1])


if __name__ == '__main__':
    main()