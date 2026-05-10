from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)

app.secret_key = "travelplanner"

# LOGIN

@app.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('travel.db')
        cursor = conn.cursor()

        cursor.execute('''
        SELECT * FROM users
        WHERE username=? AND password=?
        ''', (username, password))

        user = cursor.fetchone()

        conn.close()

        if user:

            session['user'] = username

            return redirect('/planner')

        else:

            return "Invalid Login"

    return render_template('login.html')


# REGISTER

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('travel.db')
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
        ''', (username, password))

        conn.commit()

        conn.close()

        return redirect('/')

    return render_template('register.html')


# PLANNER

@app.route('/planner', methods=['GET', 'POST'])
def planner():

    itinerary = []
    hotel = ""
    total_price = 0

    foods = []
    activities = []

    if request.method == 'POST':

        destination = request.form['destination']
        days = int(request.form['days'])
        people = int(request.form['people'])
        budget = request.form['budget']

        conn = sqlite3.connect('travel.db')
        cursor = conn.cursor()

        # FETCH PLACES

        cursor.execute('''
        SELECT place_name
        FROM places
        WHERE city=?
        ''', (destination,))

        places_data = cursor.fetchall()

        places = [item[0] for item in places_data]

        # FETCH HOTEL

        cursor.execute('''
        SELECT hotel_name, price_per_person
        FROM hotels
        WHERE city=? AND budget_type=?
        ''', (destination, budget))

        hotel_data = cursor.fetchone()

        # FETCH FOOD

        cursor.execute('''
        SELECT restaurant
        FROM food_places
        WHERE city=?
        ''', (destination,))

        foods_data = cursor.fetchall()

        foods = [item[0] for item in foods_data]

        # FETCH ACTIVITIES

        cursor.execute('''
        SELECT activity
        FROM activities
        WHERE city=?
        ''', (destination,))

        activities_data = cursor.fetchall()

        activities = [item[0] for item in activities_data]

        conn.close()

        # HOTEL PRICE

        if hotel_data:

            hotel = hotel_data[0]

            hotel_price = hotel_data[1]

            total_price = hotel_price * people * days

        # DAY-WISE ITINERARY

        if len(places) > 0:

            for i in range(days):

                if i < len(places):

                    itinerary.append([places[i]])

                else:

                    itinerary.append(["Free Day / Shopping / Relax"])

    return render_template(
        'index.html',
        itinerary=itinerary,
        hotel=hotel,
        total_price=total_price,
        foods=foods,
        activities=activities
    )


if __name__ == '__main__':
    app.run(debug=True)