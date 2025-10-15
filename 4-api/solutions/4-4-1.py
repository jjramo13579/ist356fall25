from fastapi import FastAPI, Body, HTTPException
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/flights/sample-flights.csv")
app = FastAPI()


