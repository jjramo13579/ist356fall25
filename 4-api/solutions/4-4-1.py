from fastapi import FastAPI, Query
import pandas as pd
import numpy as np
import json
app = FastAPI()

#df = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/flights/sample-flights.csv")


#load data 

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/flights/sample-flights.csv"
df = pd.read_csv(url)

