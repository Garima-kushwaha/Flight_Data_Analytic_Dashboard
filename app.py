import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px

db = DB()

st.sidebar.title('Flights Analytics')

user_option = st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')

    col1,col2 = st.columns(2)

    source_city = db.fetch_source_city_names()
    dest_city = db.fetch_dest_city_names()

    with col1:
        source = st.selectbox('Source',sorted(source_city))
    with col2:
        destination = st.selectbox('Destination', sorted(dest_city))

    if st.button('Search'):
        results = db.fetch_all_flights(source,destination)
        st.dataframe(results)

elif user_option == 'Analytics':
    airline, frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.header("Airline Pie chart")

    st.plotly_chart(fig)

    city, frequency1 = db.busy_airport()
    fig = px.bar(
        x=city,
        y=frequency1
    )
    st.markdown("## Busiest Airport")

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    date, frequency2 = db.daily_frequency()

    print(len(date))
    print(len(frequency2))
    fig = px.line(
        x=date,
        y=frequency2
    )

    st.markdown("## Daily Number of  Flights")

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

else:
    st.title('About the project')

    st.header("Overview")
    st.write(
        "The Flight Data Analytics Dashboard provides a comprehensive tool for analyzing flight data using SQL and Streamlit. SQL queries are employed to retrieve data from the database, which is then presented in the form of an interactive dashboard.")

    st.header("User-Friendly Interface")
    st.write(
        "Streamlit is utilized to create a user-friendly interface, enabling users to easily select specific criteria and generate customized insights. This intuitive design enhances the user experience, making it effortless to interact with the data.")

    st.header("Key Features ")
    st.subheader("Airline Frequencies")
    st.write("User can explore the frequencies of different airlines to gain insights into their operational activities.")

    st.subheader("Busy Airports")
    st.write(
        "Busy airports can be identified and analyzed their traffic patterns to understand their significance in the aviation network.")

    st.subheader("Daily Flight Trends")
    st.write(
        "Examination can be done of daily flight trends to uncover patterns and fluctuations in flight schedules and passenger traffic.")

