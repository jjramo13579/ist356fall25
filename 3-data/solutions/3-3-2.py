import streamlit as st
import pandas as pd
import requests
import numpy as np


import streamlit as st
import pandas as pd

base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/"
months = ['jan', 'feb', 'mar', 'apr']

st.title("Who's not Buying from MiniMart?")