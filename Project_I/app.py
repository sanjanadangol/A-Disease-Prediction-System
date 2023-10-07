from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from form import RegistrationForm, LoginForm
import csv
from pred_func import predict_disease

app = Flask(__name__)
app.config['SECRET_KEY'] = '8627eb6c716fd6abae9baf4082928629'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/diseasepredictor'
# mysql = SQLAlchemy(app)
# mysql.init_app(app)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'flask'


# with app.app_context():
#     mysql.create_all()


# class user_details(mysql.Model):
#     id = mysql.Column(mysql.Integer, primary_key=True)
#     username = mysql.Column(mysql.String(50), nullable=False)
#     email = mysql.Column(mysql.String(50), unique=True)
#     password = mysql.Column(mysql.String(32), nullable=False)

def read_csv(filename):
    symptoms = []
    with open(filename,'r') as f:
        symptoms_dict = csv.reader(f)
        for columns in symptoms_dict:
            symptoms.append(columns[1].capitalize())
    return symptoms

# model = pickle.load(open('models/my_final_model.pkl','rb'))


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if request.method == 'POST':
#         print('hello')
#         if form.validate_on_submit():
#             flash(f"Account created successfully for {form.username.data}!!!",'success')
#         # name = form.username.data
#         # email = form.email.data
#         # password = form.password.data
#         # cpassword = form.confirm.data
#         # return redirect(url_for('index'))
#         else:
#             return render_template('register.html', form=form)
#     else:
#         print('Hello')
#         return render_template('register.html', form=form)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if request.method=='POST':
#         if form.validate_on_submit():
#             if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
#                 flash(f"Logged In success","success")
#             return redirect('prediction_page')
#         # name = form.username.data
#         # email = form.email.data
#         # password = form.password.data
#         # cpassword = form.confirm.data
#         else:
#             flash(f"Logged In unsuccess","danger")
#         return redirect('login')
#     elif request.method=='GET':
#         return render_template('login.html',form=form)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/help')
def help():
    return render_template('help.html')

# @app.route('/predict',methods=['GET','POST'])
# def predict():
#     flash(f"inside predict()")
#     # symptoms = read_csv('tsymptoms.csv')
#     if request.method == 'POST':
#         # input_symptoms = request.form.getlist("cbox")
#         # prediction = predict_disease(input_symptoms)
#         return render_template('error.html',title='Symptoms')
#     else:
#         return render_template('error.html',title='Symptoms')

@app.route('/prediction_page',methods=['POST','GET'])
def prediction_page():
    
    symptoms = read_csv('tsymptoms.csv')
    
    if request.method == 'POST':
        input_symptoms = request.form.getlist("cbox")
        if len(input_symptoms)<5:
            flash(f"Please select atleast 5 symptoms",'danger')
            return redirect('prediction_page')
        else:
            prediction = predict_disease(input_symptoms)
            return render_template('disease.html',symptoms=input_symptoms,prediction=prediction)
    else:
        return render_template('prediction_page.html',title='Symptoms',symptoms=symptoms)


if __name__ == '__main__':
    app.run(debug=True)
