import pandas as pd
import streamlit as st


from participant.database import view_all_events_db
from participant.database import view_my_events_db
from participant.database import show_event_db


def view_all_events(srn):
    result = view_all_events_db(srn)
    df = pd.DataFrame(result, columns=['Event Name','Event Price', 'Event Venue','Event Date' ])
    st.dataframe(df)

def show_event(event_name):
    result = show_event_db(event_name)
    df = pd.DataFrame(result, columns=['Event Name','Event Price', 'Event Venue','Event Date' ])
    st.dataframe(df)

def view_my_events(event_name):
    result = view_my_events_db(event_name)
    df = pd.DataFrame(result, columns=['Event Name','Event Price', 'Event Venue','Event Date' ])
    st.dataframe(df)
