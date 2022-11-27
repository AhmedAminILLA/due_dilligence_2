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