from connection import get_connection

def insert_music(title,genre,year,artist_name,number_of_albums):
    connection =  get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO music(title,genre,year,artist_name,number_of_albums) VALUES (%s,%s,%s,%s,%s)"
    values = (title,genre,year,artist_name,number_of_albums)
    cursor.execute(sql,values)
    connection.commit()
    print("H mousiki prostithike")
    cursor.close()
    connection.close()

insert_music("End of the line","metal",2007,"Metallica",3)
insert_music("Come and get it","rock",1998,"Year of the ship",7)
 import tkinter as tk
from tkinter import messagebox
from connection import get_connection


def insert_music(title, genre, year, artist_name,number_of_albums):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO music(title,genre,year,artist_name,number_of_albums) VALUES (%s,%s,%s,%s,%s)"
        values = (title,genre,year,artist_name,number_of_albums)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Exception as e:
        print("Σφάλμα:", e)
        return False

def submit_music():
    title = entry_title.get()
    genre = entry_genre.get()
    year = entry_year.get()
    artist_name = entry_artist_name.get()
    number_of_albums = entry_umber_of_albums.get()

    if not (title and artist_name and year and genre):
        messagebox.showwarning("Σφάλμα", "Συμπλήρωσε όλα τα πεδία!")
        return

    try:
        year = int(year)
    except ValueError:
        messagebox.showerror("Σφάλμα", "Το έτος πρέπει να είναι αριθμός!")
        return

    if insert_music(title, genre, year, artist_name,number_of_albums):
        messagebox.showinfo("Επιτυχία", "Το βιβλίο προστέθηκε επιτυχώς!")
        entry_title.delete(0, tk.END)
        entry_artist_name.delete(0, tk.END)
        entry_year.delete(0, tk.END)
        entry_genre.delete(0, tk.END)
        entry_number_of_albums.delete(0, tk.END)
    else:
        messagebox.showerror("Αποτυχία", "Αποτυχία εισαγωγής Μουσικής.")

# Δημιουργία παραθύρου
window = tk.Tk()
window.title("Εισαγωγή Μουσικης")
window.geometry("400x300")

# Ετικέτες και πεδία
tk.Label(window, text="Τίτλος:").pack(pady=5)
entry_title = tk.Entry(window, width=40)
entry_title.pack()

tk.Label(window, text="Καλλιτεχνης:").pack(pady=5)
entry_artist_name = tk.Entry(window, width=40)
entry_artist_name.pack()

tk.Label(window, text="Έτος Έκδοσης:").pack(pady=5)
entry_year = tk.Entry(window, width=40)
entry_year.pack()

tk.Label(window, text="Είδος:").pack(pady=5)
entry_genre = tk.Entry(window, width=40)
entry_genre.pack()

# Κουμπί καταχώρησης
submit_button = tk.Button(window, text="Καταχώρηση Μουσικής", command=submit_music)
submit_button.pack(pady=20)

# Εκκίνηση εφαρμογής
window.mainloop()

