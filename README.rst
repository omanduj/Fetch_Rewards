This project is a point managing system. The user inputs a user, the amount of points to add to their account
and the timestamp at the respective endpoint. User is then able to subtract points from the oldest timestamp
or add points for a given user. The user is then able to see all points entered at their given time and the total
amount of points for each user as well.
For endpoints with view functionality, please load the appropriate url
ex) http://127.0.0.1:5000/insert   -   for all user information
    http://127.0.0.1:5000/see_all_points   -   for total points for each user

To use activate the virtual environment in the main folder via command source venv/bin/activate
Install Flask and sqlite3
Then execute the following command: poetry run python fetch_rewards/my_code_http.py

Begin using service!

Example of viable request:
curl -X POST -H "Content-Type: application/json" -d '{"payer": "Joe", "points": "500", "time_zone": "2020-11-02T14:00:00Z"}' http://127.0.0.1:5000/insert
curl -X POST -H "Content-Type: application/json" -d '{"payer": "Joe", "points": "1000", "time_zone": "2020-1-02T14:00:00Z"}' http://127.0.0.1:5000/insert
curl -X POST -H "Content-Type: application/json" -d '{"payer": "Maria", "points": "50", "time_zone": "2021-17-02T14:00:00Z"}' http://127.0.0.1:5000/insert


curl -X POST -H "Content-Type: application/json" -d '{"payer" : "Joe", "points": "100"}' http://127.0.0.1:5000/update/subtract

curl -X POST -H "Content-Type: application/json" -d '{"payer" : "Maria", "points": "1000", "time_zone":"2020-11-02T14:00:00Z"}' http://127.0.0.1:5000/update/add






HTTP_METHOD - API ENDPOINT
Description of what happens

Input POST(/insert) -> Send payer name, points and date points were obtained to database
    {
    	'payer': 'string',
    	'points': int,
    	'timestamp': date,
    }
    Output GET(/insert) -> Retrieves all points added a given time for each user
        {
            'users': user_info
        }

POST(/update/subtract) -> Subtracts points from a given user from earliest obtained points
    {
        'payer': 'string',
        'points': int,
    }
POST(/update/add) -> Adds points to a user
    {
        'payer': 'string',
        'points': int,
        'timestamp': date,
    }
GET(/see_all_points)  -> Sum of points per user for all users
    {
        'users': user_info
    }
