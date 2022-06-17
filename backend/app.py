import db
import psycopg
from func_Days_less10 import func_Days_less10
from func_for_days_more_than_10 import func_for_days_more_than_10
from models import cursor
from flask import Flask, render_template, request, redirect, url_for

db.create_database_and_table()
func_Days_less10()
func_for_days_more_than_10()


conn = psycopg.connect(
"""
    host=rc1a-7uwsuhdx1lg2ilre.mdb.yandexcloud.net
    port=6432
    dbname=postgresql
    user=postgresql
    password=<password>
    target_session_attrs=read-write
    sslmode=verify-full
""")


conn.autocommit = True

app = Flask (__name__)

@app.route("/",  methods=['POST', 'GET'])
def spisok():
  get_data_from_db = "SELECT DISTINCT data from currencies ORDER by data;";
  cursor.execute(get_data_from_db)
  data=cursor.fetchall()
  return render_template('spisok.html', data=data)




@app.route("/currencies", methods=['POST', 'GET'])
def page():
  chosen_data = request.form.get('data')
  get_data_from_db = f"select * from currencies  where data = '{chosen_data}' order by name;";
  cursor.execute(get_data_from_db)
  my_table=cursor.fetchall()
  return render_template('main.html', my_table=my_table, chosen_data=chosen_data)

@app.route('/update', methods=['POST'])
def update():
  models.create_database_and_table()
  func_Days_less10()
  func_for_days_more_than_10()
  return redirect(url_for('spisok'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)








