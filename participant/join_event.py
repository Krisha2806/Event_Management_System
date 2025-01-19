import streamlit as st
from participant.database import view_all_events_db
from participant.view_event import show_event
from participant.database import join_event

def joining_event(srn):
    col1,col2 = st.columns(2)
    with col1:
        event_name = st.text_input("Event Name: ")
        # part_phone_num = st.text_input("Phone Number: ")
        # part_dob = st.text_input("DOB: ")

    if st.button("Show event detail"):
        show_event(event_name)
    if st.button("Join Event"):
        join_event(event_name,srn)


