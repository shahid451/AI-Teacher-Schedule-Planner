from flask import Flask, render_template, request, redirect, url_for
from database import create_tables, get_connection
from timetable_generator import generate_timetable
from pdf_generator import create_pdf


app = Flask(__name__)


# =====================================================
# DASHBOARD
# =====================================================

@app.route("/")
def home():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM teachers")
    total_teachers = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM subjects")
    total_subjects = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM rooms")
    total_rooms = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM classes")
    total_classes = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        total_teachers=total_teachers,
        total_subjects=total_subjects,
        total_rooms=total_rooms,
        total_classes=total_classes
    )


# =====================================================
# TEACHERS MODULE
# =====================================================

@app.route("/teachers", methods=["GET", "POST"])
def teachers():

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":

        name = request.form["name"]
        subject = request.form["subject"]

        cursor.execute(
            """
            INSERT INTO teachers (name, subject)
            VALUES (?, ?)
            """,
            (name, subject)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("teachers"))

    cursor.execute("SELECT * FROM teachers")
    teacher_list = cursor.fetchall()

    conn.close()

    return render_template(
        "teachers.html",
        teachers=teacher_list
    )


@app.route("/edit_teacher/<int:id>", methods=["GET", "POST"])
def edit_teacher(id):

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":

        name = request.form["name"]
        subject = request.form["subject"]

        cursor.execute(
            """
            UPDATE teachers
            SET name = ?, subject = ?
            WHERE id = ?
            """,
            (name, subject, id)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("teachers"))

    cursor.execute(
        "SELECT * FROM teachers WHERE id = ?",
        (id,)
    )

    teacher = cursor.fetchone()

    conn.close()

    return render_template(
        "edit_teacher.html",
        teacher=teacher
    )


@app.route("/delete_teacher/<int:id>")
def delete_teacher(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM teachers WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("teachers"))


# =====================================================
# SUBJECTS MODULE
# =====================================================

@app.route("/subjects", methods=["GET", "POST"])
def subjects():

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":

        name = request.form["name"]
        code = request.form["code"]

        cursor.execute(
            """
            INSERT INTO subjects (name, code)
            VALUES (?, ?)
            """,
            (name, code)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("subjects"))

    cursor.execute("SELECT * FROM subjects")
    subject_list = cursor.fetchall()

    conn.close()

    return render_template(
        "subjects.html",
        subjects=subject_list
    )


@app.route("/edit_subject/<int:id>", methods=["GET", "POST"])
def edit_subject(id):

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":

        name = request.form["name"]
        code = request.form["code"]

        cursor.execute(
            """
            UPDATE subjects
            SET name = ?, code = ?
            WHERE id = ?
            """,
            (name, code, id)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("subjects"))

    cursor.execute(
        "SELECT * FROM subjects WHERE id = ?",
        (id,)
    )

    subject = cursor.fetchone()

    conn.close()

    return render_template(
        "edit_subject.html",
        subject=subject
    )


@app.route("/delete_subject/<int:id>")
def delete_subject(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM subjects WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("subjects"))


# =====================================================
# ROOMS MODULE
# =====================================================

@app.route("/rooms", methods=["GET", "POST"])
def rooms():

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":

        room_number = request.form["room_number"]
        capacity = request.form["capacity"]

        cursor.execute(
            """
            INSERT INTO rooms (room_number, capacity)
            VALUES (?, ?)
            """,
            (room_number, capacity)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("rooms"))

    cursor.execute("SELECT * FROM rooms")
    room_list = cursor.fetchall()

    conn.close()

    return render_template(
        "rooms.html",
        rooms=room_list
    )


@app.route("/edit_room/<int:id>", methods=["GET", "POST"])
def edit_room(id):

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":

        room_number = request.form["room_number"]
        capacity = request.form["capacity"]

        cursor.execute(
            """
            UPDATE rooms
            SET room_number = ?, capacity = ?
            WHERE id = ?
            """,
            (room_number, capacity, id)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("rooms"))

    cursor.execute(
        "SELECT * FROM rooms WHERE id = ?",
        (id,)
    )

    room = cursor.fetchone()

    conn.close()

    return render_template(
        "edit_room.html",
        room=room
    )


@app.route("/delete_room/<int:id>")
def delete_room(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM rooms WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("rooms"))


# =====================================================
# CLASSES MODULE
# =====================================================

@app.route("/classes", methods=["GET", "POST"])
def classes():

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":

        class_name = request.form["class_name"]
        semester = request.form["semester"]
        students = request.form["students"]

        cursor.execute(
            """
            INSERT INTO classes (class_name, semester, students)
            VALUES (?, ?, ?)
            """,
            (class_name, semester, students)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("classes"))

    cursor.execute("SELECT * FROM classes")
    class_list = cursor.fetchall()

    conn.close()

    return render_template(
        "classes.html",
        classes=class_list
    )


@app.route("/edit_class/<int:id>", methods=["GET", "POST"])
def edit_class(id):

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":

        class_name = request.form["class_name"]
        semester = request.form["semester"]
        students = request.form["students"]

        cursor.execute(
            """
            UPDATE classes
            SET class_name = ?,
                semester = ?,
                students = ?
            WHERE id = ?
            """,
            (class_name, semester, students, id)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("classes"))

    cursor.execute(
        "SELECT * FROM classes WHERE id = ?",
        (id,)
    )

    class_data = cursor.fetchone()

    conn.close()

    return render_template(
        "edit_class.html",
        class_data=class_data
    )


@app.route("/delete_class/<int:id>")
def delete_class(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM classes WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("classes"))


# =====================================================
# TIMETABLE GENERATOR
# =====================================================

@app.route("/timetable")
def timetable():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM teachers")
    teachers_data = cursor.fetchall()

    cursor.execute("SELECT * FROM subjects")
    subjects_data = cursor.fetchall()

    cursor.execute("SELECT * FROM rooms")
    rooms_data = cursor.fetchall()

    cursor.execute("SELECT * FROM classes")
    classes_data = cursor.fetchall()

    conn.close()

    generated_timetable = generate_timetable(
        teachers_data,
        subjects_data,
        rooms_data,
        classes_data
    )

    return render_template(
        "timetable.html",
        timetable=generated_timetable
    )


# =====================================================
# PDF EXPORT
# =====================================================

@app.route("/export_pdf")
def export_pdf():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM teachers")
    teachers_data = cursor.fetchall()

    cursor.execute("SELECT * FROM subjects")
    subjects_data = cursor.fetchall()

    cursor.execute("SELECT * FROM rooms")
    rooms_data = cursor.fetchall()

    cursor.execute("SELECT * FROM classes")
    classes_data = cursor.fetchall()

    conn.close()

    generated_timetable = generate_timetable(
        teachers_data,
        subjects_data,
        rooms_data,
        classes_data
    )

    create_pdf(
        generated_timetable,
        "Timetable.pdf"
    )

    return "PDF Generated Successfully!"


# =====================================================
# MAIN APPLICATION
# =====================================================

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)