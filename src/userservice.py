from flask import Response
import json
import sqlite3

'''
Starting service 
localhost:8080/users : return all users list
localhost:8080/preferred-hobbies : return all hobbies list in desc order based on number of users
'''


def configure_routes(app):
    @app.route('/users')
    def get_all_users():
        with sqlite3.connect("users.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            cur = con.cursor()
            list_of_users = cur.execute('SELECT name from users').fetchall()
            con.commit()
            return Response(json.dumps(list_of_users), mimetype='application/json')

    @app.route('/preferred-hobbies')
    def get_preferred_hobbies():
        with sqlite3.connect("users.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            cur = con.cursor()
            list_of_hobbies = cur.execute('SELECT hobbies_list,count(1) FROM preferred_hobbies '
                                          'GROUP BY hobbies_list ORDER BY 2 desc').fetchall()
            con.commit()
            return Response(json.dumps(list_of_hobbies), mimetype='application/json')
