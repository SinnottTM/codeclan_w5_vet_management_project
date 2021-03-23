# kaiju controller, under construction

from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.kaiju import Kaiju
from models.vet import Vet
import repositories.kaiju_repository as kaiju_repository
import repositories.vet_repository as vet_repository

kaiju_blueprint = Blueprint("kaiju", __name__)

# SHOW Display all kaiju in DB. GET method as default
@kaiju_blueprint.route("/kaiju")
def kaiju_all():
    try:
        kaiju = kaiju_repository.select_all_kaiju()
        return render_template("kaiju/index.html", kaiju=kaiju)
    except (Exception) as error:
        print(error)
        return render_template('kaiju/error1.html')

# SHOW new vets. GET method
@kaiju_blueprint.route("/kaiju/new", methods=['GET'])
def new_kaiju_to_vet():
    try:
        kaiju = kaiju_repository.select_all_kaiju()
        vets = vet_repository.select_all_vets()
        return render_template("kaiju/new.html", all_kaiju = kaiju, all_vets = vets)
    except (Exception) as error:
        print(error)
        return render_template('kaiju/error2.html')

# CREATE new kaiju and save to DB. POST method
@kaiju_blueprint.route("/kaiju",  methods=['POST'])
def create_kaiju():
    try:
        name = request.form['name']
        dob = request.form['dob']
        kaiju_type = request.form['kaiju_type']
        treatment_notes = request.form['treatment_notes']
        vet = vet_repository.select_single_vet(request.form['vet_id'])
        kaiju = Kaiju(name, dob, kaiju_type, treatment_notes, vet)
        kaiju_repository.save_kaiju(kaiju)
        return redirect('/kaiju')
    except (Exception) as error:
          print(error)
          return render_template('kaiju/error2.html')

# SHOW kaiju by their <id> number. GET method
@kaiju_blueprint.route("/kaiju/<id>", methods=['GET'])
def show_kaiju(id):
    try:
          kaiju = kaiju_repository.select_single_kaiju(id)
          return render_template('kaiju/show.html', kaiju=kaiju)
    except (Exception) as error:
          print(error)
          return render_template('kaiju/error1.html')
# Look into  ('kaiju/error.html', error=error.context)

# EDIT kaiju via their id. GET method 
@kaiju_blueprint.route("/kaiju/<id>/edit", methods=['GET'])
def edit_kaiju(id):
    try:
        kaiju = kaiju_repository.select_single_kaiju(id)
        vets = vet_repository.select_all_vets()
        return render_template('kaiju/edit.html', kaiju = kaiju, all_vets = vets)
    except (Exception) as error:
          print(error)
          return render_template('kaiju/error2.html')

# UPDATE kaiju via their id. POST method
@kaiju_blueprint.route("/kaiju/<id>", methods=['POST'])
def update_kaiju(id):
    try:
        name = request.form['name']
        dob = request.form['dob']
        kaiju_type = request.form['kaiju_type']
        treatment_notes = request.form['treatment_notes']
        vet = vet_repository.select_single_vet(request.form['vet_id'])
        kaiju = Kaiju(name, dob, kaiju_type, treatment_notes, vet)
        kaiju_repository.update_kaiju(kaiju)
        return redirect('/kaiju')
    except (Exception) as error:
        print(error)
        return render_template('kaiju/error1.html')

# DELETE kaiju by id
@kaiju_blueprint.route("/kaiju/<id>/delete", methods=['POST'])
def delete_kaiju(id):
    try:
        kaiju_repository.delete_single_kaiju(id)
        return redirect('/kaiju')
    except (Exception) as error:
        print(error)
        return render_template('kaiju/error2.html')

# DELETE all kaiju
@kaiju_blueprint.route("/kaiju/delete", methods=['POST'])
def delete_all_kaiju():
    try:
        kaiju_repository.delete_all_kaiju()
        return redirect('/kaiju')
    except (Exception) as error:
        print(error)
        return render_template('kaiju/error1.html')

@kaiju_blueprint.route("/kaiju/facts")
def kaiju_facts():
    return render_template('kaiju/facts.html')

@kaiju_blueprint.route("/kaiju/error1")
def error_1_kaiju():
        return render_template('kaiju/error1.html')

@kaiju_blueprint.route("/kaiju/error2")
def error_2_kaiju():
    return render_template('kaiju/error2.html')
