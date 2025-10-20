import pandas as pd
import streamlit as st


# Extract roster
roster_url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls/roster.csv"
roster_df = pd.read_csv(roster_url)
st.dataframe(roster_df)


# extract each poll
polls = []
dates =["2024-01-08", "2024-01-15", "2024-01-22", "2024-01-29"]
for date in dates:
    #read in each poll
    poll = f"https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls/poll-responses-{date}.csv"
    poll_df = pd.read_csv(poll)
    #add lineage to each poll by adding a date column
    poll_df['date'] = date
    #add poll to polls list
    #append to polls list
    polls.append(poll_df)
    
    
# combine all polls into one dataframe 
poll_df = pd.concat(polls, ignore_index=True)   
st.dataframe(poll_df)
st.dataframe(roster_df)


# Transformation
# join the roster to the polls , do a left join to capture absent students
combined_df = pd.merge(roster_df, poll_df, how='left', left_on='netid', right_on='student_id')
st.dataframe(combined_df)

poll_counts = combined_df.pivot_table(index ='date', values ='poll_num', aggfunc='max')
st.dataframe(poll_counts)