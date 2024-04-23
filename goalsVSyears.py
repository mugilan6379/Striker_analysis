import streamlit as st
import pandas as pd
import altair as alt
import app

def goalsvsyears(df_file): 
    main_file=pd.read_csv('StrikerAnalysis.csv')
    
    main_file=main_file[
        (main_file['League']=='La Liga') | 
        (main_file['League']=='Premier League') |
        (main_file['League']=='Bundesliga') |
        (main_file['League']=='Serie A')
    ]
    grouped_data=main_file.groupby(['League','Year'])['Goals'].sum().reset_index()
    grouped_data['Year'] = grouped_data['Year'].astype(int)
    st.write(grouped_data)
    line = alt.Chart(grouped_data).mark_line().encode(
    x=alt.X('Year:O', axis=alt.Axis(format='')),
    y='Goals',
    color='League:N',
    tooltip=['Year','Goals','League']
    ).properties(
        width=600,
        height=500,
        title='Goals scored on each leagues for every years'
    )

    st.write('Goals vs Years Chart')
    return st.altair_chart(line)

#Lekha was here