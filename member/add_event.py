import streamlit as st
from member.database import add_event
# from member.database import join_event

def adding_event(srn):
    col1, col2 = st.columns(2)
    with col1:
        event_name = st.text_input("Event Name: ")
        event_price = st.text_input("Event Price:")
        conducting_team_id = st.text_input("Conducting Team ID:")
    with col2:
        event_venue_id = st.text_input("Event Venue ID:")
        event_date = st.text_input("Event Date:")
        event_time = st.text_input("Event Time:")
    if st.button("Add Event"):
        add_event(event_name, event_price,conducting_team_id, event_venue_id, event_date, event_time,srn)
        st.success("Successfully added Event: {}".format(event_name))

# def joining_team(srn):
#     col1, col2 = st.columns(2)
#     with col1:
#         team_name = st.text_input("Team Name: ")
#         fest_id = st.text_input("Fest ID:")
#     if st.button("Join Team"):
#         join_team(team_name, fest_id)
#         st.success("Successfully joined Team/Project: {}".format(team_name))
#
# def view_team_db(srn):
#     c.execute('SELECT t.team_id, t.team_name, t.team_lead_id, t.fest_id, t.event_id FROM fest_management_system.team AS t JOIN fest_management_system.member AS m ON t.team_id = m.team_id WHERE m.memb_srn = %s;', (srn,))
#     data = c.fetchall()
#     return data
