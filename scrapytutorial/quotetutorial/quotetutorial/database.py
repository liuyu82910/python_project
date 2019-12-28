import sqlite3

conn = sqlite3.connect('myquotes.db')
cur= conn.cursor()

cur.execute("""create table quote_table(
               title text,
               author text,
               tag text
               )""")
cur.execute("""insert into quote_table values (
'Where is your dream?','J K Lowing', 'warm, bitter'
) """)
conn.commit()
conn.close()


