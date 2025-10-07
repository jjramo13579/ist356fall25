import streamlit as st
import pandas as pd
from check_functions import clean_currency, detect_whale, detect_tipper

from check_functions import clean_currency, detect_whale, detect_tipper

st.title("Dining Check Data")

#load
checks = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv')

