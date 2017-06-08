import os
from datetime import datetime
from flask import Flask, render_template, redirect, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, login_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField
from wtforms.validators import DataRequired


# Enable CSRF Protection
csrf = CSRFProtect()

# Instantiating the application
app = Flask(__name__)
csrf.init_app(app)

# Configuring the Flask application
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////car_wash.db"
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
WTF_CSRF_SECRET_KEY = app.config['SECRET_KEY']

# Instantiating the SQLAlchemy object with the application and its configuration
db = SQLAlchemy(app)

# Instantiating the LoginManager class for Flask_Login
login_manager = LoginManager()
login_manager.init_app(app)


# Create classes for database
class CarWashService(db.Model):
    __tablename__ = "carwash"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    price_for_car = db.Column(db.Float)
    price_for_truck = db.Column(db.Float)

    def __repr__(self):
        return "Car Wash Price: {car}\nTruck Wash Price: {truck}\n".format(
            car=self.price_for_car,
            truck=self.price_for_truck
        )


class Customer(db.Model):
    __tablename__ = "customer"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    email_address = db.Column(db.String(40), nullable=False)
    vehicle_type = db.Column(db.String(40), nullable=False)
    license_plate = db.Column(db.String(40), nullable=False)
    total_paid = db.Column(db.Float, default=0.0, nullable=False)
    total_owed = db.Column(db.Float, default=0.0, nullable=False)
    times_visited = db.Column(db.Integer, default=0, nullable=False)

    def __repr__(self):
        return "ID: {id}\nName: {first} {last}\nVehicle: {car}\nVisits: {num}\nOwes: {owe}\nRevenue: {total}".format(
            id=self.id,
            first=self.first_name,
            last=self.last_name,
            car=self.vehicle_type,
            num=self.times_visited,
            owe=self.total_owed,
            total=self.total_paid
        )


# Inheriting the UserMixin for Flask_Login to work properly
# See docs for details
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    email_address = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean)


# Create a form for login
class LoginForm(FlaskForm):
    email_address = StringField('email_address', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])


# Instantiating the Admin class to use Flask_Admin
admin = Admin(app, name='car_wash_app', template_mode="bootstrap3")
# Admin views go here
admin.add_view(ModelView(CarWashService, db.session))
admin.add_view(ModelView(Customer, db.session))
admin.add_view(ModelView(User, db.session))


# Creating routes with Flask
@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(User)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


# Running the application
if __name__ == '__main__':
    app.run(debug=True)
