import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import pymysql

pymysql.install_as_MySQLdb()
import MySQLdb

#연결
connect = create_engine('mysql+mysqldb://root:admin@localhost/parkhs')

dataframe = pd.read_sql_table('dbms', connect)
print(dataframe)