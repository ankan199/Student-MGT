from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = []
next_id = 1  # simple unique ID counter

@app.route('/', methods=["GET", "POST"])
def home():
    global next_id
    if request.method == "POST":
        student_name = request.form.get("student_name")
        student_class = request.form.get("student_class")
        student_dob = request.form.get("student_dob")
        student_city = request.form.get("student_city")
        student_state = request.form.get("student_state")
        student_stream = request.form.get("student_stream")
        student_subjects = request.form.get("student_subjects")
        student_admno = request.form.get("student_admno")
        student_doadm = request.form.get("student_doadm")

        form_data = {
            "id": next_id,
            "student_name": student_name,
            "student_class": student_class,
            "student_dob": student_dob,
            "student_city": student_city,
            "student_state": student_state,
            "student_stream": student_stream,
            "student_subjects": student_subjects,
            "student_admno": student_admno,
            "student_doadm": student_doadm
        }

        students.append(form_data)
        next_id += 1

    return render_template('todlis.html', form_data=students)

@app.route('/edit/<int:student_id>', methods=["GET", "POST"])
def edit(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        return "Student not found", 404

    if request.method == "POST":
        # Update student data
        student["student_name"] = request.form.get("student_name")
        student["student_class"] = request.form.get("student_class")
        student["student_dob"] = request.form.get("student_dob")
        student["student_city"] = request.form.get("student_city")
        student["student_state"] = request.form.get("student_state")
        student["student_stream"] = request.form.get("student_stream")
        student["student_subjects"] = request.form.get("student_subjects")
        student["student_admno"] = request.form.get("student_admno")
        student["student_doadm"] = request.form.get("student_doadm")

        return redirect(url_for('home'))

    return render_template('edit_student.html', student=student)

if __name__ == '__main__':
    app.run(debug=True, port=4000)
