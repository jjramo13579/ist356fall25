import pandas as pd
import numpy as np
import streamlit as st

link = 'https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv'

st.title('My first dataframe')

customers = pd.read_csv(link)


