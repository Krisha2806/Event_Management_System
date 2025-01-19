import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


from member.add_team import adding_team
from member.add_team import joining_team
from member.view_team import view_team
from member.add_event import adding_event
from member.view_event import view_event
from member.leave_team import leaving_team

from participant.view_event import view_all_events
from participant.join_event import joining_event
from participant.view_event import view_my_events

st.title("PES University")
st.header("College Fest Management System")

is_login = False # Variable to check if the user has logged in
with open('users.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    with open('users.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    user_type = config['credentials']['usernames'].get(username, {}).get('type', None)
    is_login = True
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

srn = username

# User priviledges on frontend after login for student
if is_login and user_type=='Member':
    menu = ["Dashboard", "Add Team","Join Team", "View Team","Add Event", "View my Events","Leave Team" ]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice=="Dashboard":
        st.subheader(f'Welcome *{name} ({user_type})*')
        authenticator.logout('Logout', 'main')
    elif choice=="Add Team":
        st.divider()
        st.subheader("Add your Team")
        adding_team(srn)
    elif choice=="View Team":
        st.divider()
        st.subheader("View your Team")
        view_team(srn)
    elif choice=="Join Team":
        st.divider()
        st.subheader("Join a Team")
        joining_team(srn)
    elif choice=="Add Event":
        st.divider()
        st.subheader("Add Event")
        adding_event(srn)
    elif choice=="View my Events":
        st.divider()
        st.subheader("Your Events")
        view_event(srn)
    elif choice=="Leave Team":
        st.divider()
        st.subheader("Leave Team")
        leaving_team(srn)


if is_login and user_type=='Participant':
    menu = ["Dashboard", "Join an Event", "My Registrations"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice=="Dashboard":
        st.subheader(f'Welcome {name} ({user_type})')
        authenticator.logout('Logout', 'main')
    elif choice == "Join an Event":
        st.subheader("All existing events:")
        view_all_events(srn)
        st.subheader("Join any event:")
        joining_event(srn)
    elif choice == "My Registrations":
        st.subheader("Your Registrations:")
        view_my_events(srn)

    else:
        st.subheader("About tasks")
