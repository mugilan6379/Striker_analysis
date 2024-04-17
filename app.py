import streamlit as st
import pandas as pd
import goalsXG 
import goalsVSyears as gy
import altair as alt

st.header('Striker Analysis')


def load_data(csv):
    df = pd.read_csv(csv)
    return df
main_file=load_data('StrikerAnalysis.csv')


def modify_file(main_file):
    main_file=main_file[(main_file['Year']>=2018)]
    #top 4 leagues only
    main_file=main_file[
        (main_file['League']=='La Liga') | 
        (main_file['League']=='Premier League') |
        (main_file['League']=='Bundesliga') |
        (main_file['League']=='Serie A')
    ]
    #player_goals = main_file.groupby('Player Names')['Goals'].sum().reset_index()
    main_file=main_file.drop(columns=['Year'])
    return main_file
   
main_file=modify_file(main_file)

tab1,tab2=st.tabs(['Goals in each year as per leagues(line chart)','Goals vs XG(Scatter plot)'])

with tab1:
    main_file=pd.read_csv('StrikerAnalysis.csv')
    
    main_file=main_file[
        (main_file['League']=='La Liga') | 
        (main_file['League']=='Premier League') |
        (main_file['League']=='Bundesliga') |
        (main_file['League']=='Serie A')
    ]
    grouped_data=main_file.groupby(['League','Year'])['Goals'].sum().reset_index()
    grouped_data['Year'] = grouped_data['Year'].astype(int)
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
    st.altair_chart(line)
    st.write(grouped_data)

with tab2:
    goalsXG.goalsVsXG(main_file)