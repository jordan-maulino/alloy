from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, EmailField,
                    TelField, SelectField, DateField, IntegerField)
from wtforms.validators import DataRequired, Email, Length, Optional 

class InfoForm(FlaskForm):
    name_first = StringField('First Name: ', validators=[DataRequired()])
    name_last = StringField('Last Name: ', validators=[DataRequired()])
    birth_date = DateField("Date of Birth: ", format='%Y-%m-%d', validators=[DataRequired()])
    document_ssn = TelField("SSN: ", validators=[DataRequired(), Length(9)])
    email_address = EmailField("Email: ", validators=[DataRequired()])
    phone_number = TelField('Phone Number: ', validators=[Optional(), Length(11)])
    address_line_1 = StringField("Street Address: ", validators=[DataRequired()])
    address_line_2 = StringField("Street Address line 2 (optional): ", validators=[Optional()])
    address_city = StringField("City: ", validators=[DataRequired()])
    address_state = StringField("State: ", validators=[DataRequired(), Length(2)])
    address_postal_code = TelField("ZIP Code: ", validators=[DataRequired(), Length(5)])
    address_country_code = SelectField('Country: ', choices=["US", "US"], validators=[DataRequired()])







    submit = SubmitField('Submit')