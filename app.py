from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



app = Flask(__name__) 

app.config['SECRET_KEY'] = 'key'

class InfoForm(FlaskForm):
    name_first = StringField('First Name: ', validators=[DataRequired()])
    name_last = StringField('Last Name: ', validators=[DataRequired()] )
    submit = SubmitField('Submit')


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    form = InfoForm()

    if form.validate_on_submit():
        session['name_first'] = form.name_first.data
        session['name_last'] = form.name_last.data
        
        return redirect(url_for('index'))
    

    return render_template('apply.html', form=form)
    

if __name__ == '__main__':
    app.run()