import sqlite3

conn = sqlite3.connect('myquotes.db')
curr = conn.cursor()

# curr.execute("""create table quotes_db(
#              title text,
#              author text,
#              tag text)""")

# curr.execute("""insert into quotes_db values('python is awesome','buildwithpython','python')""")


conn.commit()
conn.close()