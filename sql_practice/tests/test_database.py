import sqlite3
import pytest
from pathlib import Path

@pytest.fixture
def db_connection():
    connect = sqlite3.connect(Path(__file__).resolve().parent.parent/"database"/"qa_practice.db")
    cur = connect.cursor()
    yield cur
    connect.close()

@pytest.mark.parametrize(
    ("order_id", "expected_status"),
    (
        (101, "completed"),
        (102, "completed"),
        (103, "completed"),
        (104, "pending"),
        (105, "cancelled")
    )
)
def test_order_status(db_connection, order_id, expected_status):
    db_connection.execute("SELECT status FROM orders WHERE order_id = ?",(order_id,))
    data = db_connection.fetchone()
    assert data == (expected_status,) , f"{data} failed"


@pytest.mark.parametrize(
    ("user_id", "expected_count"),
    (
        (1, 2),
        (2, 1),
        (3, 1),
        (4, 0),
        (5, 0),
        (6, 1),
    )
)
def test_user_order_count(db_connection, user_id, expected_count):
    db_connection.execute(f"SELECT COUNT(orders.user_id) FROM users LEFT JOIN orders on users.id = orders.user_id WHERE users.id = ? GROUP BY users.name",(user_id,))
    data = db_connection.fetchone()
    assert data == (expected_count,)

def test_valid_foreign_key():
    connect = sqlite3.connect(Path(__file__).resolve().parent.parent/"database"/"qa_practice.db")
    cur = connect.cursor()

    cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute("PRAGMA foreign_keys;")
    data = cur.fetchone()
    assert data == (1,), f"Failed to find foreign key {data}"

    payload = (101, 1, 20.00, "completed")
    cur.execute("INSERT INTO orders_fk_demo(order_id, user_id, amount, status) VALUES(?,?,?,?)", payload)
    cur.execute("SELECT * FROM orders_fk_demo")
    data = cur.fetchone()
    assert data == (101, 1, 20, 'completed'), f"Invalid Foreign Key payload = {payload} data = {data}"

    cur.execute("ROLLBACK")
    cur.execute("SELECT * FROM orders_fk_demo")
    data = cur.fetchone()
    assert data is None, f"{data} is not empty"

    cur.close()
    connect.close()

def test_invalid_foreign_key():
    connect = sqlite3.connect(Path(__file__).resolve().parent.parent / "database" / "qa_practice.db")
    cur = connect.cursor()

    cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute("PRAGMA foreign_keys;")
    data = cur.fetchone()
    assert data == (1,), "Failed to find foreign key"

    payload2 = (102, 999, 99.00, "pending")
    with pytest.raises(sqlite3.IntegrityError) as exc_info:
        cur.execute("INSERT INTO orders_fk_demo(order_id, user_id, amount, status) VALUES(?,?,?,?)", payload2)

    assert "FOREIGN KEY constraint failed" in str(exc_info.value)

    cur.close()
    connect.close()