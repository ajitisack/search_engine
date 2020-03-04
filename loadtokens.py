import subprocess
import pandas as pd
import dbconnection as db


def loadtokens_windows():
    tblname = db.DBNAME + "." + db.SCHEMA + ".tokens1"
    filename =  "tokens.csv"
    bcp_cmd = 'bcp "' + tblname + '" in ' + filename + ' -S "' + db.DBSERVER + '" -t"," -c -T'
    subprocess.call(bcp_cmd, shell=True)

