import sqlite3


# =====================================================
# DATABASE CONNECTION
# =====================================================

def get_connection():

    conn = sqlite3.connect("planner.db")

    # This allows accessing data like:
    # teacher["name"]
    conn.row_factory = sqlite3.Row

    return conn


# =====================================================
# CREATE ALL TABLES
# =====================================================

def create_tables():

    conn = get_connection()
    cursor = conn.cursor()


    # ===============================
    # TEACHERS TABLE
    # ===============================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            subject TEXT NOT NULL
        )
    """)


    # ===============================
    # SUBJECTS TABLE
    # ===============================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subjects (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            code TEXT NOT NULL
        )
    """)


    # ===============================
    # ROOMS TABLE
    # ===============================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            room_number TEXT NOT NULL,

            capacity INTEGER NOT NULL
        )
    """)


    # ===============================
    # CLASSES TABLE
    # ===============================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS classes (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            class_name TEXT NOT NULL,

            semester TEXT NOT NULL,

            students INTEGER NOT NULL
        )
    """)


    # Save changes
    conn.commit()

    # Close database
    conn.close()