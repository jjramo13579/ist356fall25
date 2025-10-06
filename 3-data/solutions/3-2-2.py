import requests
import json
import pandas as pd
import streamlit as st

st.title("Employee JSON")

link = "https://raw.githubusercontent.com/mafudge/datasets/master/json-samples/employees.json"
response = requests.get(link)
