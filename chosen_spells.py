import sqlite3

# Connect to the database
conn = sqlite3.connect('stored_spells.db')
cursor = conn.cursor()

# Create a table to store the key-value pairs
cursor.execute('''
    CREATE TABLE IF NOT EXISTS chosen_spells (
        spell TEXT PRIMARY KEY,
        episode TEXT
    )
''')

# Function to insert a key-value pair into the database
def insert_key_value(spell, episode):
    cursor.execute('INSERT INTO chosen_spells VALUES (?, ?)', (spell, episode))
    conn.commit()
    #print("Spell-Description inserted successfully.")
    

# Function to retrieve the value for a given key
def get_value(spell):
    cursor.execute('SELECT episode FROM stored_spells WHERE spell = ?', (spell,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None
    
def get_random_key_value():
    cursor.execute('SELECT spell, episode FROM chosen_spells ORDER BY RANDOM() LIMIT 1')
    result = cursor.fetchone()
    if result:
        return result
    else:
        return None
def remove_spell_from_database(spell):
    # Remove the chosen spell from the stored spells database
    cursor.execute("DELETE FROM chosen_spells WHERE spell = ?", (spell,))
    conn.commit()
    print("Spell removed from the database.")

# Insert key-value pairs into the database
#insert_key_value('name', 'John')
#insert_key_value('age', '25')
#insert_key_value('city', 'New York')


# Retrieve values using keys
#print(get_value('name'))  # Output: John
#print(get_value('age'))   # Output: 25
#print(get_value('city'))  # Output: New York

# Close the database connection
def close_connection():
    conn.close()