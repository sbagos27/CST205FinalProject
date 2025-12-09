"""
Senen Bagos, 
This will be our minimal outline to start off 
this code provides michael jackson songs in an extremely simple html

Connor Overbo,
Update default route and added second route.  
Create form for user input and store the values.
Call APIs to generate the image and affirmation for the 2nd web site route.

Steps to run
In terminal, CD to the Flask project folder that these files/subfolders are saved in.  
Then run the home.py file from VS Code.  
Open browser to 127.0.0.1:5000 to get to the app.

"""


from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
from API2 import get_cat_image, get_affirmation

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)

class User(FlaskForm):
    first_name = StringField(
        'First Name', 
        validators=[DataRequired()]
    )
    day_of_week = StringField(
        'Day of the Week',
        validators=[DataRequired()]
    )

data = {"fn": None, "day": None}

def store_data(first_name, day_of_week):
    data["fn"] = first_name
    data["day"] = day_of_week

@app.route('/', methods=('GET', 'POST'))
def main():
    form = User()
    if form.validate_on_submit():
        store_data(form.first_name.data, form.day_of_week.data)
        return redirect('/index')
    return render_template('main.html', form=form)

@app.route('/index')
def index():
    if data["fn"] is None or data["day"] is None:
        return redirect('/')
    get_cat_image()
    affirmation = get_affirmation()
    return render_template('index.html', fn=data["fn"], day=data["day"], affirmation=affirmation)

if __name__ == '__main__':
    app.run(debug=True)