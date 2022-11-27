import csv
import pandas as pd
import numpy as np
import math
from datetime import datetime as dt, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
pd.options.display.max_columns = None 

def driver_status(data,m):
    status = []
    for i in range(m):
    # If the user has no purchase in the current month
        if data[i] == 0:
            # If the user has made purchases before
            if len(status) > 0:
                # If the user is unregistered in the previous month
                if status[i-1] == "unreg":
                # The the user is also unregistered this month
                    status.append("unreg")
                # Otherwise the user is an active user, i.e., he/she already registered
                else:
                    status.append("inactive")
            # Otherwise the user is not registered in the current month, i.e., he/she has never made any purchases
            else:
                status.append("unreg")
        else:
            # This is the first purchase of the user
            if len(status) == 0:
                status.append("new")
            else:
                if status[i-1] == "inactive":
                    status.append("active")
                elif status[i-1] == "unreg":
                    status.append("new")
                else:
                    status.append("active")
    return status

    ### Needed functions
def get_col_name(row):    
    b = (df2.index[row.name] == row['value'])
    return b.index[b.argmax()]

def maxer(df,s=0,e=12):
    max_index = []
    for i in df.index.values:
      max_index.append(df.iloc[:,s:e].loc[str(i)].idxmax())
    return pd.Series(max_index, name = "max_month", index=df.index)

def maxer_2(df,s=0,e=12):
    max_index = []
    for i in df.index.values:
      max_index.append(df.iloc[:,s:e].iloc[i].idxmax())
    return pd.Series(max_index, name = "max_month", index=df.index)
def check_truck(val):
          val =  val.lower().replace('_'," ").replace("-"," ").split()
          if "jumbo" in val:
            return "jumbo"
          elif "dababa" in val:
            return "dababa"
          elif ("trella" in val)|("side" in val):
            return "trailer"
          elif "van" in val:
            return "van"