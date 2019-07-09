import sqlite3

con = sqlite3.connect('./manga.db')
cur = con.cursor()

sql = "select * from manga_info"
cur.execute(sql)

for row in cur:
    print(row[0], row[1], row[2], row[3], row[4])

con.close()
