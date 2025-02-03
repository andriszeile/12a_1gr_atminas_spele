import sqlite3

# Izveido savienojumu ar datubāzi (ja faili nepastāv, tie tiks izveidoti)
conn = sqlite3.connect('dati.db')
c = conn.cursor()

# Izveido tabulu rezultātiem
c.execute('''
CREATE TABLE IF NOT EXISTS rezultati (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    klikski INTEGER NOT NULL,
    laiks INTEGER NOT NULL,
    datums TEXT NOT NULL
)
''')

# Piecu izdomātu ierakstu saraksts
ieraksti = [
    ("Anonīmais", 1000, 1000, "2020-01-01"),
    ("Anonīmais", 100, 100, "2020-01-01"),
    ("Anonīmais", 100, 100, "2020-01-01"),
    ("Anonīmais", 100, 100, "2020-01-01"),
    ("Anonīmais", 100, 100, "2020-01-01"),
    ("Anonīmais", 100, 100, "2020-01-01"),
    ("Anonīmais", 100, 100, "2020-01-01"),
    ("Anonīmais", 100, 100, "2020-01-01"),
    ("Anonīmais", 100, 100, "2020-01-01"),
    ("Anonīmais", 100, 100, "2020-01-01"),
]

# Pievieno ierakstus tabulā
c.executemany('''
INSERT INTO rezultati (vards, klikski, laiks, datums)
VALUES (?, ?, ?, ?)
''', ieraksti)

# Saglabā izmaiņas un aizver savienojumu
conn.commit()
conn.close()

print("Datubāze un ieraksti veiksmīgi izveidoti!")
