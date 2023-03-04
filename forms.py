from wtforms import Form, validators
from wtforms import StringField, EmailField

class UserForm(Form):
  id = StringField('id', validators=[validators.DataRequired()])
  nombre = StringField('nombre', validators=[validators.DataRequired()])
  apellidos = StringField('apellidos', validators=[validators.DataRequired()])
  email = EmailField('email', validators=[validators.DataRequired()])