import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# data needs to be cleaned up :-( not uncommon
ff = pd.read_csv("./6-viz/data/fast_food_nutrition_cleaned.csv")
