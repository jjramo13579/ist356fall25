import pandas as pd
import numpy as np
import requests
import streamlit as st


link ="https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json"
response = requests.get(link)
employees = response.json()
st.write(employees) # this will show the dictionary


