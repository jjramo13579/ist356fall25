import requests

'''
Post curl here

'''



import pandas as pd
import numpy as np

import streamlit as st
import requests
import json 



def extract_entities(text: str)->dict:
    '''
    Extract entities from the text using Azure entity recognition API.
    '''
    
# Complete function 


text = st.text_area("Enter text to extract entities:")

# Complete code to call the function and display results  