from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "db"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "rootpassword"),
            database=os.getenv("DB_NAME", "myappdb")
        )
        cursor = conn.cursor()
        cursor.execute("SELECT message FROM greetings LIMIT 1;")
        result = cursor.fetchone()
        conn.close()
        return f"Hello from Flask! DB says: {result[0]}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)



