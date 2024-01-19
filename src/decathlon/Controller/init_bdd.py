import os
import sqlite3

from src.decathlon.Model.health import HealthData
from src.decathlon.connexion import get_connection
import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    mail TEXT,
                    password TEXT,
                    birth_date DATETIME)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS unites (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    abbreviation TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS health_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_user INTEGER,
                    date DATETIME,
                    nombre_pas INTEGER,
                    duree_sommeil INTEGER,
                    u_duree_sommeil INTEGER,
                    frequence_cardiaque INTEGER,
                    u_frequence_cardiaque INTEGER,
                    poids INTEGER,
                    u_poids INTEGER,
                    taille REAL,
                    u_taille INTEGER)''')

conn.commit()

