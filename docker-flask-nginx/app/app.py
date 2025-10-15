import os
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "demo")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "example")

def get_conn():
    return psycopg2.connect(
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD
    )

@app.get("/healthz")
def health():
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
        return "ok", 200
    except Exception as e:
        return f"db_error: {e}", 500

@app.get("/")
def home():
    return "hello from flask via nginx (with Postgres)!", 200

@app.get("/users")
def list_users():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, created_at FROM users ORDER BY id DESC")
            rows = cur.fetchall()
    data = [{"id": r[0], "name": r[1], "created_at": r[2].isoformat()} for r in rows]
    return jsonify(data), 200

@app.post("/users")
def create_user():
    payload = request.get_json(silent=True) or {}
    name = payload.get("name")
    if not name:
        return {"error": "name is required"}, 400
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users(name) VALUES(%s) RETURNING id", (name,))
            new_id = cur.fetchone()[0]
        conn.commit()
    return {"id": new_id, "name": name}, 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

