import streamlit as st
import pandas as pd
import requests
import numpy as np


base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/"
months = ['jan', 'feb', 'mar', 'apr']

st.title("Who's not Buying from MiniMart?")
month = st.selectbox('Select Month:', months)

purchases = pd.read_csv(f"{base}/purchases-{month}.csv")

# Code here...