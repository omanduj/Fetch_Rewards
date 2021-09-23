import sqlite3
import json


def base_set_up():
    """Purpose: To set up sqlite3 database
       Paramaters: None
       Return Value: None
    """
    conn = sqlite3.connect("fetch_rewards.db")
    c = conn.cursor()

    c.execute("""DROP TABLE IF EXISTS fetch_rewards""")

    c.execute("""CREATE TABLE fetch_rewards (
                id integer primary key autoincrement,
                payer text,
                points integer,
                time_zone date
            ) """)

    conn.commit()
    conn.close()

def insert_info(payer, points, time_zone):
    """Purpose: To insert user info into database
       Paramaters: payer = the name of a user, points = the amounts the user has and
                            time_zone = the time points were obtained
       Return Value: None
    """
    conn = sqlite3.connect("fetch_rewards.db")
    c = conn.cursor()

    c.execute("INSERT INTO fetch_rewards (payer, points, time_zone) VALUES (:payer, :points, :time_zone)",
                {'payer': payer, 'points': points, 'time_zone': time_zone})

    conn.commit()
    conn.close()


def update_info_sub(points):
    """Purpose: To update a given users information when points are used
       Paramaters: payer = the name of a user, points = the amounts the user has and
                            time_zone = the time points were obtained
       Return Value: None
    """
    conn = sqlite3.connect("fetch_rewards.db")
    c = conn.cursor()

    points_db = c.execute("SELECT SUM(points) FROM fetch_rewards")
    points_db = points_db.fetchone()

    if(points_db[0] - int(points) >= 0):
        c.execute("UPDATE fetch_rewards SET points = (points - '{}') WHERE time_zone = (SELECT MIN(time_zone) FROM fetch_rewards)".format(points))
    if (points_db[0] - int(points) <= 0):
        return "error"
    conn.commit()
    conn.close()

def update_info_add(payer, points, time_zone):
    """Purpose: To update a given users information when points are added
       Paramaters: payer = the name of a user, points = the amounts the user has and
                            time_zone = the time points were obtained
       Return Value: None
    """
    conn = sqlite3.connect("fetch_rewards.db")
    c = conn.cursor()

    c.execute("UPDATE fetch_rewards SET points = (points + '{}') WHERE payer = '{}' AND time_zone = (SELECT MIN(time_zone) FROM fetch_rewards)".format(points, payer))

    conn.commit()
    conn.close()

def group_users_by_name():
    """Purpose: To return all points of a given user
       Paramaters: None
       Return Value: information = all the points summed for each user
    """
    conn = sqlite3.connect("fetch_rewards.db")
    c = conn.cursor()

    user_info = c.execute("SELECT payer, SUM(points) FROM fetch_rewards GROUP BY payer")
    info = user_info.fetchall()

    conn.commit()
    conn.close()
    return info

def select_info():
    """Purpose: To show all users, points, and date added for each user
       Paramaters: None
       Return Value: information = all information stored about all users
    """
    conn = sqlite3.connect("fetch_rewards.db")
    c = conn.cursor()

    requested_info = c.execute("SELECT * FROM fetch_rewards")
    information = c.fetchall()

    conn.commit()
    conn.close()

    return information

def main_DB(payer, points, time_zone):
    """Purpose: To execute above functions in testing environment
       Paramaters: payer = the name of a user, points = the amounts the user has and
                            time_zone = the time points were obtained
       Return Value: requested_info = information that was requested/being tested
    """
    # base_set_up()
    x = insert_info(payer, points, time_zone)
    # update_info_sub("Oscar", 10)
    # x = select_info()
    x = select_info()
    return x
