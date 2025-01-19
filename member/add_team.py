import streamlit as st
from member.database import add_team
from member.database import join_team

def adding_team(srn):
    col1, col2 = st.columns(2)
    with col1:
        team_name = st.text_input("Team Name: ")
        team_lead_id = st.text_input("Team Lead ID:")
    with col2:
        event_id = st.text_input("Event ID:")
        fest_id = st.text_input("Fest ID:")
    # domain_id = st.number_input("Domain ID:", min_value=0, step=1)
    if st.button("Add Team"):
        add_team(team_name, team_lead_id, fest_id,event_id)
        st.success("Successfully added Team: {}".format(team_name))

def joining_team(srn):
    col1, col2 = st.columns(2)
    with col1:
        team_name = st.text_input("Team Name: ")
        fest_id = st.text_input("Fest ID:")
    if st.button("Join Team"):
        join_team(team_name, fest_id)
        st.success("Successfully joined Team: {}".format(team_name))

def view_team_db(srn):
    c.execute('SELECT t.team_id, t.team_name, t.team_lead_id, t.fest_id, t.event_id FROM fest_management_system.team AS t JOIN fest_management_system.member AS m ON t.team_id = m.team_id WHERE m.memb_srn = %s;', (srn,))
    data = c.fetchall()
    return data
