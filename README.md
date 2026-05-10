# EasySQL

EasySQL is a simple MySQL utility library built with Python and PyMySQL.

It provides easy-to-use methods for:
- SELECT
- INSERT
- UPDATE
- DELETE

The goal of this library is to simplify MySQL database operations for beginners and small projects.

---

# Features

- Simple CRUD operations
- Parameterized queries
- Multiple WHERE conditions
- Dictionary-based results
- Lightweight and beginner friendly

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/easysql.git
cd easysql
```

## Install Package

```bash
pip install -e .
```

---

# Requirements

- Python 3.8+
- MySQL Server

---

# Dependencies

```bash
pip install pymysql cryptography
```

---

# Example Usage

```python
from easysql import EasySQL

db = EasySQL(
    host="localhost",
    user="root",
    password="1234",
    database="test"
)

print(db.is_connected())
```

---

# Select Example

```python
users = db.select(
    table="users",
    columns=["id", "name"],
    where_columns=["id"],
    where_values=[1]
)

print(users)
```

---

# Insert Example

```python
db.insert(
    table="users",
    columns=["name", "email"],
    data=["Atul", "atul@gmail.com"]
)
```

---

# Update Example

```python
db.update(
    table="users",
    set_columns=["name"],
    set_values=["New Name"],
    where_columns=["id"],
    where_values=[1]
)
```

---

# Delete Example

```python
db.delete(
    table="users",
    where_columns=["id"],
    where_values=[1]
)
```

---

# Project Structure

```text
easysql/
│
├── easysql/
│   ├── __init__.py
│   ├── database.py
│   ├── exceptions.py
│   └── validators.py
│
├── tests/
│   └── test_database.py
│
├── README.md
├── LICENSE
├── setup.py
├── pyproject.toml
└── requirements.txt
```

---

# Future Improvements

- ORDER BY support
- LIMIT support
- JOIN support
- Connection pooling
- Async support
- Query builder
- Logging system

---

# License

This project is licensed under the MIT License.