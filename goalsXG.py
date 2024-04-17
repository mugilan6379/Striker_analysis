import streamlit as st
import pandas as pd
import altair as alt

import ScatterPlot

def goalsVsXG(main_file):
    main_file=main_file[['Player Names','Goals','X G']]
    main_file=main_file.groupby('Player Names').agg(
        {
            'X G' : 'sum',
            'Goals' : 'sum'
            
        }
    ).reset_index().sort_values(by='Goals',ascending=False).head(15)
    return st.altair_chart(ScatterPlot.scatter_plot(main_file,'Goals','X G','Goals vs XG'))
    