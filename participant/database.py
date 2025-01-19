import mysql.connector
import streamlit as st

#set your mysql password
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Darkri@1208",
    database="fest_management_system"
)

c = mydb.cursor()

def join_event(event_name,srn):

    c.execute('INSERT INTO participants (part_name, part_phone_num, event_id, part_dob, part_srn)'
          'SELECT p.part_name, p.part_phone_num, e.event_id, p.part_dob, %s '
          'FROM participants p, event e '
          'WHERE p.part_srn = %s AND e.event_name = %s',
          (srn, srn, event_name))
    mydb.commit()
    st.success("Successfully joined Event: {}".format(event_name))

def view_all_events_db(srn):
    c.execute('SELECT DISTINCT e.event_name,e.event_price,v.venue_name, e.event_date FROM fest_management_system.event AS e,fest_management_system.venue AS v WHERE (v.venue_ID=e.event_venue_id);')
    data = c.fetchall()
    return data

def view_my_events_db(srn):
    c.execute('SELECT DISTINCT e.event_name,e.event_price,v.venue_name, e.event_date FROM fest_management_system.event AS e,fest_management_system.venue AS v, fest_management_system.participants as p WHERE (v.venue_ID=e.event_venue_id and p.part_srn=%s and p.event_id = e.event_id );',(srn,))
    data = c.fetchall()
    return data

def show_event_db(event_name):
    c.execute('SELECT DISTINCT e.event_name,e.event_price,v.venue_name, e.event_date FROM fest_management_system.event AS e,fest_management_system.venue AS v WHERE (v.venue_ID=e.event_venue_id and e.event_name=%s);', (event_name,))
    data = c.fetchall()
    return data

def close():
    c.close()
    mydb.close()
