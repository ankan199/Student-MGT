from flask import Flask,render_template,request
# Flask constructor
app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def home():
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
        form_data={"student_name":student_name,
                            "student_class":student_class,"student_dob":student_dob,"student_city":student_city,"student_state":student_state,"student_stream":student_stream,"student_subjects":student_subjects,"student_admno":student_admno,
                              "student_doadm":student_doadm}
        print(form_data)
        return render_template('todlis.html',data=form_data)

    return render_template('todlis.html')
    
                   
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True,port=4000)
