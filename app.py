import mysql.connector 
import re

def add_user(ID, username, password, email, pnumber):
    ok = True
    # check if ID is unique
    query = "SELECT ID FROM USERS WHERE ID = %s"
    values = (ID)
    cur.execute(query, values)
    if cur.fetchone() is not None:
        ok = False
    # check if phone number is of the form 123-456-7890
    if not re.match(r"^\d{3}-\d{3}-\d{4}$", pnumber):
        ok = False
    if(ok == True):
        query = "INSERT INTO USERS (ID, username, password, email, pnumber) VALUES (%s, %s, %s, %s, %s)" 
        values = (ID, username, password, email, pnumber)
        cur.execute(query, values)
        cnx.commit()

def delete_user(ID):
    ok = True
    # check if ID exists
    query = "SELECT ID FROM USERS WHERE ID = %s"
    values = (ID)
    cur.execute(query, values)
    if cur.fetchone() is None:
        ok = False
    if(ok == True):
        query = "DELETE FROM USERS WHERE ID = %s" 
        values = (ID)
        cur.execute(query, values)
        cnx.commit()
    else:
        print("Error: deleting a user failed")

def add_team(ID, teamname, leader, teamdescription):
    ok = True
    # check if team_ID is unique
    query = "SELECT team_ID FROM TEAMS WHERE team_ID = %s"
    values = (ID)
    cur.execute(query, values)
    if cur.fetchone() is not None:
        ok = False
    # check if team_leader exists
    query = "SELECT ID FROM USERS WHERE ID = %s"
    values = (leader)
    cur.execute(query, values)
    if cur.fetchone() is None:
        leader = None
    if(ok == True):
        query = "INSERT INTO TEAMS (team_ID, team_name, team_leader, team_desc) VALUES (%s, %s, %s, %s)" 
        values = (ID, teamname, leader, teamdescription)
        cur.execute(query, values)
        cnx.commit()
    else:
        print("Error: inserting a team failed")

def delete_team(ID):
    ok = True
    # check if team_ID exists
    query = "SELECT team_ID FROM TEAMS WHERE team_ID = %s"
    values = (ID)
    cur.execute(query, values)
    if cur.fetchone() is None:
        ok = False
    if(ok == True):
        query = "DELETE FROM TEAMS WHERE team_ID = %s" 
        values = (ID)
        cur.execute(query, values)
        cnx.commit()
    else:
        print("Error: deleting a team failed")

def add_task(ID, user_ID, title, desc, stat, due_date, priority):
    ok = True
    super_ok = True

    # check if task_ID is unique
    query = "SELECT task_ID FROM TASKS WHERE task_ID = %s"
    values = (ID)
    cur.execute(query, values)
    if cur.fetchone() is not None:
        ok = False
        super_ok = False
    # check if user_ID exists
    query = "SELECT ID FROM USERS WHERE ID = %s"
    values = (user_ID)
    cur.execute(query, values)
    if cur.fetchone() is None:
        ok = False
        super_ok = False
    #  check if date is 4 numbers then a dask then 2 numbers then a dash then 2 numbers
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", due_date):
        ok = False
        due_date = "0000-00-00"
    #  check is description is less than 1000 characters
    if len(desc) > 1000:
        ok = False
        desc = desc[:1000]
    # check if title is less than 255 characters
    if len(title) > 255:
        ok = False
        title = title[:255]
    # check if status is less then 255 characters
    if len(stat) > 255:
        ok = False
        stat = stat[:255]
    #  check if priority is a num
    if not priority.isdigit():
        ok = False
        priority = 0
    if(ok == True):
        query = "INSERT INTO TASKS (task_ID, user_ID, title, description, status, due_date, priority) VALUES (%s, %s, %s, %s, %s, %s)" 
        values = (ID, user_ID, title, desc, stat, due_date, priority)
        cur.execute(query, values)
        cnx.commit()
    elif(ok == False and super_ok == True):
        query = "INSERT INTO TASKS (task_ID, user_ID, title, description, status, due_date, priority) VALUES (%s, %s, %s, %s, %s, %s)" 
        values = (ID, user_ID, title, desc, stat, due_date, priority)
        cur.execute(query, values)
        cnx.commit()
    else:
        print("Error: inserting a task failed")

def update_stat(task_ID, stat):
    ok = True
    # check if task_ID exists
    query = "SELECT task_ID FROM TASKS WHERE task_ID = %s"
    values = (task_ID)
    cur.execute(query, values)
    if cur.fetchone() is None:
        ok = False
    # check if status is less then 255 characters
    if len(stat) > 255:
        stat = stat[:255]
    if(ok == True):
        query = "UPDATE TASKS SET status = %s WHERE task_ID = %s" 
        values = (stat, task_ID)
        cur.execute(query, values)
        cnx.commit()
    else:
        print("Error: updating a task status failed")


if __name__ == "__main__":
  
    #Connect to Database
    user = 'tom'
    password = 'password'
    cnx = mysql.connector.connect(
    host ="127.0.0.1",
    port = 3306,
    user = user,
    password = password)

    #Cursor
    cur = cnx.cursor()

    #sql Database
    cur.execute("use todo")

    

    cnx.close()