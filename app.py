from flask import Flask, redirect, render_template, request, url_for, jsonify
import forms

from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)

@app.get("/")
def index():
  return render_template("index.j2")

@app.post("/")
def index_post():
  create_form = forms.UserForm(request.form)
  if create_form.validate():
    alum = Alumnos(nombre=create_form.nombre.data, apellidos=create_form.apellidos.data, email=create_form.email.data)
    db.session.add(alum)
    db.session.commit()
  return render_template("index.j2", create_form=create_form)

if __name__ == '__main__':
  csrf.init_app(app)
  db.init_app(app)
  with app.app_context():
    db.create_all()
  app.run(debug=True)