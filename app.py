import streamlit as st
import pandas as pd
import goalsXG 
import goalsVSyears as gy
import altair as alt
from streamlit_extras.let_it_rain import rain

st.header('Striker Analysis')
def rain(emoji="⚽", font_size=54, falling_speed=5):
    import streamlit as st
    import streamlit.components.v1 as components

    # CSS for the falling animation
    css = f"""
    <style>
        @keyframes fall {{
            0% {{ top: -10%; opacity: 1; }}
            100% {{ top: 100%; opacity: 0; }}
        }}
        .emoji {{
            position: fixed;
            font-size: {font_size}px;
            animation: fall {falling_speed}s linear 1 forwards;
        }}
    </style>
    """

    # JavaScript to create and animate the emojis
    js = f"""
    <script>
        function createEmoji() {{
            const area = document.createElement('div');
            area.classList.add('emoji');
            area.textContent = '{emoji}';
            document.body.appendChild(area);

            // Randomizing starting positions across the screen width
            area.style.left = `${{Math.floor(Math.random() * 100)}}vw`;
            area.style.top = '-10%';  // Start just above the screen
        }}

        // Create emojis for the first 3 seconds only
        const interval = setInterval(createEmoji, 300); // Adjust time here to control the frequency of emojis appearing

        // Stop the rain after 3 seconds
        setTimeout(() => {{
            clearInterval(interval);
        }}, 3000);  // Stop after 3 seconds
    </script>
    """

    # Combine CSS and JS with an empty HTML body
    html = f'<html><head>{css}</head><body></body>{js}</html>'

    # Use Streamlit's components to inject the custom HTML
    components.html(html, height=600)



def example():
    if 'initiated' not in st.session_state:
        rain(emoji="⚽", font_size=54, falling_speed=5)
        st.session_state['initiated'] = True 


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


#lizeth was here