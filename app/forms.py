from flask_wtf import Form
from wtforms import StringField, BooleanField,  TextAreaField, SelectMultipleField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from .models import Todo

class TodoForm(Form):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
