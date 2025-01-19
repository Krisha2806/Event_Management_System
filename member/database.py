import mysql.connector

#set your mysql password
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Darkri@1208",
    database="fest_management_system"
)

c = mydb.cursor()


def add_team(team_name, team_lead_id, fest_id, event_id):
    c.execute('INSERT INTO team (team_name, team_lead_id, fest_id,event_id) VALUES (%s,%s,%s, %s);', (team_name, team_lead_id, fest_id,event_id))
    mydb.commit()
    c.execute('UPDATE member SET team_id=(SELECT team_id FROM team WHERE (team_name=%s AND team_lead_id=%s AND fest_id=%s))', (team_name, team_lead_id, fest_id))
    mydb.commit()

def join_team(team_name, fest_id):
    c.execute('UPDATE member SET team_id=(SELECT team_id FROM team WHERE (team_name=%s AND fest_id=%s))', (team_name, fest_id))
    mydb.commit()

def leave_team(srn):
    c.execute('DELETE FROM member as m WHERE m.memb_srn=%s', (srn,))
    mydb.commit()


def view_team_db(srn):
    # c.execute('SELECT m.memb_name,m.memb_phone_num,m.memb_srn,m.memb_dob FROM fest_management_system.team AS t, fest_management_system.member AS m WHERE t.team_id = m.team_id;')
    c.execute('SELECT m.memb_name, m.memb_phone_num, m.memb_srn, m.memb_dob FROM member m JOIN team t ON m.team_id = t.team_id;')
    # mydb.commit()
    data = c.fetchall()
    return data

def add_event(event_name, event_price,conducting_team_id, event_venue_id, event_date, event_time,srn):
    c.execute('INSERT INTO event (event_name, event_price,conducting_team_id, event_venue_id, event_date, event_time) VALUES ( %s,%s,%s,%s,%s,%s);', (event_name, event_price,conducting_team_id, event_venue_id, event_date, event_time))
    mydb.commit()
    c.execute('UPDATE event SET conducting_team_id = (SELECT team_id FROM member WHERE member.memb_srn = %s);', (srn,))
    mydb.commit()

def view_event_db(srn):
    c.execute('SELECT e.event_name,e.event_price,v.venue_name, e.event_date FROM fest_management_system.event AS e,fest_management_system.venue AS v, fest_management_system.member AS m WHERE (e.conducting_team_id = m.team_id AND v.venue_ID=e.event_venue_id and m.memb_srn = %s );', (srn,))
    data = c.fetchall()
    return data


def close():
    c.close()
    mydb.close()
