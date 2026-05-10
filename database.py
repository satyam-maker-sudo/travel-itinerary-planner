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

# INDIAN TOURIST PLACES

places_data = [

    # GOA

    ('Goa', 'Baga Beach'),
    ('Goa', 'Calangute Beach'),
    ('Goa', 'Fort Aguada'),
    ('Goa', 'Anjuna Beach'),
    ('Goa', 'Dudhsagar Falls'),

    # MUMBAI

    ('Mumbai', 'Gateway of India'),
    ('Mumbai', 'Marine Drive'),
    ('Mumbai', 'Juhu Beach'),
    ('Mumbai', 'Bandra Bandstand'),
    ('Mumbai', 'Elephanta Caves'),

    # PUNE

    ('Pune', 'Shaniwar Wada'),
    ('Pune', 'Sinhagad Fort'),
    ('Pune', 'Aga Khan Palace'),
    ('Pune', 'Khadakwasla Dam'),

    # JAIPUR

    ('Jaipur', 'Hawa Mahal'),
    ('Jaipur', 'Amber Fort'),
    ('Jaipur', 'City Palace'),
    ('Jaipur', 'Jal Mahal'),

    # DELHI

    ('Delhi', 'India Gate'),
    ('Delhi', 'Red Fort'),
    ('Delhi', 'Qutub Minar'),
    ('Delhi', 'Lotus Temple'),

    # MANALI

    ('Manali', 'Solang Valley'),
    ('Manali', 'Rohtang Pass'),
    ('Manali', 'Hadimba Temple'),
    ('Manali', 'Mall Road')

]

# HOTELS WITH BUDGET CATEGORY

hotel_data = [

    # GOA

    ('Goa', 'Sea View Resort', 'Low', 1500),
    ('Goa', 'Goa Paradise Inn', 'Medium', 3000),
    ('Goa', 'Grand Hyatt Goa', 'High', 7000),

    # MUMBAI

    ('Mumbai', 'Hotel City Palace', 'Low', 2000),
    ('Mumbai', 'The Orchid Hotel', 'Medium', 4500),
    ('Mumbai', 'Taj Mahal Palace', 'High', 9000),

    # PUNE

    ('Pune', 'Royal Stay Inn', 'Low', 1200),
    ('Pune', 'Hotel Sapphire', 'Medium', 2800),
    ('Pune', 'JW Marriott Pune', 'High', 6500),

    # JAIPUR

    ('Jaipur', 'Pink City Hotel', 'Low', 1800),
    ('Jaipur', 'Royal Heritage', 'Medium', 3500),
    ('Jaipur', 'Rambagh Palace', 'High', 8500),

    # DELHI

    ('Delhi', 'Capital Residency', 'Low', 1700),
    ('Delhi', 'The Park Hotel', 'Medium', 4000),
    ('Delhi', 'The Leela Palace', 'High', 9500),

    # MANALI

    ('Manali', 'Hill View Cottage', 'Low', 1400),
    ('Manali', 'Snow Peak Resort', 'Medium', 3200),
    ('Manali', 'The Himalayan Resort', 'High', 7500)

]

# INSERT PLACE DATA

cursor.executemany('''
INSERT INTO places (city, place_name)
VALUES (?, ?)
''', places_data)

# INSERT HOTEL DATA

cursor.executemany('''
INSERT INTO hotels (city, hotel_name, budget_type, price_per_person)
VALUES (?, ?, ?, ?)
''', hotel_data)

conn.commit()

print("Indian Travel Database Created Successfully")

conn.close()