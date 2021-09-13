from flask import Flask, url_for, request, jsonify
from fetch_database import select_info, insert_info, update_info_sub, update_info_add, base_set_up, group_users_by_name



app = Flask(__name__)

@app.route("/insert", methods = ["POST"])
def main():
    """Purpose: To insert information sent by user to database
       Paramaters: None, just the HTTP post information
       Return Value: A jsonified list of user data
    """
    base_set_up()
    information = request.get_json()
    payer = information['payer']
    points = information['points']
    time_zone = information['time_zone']
    insert_info(payer, points, time_zone[:10])

    return(
    jsonify({
        "payer": payer,
        "points": points,
        "time_zone": time_zone
        }))

@app.route("/insert", methods = ["GET"])
def main2():
    """Purpose: To show all data stored in database
       Paramaters: None
       Return Value: A jsonified list of all user data
    """
    user_info = select_info()

    return(
    jsonify({
        'users': user_info
        }))

@app.route("/update/subtract", methods = ["POST"])
def main3():
    """Purpose: To subtract a given number of points from a given user
       Paramaters: None
       Return Value: A jsonified list of user data
    """
    information = request.get_json()
    payer = information['payer']
    points = information['points']
    update_info_sub(payer, points)

    return(
    jsonify({
        "payer": payer,
        "points": points,
        }))

@app.route("/update/add", methods = ["POST"])
def main4():
    """Purpose: To add a given number of points to a given user
       Paramaters: None
       Return Value: A jsonified list of user data
    """
    information = request.get_json()
    payer = information['payer']
    points = information['points']
    time_zone = information['time_zone']
    update_info_add(payer, points, time_zone)

    return(
    jsonify({
        "payer": payer,
        "points": points,
        "time_zone": time_zone
        }))

@app.route("/see_all_points", methods = ["GET"])
def main5():
    """Purpose: To see the total points of all users. For example if two entries of 100 for
                Tim, this will show Tim 200
       Paramaters: None
       Return Value: A jsonified list of user data
    """
    users_info = group_users_by_name()

    return(
    jsonify({
        "info": users_info
        }))

app.run(debug=True)
