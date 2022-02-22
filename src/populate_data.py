import sqlite3

'''
create two table users and preferred_hobbies
users: user_id primary key
preferred_hobbies: user_id is foreign key
'''

if __name__ == "__main__":
    con = sqlite3.connect('users.db')
    con.row_factory = lambda cursor, row: row[0]
    cur = con.cursor()
    cur.execute('drop table if exists users')
    cur.execute('drop table if exists preferred_hobbies')
    cur.execute('''CREATE TABLE users
                   (user_id INTEGER PRIMARY KEY, name text, joining_year INTEGER)''')
    cur.execute('''CREATE TABLE preferred_hobbies
                   (user_id INTEGER, hobbies_list text, FOREIGN KEY(user_id) REFERENCES users(user_id))''')
    cur.execute("INSERT INTO users(user_id, name, joining_year) VALUES "
                "(1, 'Hans',2018),(2, 'Klara',2019),(3, 'Sakura',2020)")

    cur.execute("INSERT INTO preferred_hobbies(user_id, hobbies_list) VALUES "
                "(1,'knitting'),(1,'watching tellie'),(2,'sky diving'), (3,'watching tellie'),(3,'sky diving')")

    con.commit()

    user_count = cur.execute('SELECT COUNT(1) as users_count from users WHERE joining_year = 2018').fetchall()
    print('****** total number of user for 2018=', user_count.pop())

    hobby_list = cur.execute('SELECT DISTINCT(ph.hobbies_list) FROM preferred_hobbies as ph '
                             'JOIN users as u on ph.user_id = u.user_id '
                             'WHERE joining_year >= 2019').fetchall()
    print('****** All hobby list=', hobby_list)

    con.close()
