from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import psycopg2

app = Flask(__name__)

# Konfigurasi koneksi database PostgreSQL
conn = psycopg2.connect(
    dbname="feedbackdb",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    rating = request.form['rating']
    created_at = datetime.now()
    cur.execute("INSERT INTO feedback (rating) VALUES (%s)", (rating,))
    conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
