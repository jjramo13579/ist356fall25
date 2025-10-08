import pandas as pd
import streamlit as st


from check_functions import clean_currency

st.title("Dining Check Data")

# load
checks = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv')

# transformations
checks['total_amount_of_check_cleaned'] = ???
checks['gratuity_cleaned'] = ????

checks['price_per_item'] = ???
checks['price_per_person'] = ???
checks['items_per_person'] = ???
checks['tip_percentage'] = ???

st.dataframe(checks, width=1000)

# display
col1,col2,col3,col4 = st.columns(4)

col1.metric("Average Price Per Item", checks['price_per_item'].mean())
col2.metric("Average Price Per Person", checks['price_per_person'].mean())
col3.metric("Average Items Per Person", checks['items_per_person'].mean())
col4.metric("Average Tip Pct", checks['tip_percentage'].mean())

st.dataframe(checks.describe())