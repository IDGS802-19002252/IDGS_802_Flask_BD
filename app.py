from flask import Flask, redirect, render_template, request, url_for, jsonify
import forms

from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)

@app.route("/", methods=["GET", "POST"])
def index():
  create_form = forms.UserForm(request.form)
  if request.method == "POST":
    alum = Alumnos(nombre=create_form.nombre.data, apellidos=create_form.apellidos.data, email=create_form.email.data)
    db.session.add(alum)
    db.session.commit()
  return render_template("index.j2", form=create_form)
  # return render_template("index.j2")

@app.route('/modificar', methods=["GET", "POST"])
def modificar():
  create_form = forms.UserForm(request.form)
  if request.method == "GET":
    id=request.args.get("id")
    alum1 = db.session.query(Alumnos).filter_by(id = id).first()
    create_form.id.data = request.args.get("id")
    create_form.nombre.data = alum1.nombre
    create_form.apellidos.data = alum1.apellidos
    create_form.email.data = alum1.email
  if request.method == "POST":
    id=create_form.id.data
    alum=db.session.query(Alumnos).filter_by(id=id).first()
    print(create_form.data)
    alum.nombre=create_form.nombre.data
    alum.apellidos=create_form.apellidos.data
    alum.email=create_form.email.data
    db.session.add(alum)
    db.session.commit()
    return redirect(url_for("ABCompleto"))
  return render_template("modificar.j2", form=create_form)

@app.route('/ABCompleto', methods=["GET", "POST"])
def ABCompleto():
  form = forms.UserForm(request.form);
  alumnos = db.session.query(Alumnos).all()
  return render_template("ABCompleto.j2", form = form, alumnos = alumnos)

# @app.post("/")
# def index_post():
#   create_form = forms.UserForm(request.form)
#   if create_form.validate():
#     alum = Alumnos(nombre=create_form.nombre.data, apellidos=create_form.apellidos.data, email=create_form.email.data)
#     db.session.add(alum)
#     db.session.commit()
#   return render_template("index.j2", form=create_form)

if __name__ == '__main__':
  csrf.init_app(app)
  db.init_app(app)
  with app.app_context():
    db.create_all()
  app.run(debug=True)