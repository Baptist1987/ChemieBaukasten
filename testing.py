import sqlite3

# Verbindung zur Datenbank herstellen (wenn die Datenbank nicht vorhanden ist, wird sie erstellt)
conn = sqlite3.connect('example.db')

# Cursor-Objekt erstellen, um Datenbankabfragen auszuführen
cursor = conn.cursor()

# Tabelle erstellen
cursor.execute('''Insert Into datKunden (name, land) Values ('A', 'B');''')

conn.commit()
ausgabe = cursor.fetchall()
print(ausgabe)
# Datenbankverbindung schließen
conn.close()


