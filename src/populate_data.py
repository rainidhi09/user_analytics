import sqlite3

'''
create two table users and preferred_hobbies
users: user_id primary key
preferred_hobbies: user_id is foreign key
'''
class PopulateData:

    def __init__(self, con):
        con.row_factory = lambda cursor, row: row[0]
        self.con=con
        self.cur = self.con.cursor()

    def setup_db(self):
        self.cur.execute('drop table if exists users')
        self.cur.execute('drop table if exists preferred_hobbies')
        self.cur.execute('''CREATE TABLE users
                           (user_id INTEGER PRIMARY KEY, name text, joining_year INTEGER)''')
        self.cur.execute('''CREATE TABLE preferred_hobbies
                           (user_id INTEGER, hobbies_list text, FOREIGN KEY(user_id) REFERENCES users(user_id))''')
        self.con.commit()

    def populate_data(self):
        self.cur.execute("INSERT INTO users(user_id, name, joining_year) VALUES "
                    "(1, 'Hans',2018),(2, 'Klara',2019),(3, 'Sakura',2020)")

        self.cur.execute("INSERT INTO preferred_hobbies(user_id, hobbies_list) VALUES "
                    "(1,'knitting'),(1,'watching tellie'),(2,'sky diving'), (3,'watching tellie'),(3,'sky diving')")
        self.con.commit()

    def get_total_num_user(self):
        user_count = self.cur.execute('SELECT COUNT(1) as users_count from users WHERE joining_year = 2018').fetchone()
        print('****** total number of user for 2018={}'.format(user_count))

    def get_all_hobbies(self):
        hobby_list = self.cur.execute('SELECT DISTINCT(ph.hobbies_list) FROM preferred_hobbies as ph '
                                 'JOIN users as u on ph.user_id = u.user_id '
                                 'WHERE joining_year >= 2019').fetchall()
        print('****** All hobby list={}'.format(hobby_list))



if __name__ == "__main__":
    con = sqlite3.connect('users.db')
    try:
        obj = PopulateData(con)
        obj.setup_db()
        obj.populate_data()
        obj.get_total_num_user()
        obj.get_all_hobbies()
    except Exception as ex:
        print("Exception occurred while running queries", ex)
    finally:
        con.close()