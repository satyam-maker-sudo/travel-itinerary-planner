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

    if request.method == 'POST':

        destination = request.form['destination']
        days = int(request.form['days'])
        people = int(request.form['people'])
        budget = request.form['budget']

        conn = sqlite3.connect('travel.db')

        cursor = conn.cursor()

        # FETCH PLACES

        cursor.execute('''
        SELECT place_name FROM places
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

        conn.close()

        if hotel_data:

            hotel = hotel_data[0]

            hotel_price = hotel_data[1]

            total_price = hotel_price * people * days

        # ITINERARY

        if len(places) > 0:

            places_per_day = max(1, len(places)//days)

            for i in range(days):

                start = i * places_per_day
                end = start + places_per_day

                day_places = places[start:end]

                if day_places:
                    itinerary.append(day_places)

    return render_template(
        'index.html',
        itinerary=itinerary,
        hotel=hotel,
        total_price=total_price
    )

if __name__ == '__main__':
    app.run(debug=True)