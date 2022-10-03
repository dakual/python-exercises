import sqlite3

# Connecting database
conn = sqlite3.connect("test.db")
crsr = conn.cursor()

# Single result
crsr.execute("SELECT sqlite_version();")
data = crsr.fetchone()
print("Database version :",data)

# Creating database
crsr.execute("""CREATE TABLE IF NOT EXISTS employe (
            id INTEGER PRIMARY KEY,
            firstname VARCHAR(20),
            lastname VARCHAR(30),
            gender CHAR(1),
            createdat DATE);
            """)

# Inserting data
try:
  crsr.execute("""INSERT INTO employe VALUES (1, "Ali","Veli", "M", "1999-04-07");""")
  crsr.execute("""INSERT INTO employe VALUES (2, "Mustafa", "Yılmaz","M", "1980-05-11");""")
  crsr.execute("""INSERT INTO employe VALUES (4, "Ayşe", "Demir","F", "1987-11-20");""")
  crsr.execute("""INSERT INTO employe VALUES (5, "Ebru", "Kaya","F", "1992-01-13");""")
  crsr.execute("""INSERT INTO employe VALUES (6, "İbrahim", "Şahin","M", "1996-04-22");""")

  conn.commit()
except Exception as e:
  conn.rollback()

sql = "INSERT INTO employe (firstname, lastname, gender, createdat) VALUES (?, ?, ?, ?)"
val = [("Aaaa", "Bbbb", "M", "1996-04-22"),
       ("Cccc", "Dddd", "M", "1996-04-22"),
       ("Eeee", "Ffff", "F", "1996-04-22"),
       ("Gggg", "Hhhh", "F", "1996-04-22"),
       ("Kkkk", "Llll", "F", "1996-04-22")]
crsr.executemany(sql, val)



# Updating
sql = "UPDATE employe SET firstname = 'İbrahim Kara' WHERE id = %d;" % (6)
try:
  crsr.execute(sql)
  conn.commit()
except:
  conn.rollback()

# Deleting
crsr.execute("""DELETE FROM employe WHERE firstname="Ali";""")

# Fetching Data
crsr.execute("""SELECT * FROM employe""")
results = crsr.fetchall()
for i in results:
  print(i)


# Commit your changes in the database
conn.commit()


# Close connection
crsr.close()
conn.close()

