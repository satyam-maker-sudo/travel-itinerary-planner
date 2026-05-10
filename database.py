import sqlite3

conn = sqlite3.connect('travel.db')

cursor = conn.cursor()

# USERS TABLE

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
''')

# PLACES TABLE

cursor.execute('''
CREATE TABLE IF NOT EXISTS places (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    place_name TEXT
)
''')

# HOTELS TABLE

cursor.execute('''
CREATE TABLE IF NOT EXISTS hotels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    hotel_name TEXT,
    budget_type TEXT,
    price_per_person INTEGER
)
''')

# FOOD TABLE

cursor.execute('''
CREATE TABLE IF NOT EXISTS food_places (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    restaurant TEXT
)
''')

# ACTIVITIES TABLE

cursor.execute('''
CREATE TABLE IF NOT EXISTS activities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    activity TEXT
)
''')

# DELETE OLD DATA

cursor.execute("DELETE FROM places")
cursor.execute("DELETE FROM hotels")
cursor.execute("DELETE FROM food_places")
cursor.execute("DELETE FROM activities")

# =========================
# GOA
# =========================

goa_places = [

    ('Goa', 'Baga Beach'),
    ('Goa', 'Calangute Beach'),
    ('Goa', 'Fort Aguada'),
    ('Goa', 'Anjuna Beach'),
    ('Goa', 'Dudhsagar Falls'),
    ('Goa', 'Candolim Beach')

]

goa_hotels = [

    ('Goa', 'Goa Paradise Resort', 'Low', 1800),
    ('Goa', 'Sea View Resort', 'Medium', 3500),
    ('Goa', 'Grand Hyatt Goa', 'High', 8000)

]

goa_food = [

    ('Goa', 'Thalassa'),
    ('Goa', 'Cafe Chocolatti'),
    ('Goa', 'Ritz Classic')

]

goa_activities = [

    ('Goa', 'Water Sports'),
    ('Goa', 'Beach Party'),
    ('Goa', 'Nightlife')

]

# =========================
# MUMBAI
# =========================

mumbai_places = [

    ('Mumbai', 'Gateway of India'),
    ('Mumbai', 'Marine Drive'),
    ('Mumbai', 'Juhu Beach'),
    ('Mumbai', 'Elephanta Caves'),
    ('Mumbai', 'Bandra Worli Sea Link'),
    ('Mumbai', 'Colaba Causeway')

]

mumbai_hotels = [

    ('Mumbai', 'Hotel City Palace', 'Low', 2200),
    ('Mumbai', 'The Orchid Hotel', 'Medium', 4500),
    ('Mumbai', 'Taj Palace Mumbai', 'High', 9000)

]

mumbai_food = [

    ('Mumbai', 'Leopold Cafe'),
    ('Mumbai', 'Bademiya'),
    ('Mumbai', 'Cafe Mondegar')

]

mumbai_activities = [

    ('Mumbai', 'Marine Drive Walk'),
    ('Mumbai', 'Shopping'),
    ('Mumbai', 'Street Food Tour')

]

# =========================
# JAIPUR
# =========================

jaipur_places = [

    ('Jaipur', 'Hawa Mahal'),
    ('Jaipur', 'Amber Fort'),
    ('Jaipur', 'City Palace'),
    ('Jaipur', 'Jal Mahal'),
    ('Jaipur', 'Nahargarh Fort'),
    ('Jaipur', 'Birla Mandir')

]

jaipur_hotels = [

    ('Jaipur', 'Pink City Hotel', 'Low', 2000),
    ('Jaipur', 'Royal Heritage Stay', 'Medium', 4000),
    ('Jaipur', 'Rambagh Palace', 'High', 10000)

]

jaipur_food = [

    ('Jaipur', 'Chokhi Dhani'),
    ('Jaipur', 'Laxmi Mishthan Bhandar'),
    ('Jaipur', 'Tapri Central')

]

jaipur_activities = [

    ('Jaipur', 'Camel Ride'),
    ('Jaipur', 'Fort Visit'),
    ('Jaipur', 'Cultural Dance Show')

]

# =========================
# MANALI
# =========================

manali_places = [

    ('Manali', 'Solang Valley'),
    ('Manali', 'Rohtang Pass'),
    ('Manali', 'Hadimba Temple'),
    ('Manali', 'Mall Road'),
    ('Manali', 'Jogini Waterfalls'),
    ('Manali', 'Old Manali')

]

manali_hotels = [

    ('Manali', 'Snow Peak Resort', 'Low', 1800),
    ('Manali', 'Mountain View Resort', 'Medium', 3800),
    ('Manali', 'The Himalayan', 'High', 8500)

]

manali_food = [

    ('Manali', 'Johnson Cafe'),
    ('Manali', 'Cafe 1947'),
    ('Manali', 'Drifters Cafe')

]

manali_activities = [

    ('Manali', 'Snow Adventure'),
    ('Manali', 'River Rafting'),
    ('Manali', 'Paragliding')

]

# INSERT ALL DATA

cursor.executemany('''
INSERT INTO places(city, place_name)
VALUES (?, ?)
''', goa_places + mumbai_places + jaipur_places + manali_places)

cursor.executemany('''
INSERT INTO hotels(city, hotel_name, budget_type, price_per_person)
VALUES (?, ?, ?, ?)
''', goa_hotels + mumbai_hotels + jaipur_hotels + manali_hotels)

cursor.executemany('''
INSERT INTO food_places(city, restaurant)
VALUES (?, ?)
''', goa_food + mumbai_food + jaipur_food + manali_food)

cursor.executemany('''
INSERT INTO activities(city, activity)
VALUES (?, ?)
''', goa_activities + mumbai_activities + jaipur_activities + manali_activities)

conn.commit()

print("Robust Indian Travel Database Created Successfully")

conn.close()