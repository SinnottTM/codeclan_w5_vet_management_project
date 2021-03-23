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
    kaiju = kaiju_repository.select_all()
    return render_template("kaiju/index.html", kaiju=kaiju)

# SHOW new vets. GET method (possably belongs in other controller?)
@kaiju_blueprint.route("/kaiju/new", methods=['GET'])
def new_kaiju_to_vet():
    vets = vet_repository.select_all()
    return render_template("kaiju/new.html", all_vets = vets)

# CREATE new kaiju and save to DB. POST method
@kaiju_blueprint.route("/kaiju",  methods=['POST'])
def create_kaiju():
    name = request.form['name']
    dob = request.form['dob']
    kaiju_type = request.form['kaiju_type']
    treatment_notes = request.form['treatment_notes']
    vet = vet_repository.select(request.form['vet_id'])
    kaiju = Kaiju(name, dob, kaiju_type, treatment_notes, vet)
    kaiju_repository.save(kaiju)
    return redirect('/kaiju')

# SHOW kaiju by their <id> number. GET method
@kaiju_blueprint.route("/kaiju/<id>", methods=['GET'])
def show_kaiju(id):
    kaiju = kaiju_repository.select(id)
    return render_template('kaiju/show.html', kaiju = kaiju)

# EDIT kaiju via their id. GET method 
@kaiju_blueprint.route("/kaiju/<id>/edit", methods=['GET'])
def edit_kaiju(id):
    kaiju = kaiju_repository.select(id)
    vets = vet_repository.select_all()
    return render_template('kaiju/edit.html', kaiju = kaiju, all_vets = vets)

# UPDATE kaiju via their id. POST method
@kaiju_blueprint.route("/kaiju/<id>", methods=['POST'])
def update_kaiju(id):
    name = request.form['name']
    dob = request.form['dob']
    kaiju_type = request.form['kaiju_type']
    treatment_notes = request.form['treatment_notes']
    vet = vet_repository.select(request.form['vet_id'])
    kaiju = Kaiju(name, dob, kaiju_type, treatment_notes, vet)
    kaiju_repository.update(kaiju)
    return redirect('/kaiju')

# DELETE kaiju by id
@kaiju_blueprint.route("/kaiju/<id>/delete", methods=['POST'])
def delete_kaiju(id):
    kaiju_repository.delete(id)
    return redirect('/kaiju')
