import sqlite3

# Connect to the database
conn = sqlite3.connect('episodes.db')
cursor = conn.cursor()

# Create a table to store the key-value pairs
cursor.execute('''
    CREATE TABLE IF NOT EXISTS episodes (
        episode_index TEXT PRIMARY KEY,
        current_episode TEXT
    )
''')

# Function to insert a key-value pair into the database
def insert_key_value(index, episode):
    cursor.execute('INSERT INTO episodes VALUES (?, ?)', (index, episode))
    conn.commit()
    #print("Spell-Description inserted successfully.")
    

# Function to retrieve the value for a given key
def get_value():
    cursor.execute('SELECT current_episode FROM episodes WHERE episode_index = ?', ("0"))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None
    
def remove_episode_from_database(episode):
    # Remove the chosen spell from the stored spells database
    cursor.execute("DELETE FROM episodes WHERE index = ?", (episode,))
    conn.commit()
    print("Episode removed from the database.")

def update_value(new_value):
    cursor.execute("UPDATE episodes SET current_episode = ? WHERE episode_index = 0",(new_value,))
    conn.commit()


# Insert key-value pairs into the database
#try:
#    insert_key_value('name')
#except Exception as e:
#    #print(e)
#    pass
#insert_key_value('age', '25')
try:
    insert_key_value(0, 0)
except:
    print("Database Table Already Created")



# Retrieve values using keys
#print(get_value('name'))  # Output: John
#print(get_value('age'))   # Output: 25
#print(get_value('city'))  # Output: New York

# Close the database connection
def close_connection():
    conn.close()