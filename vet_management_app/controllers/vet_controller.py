from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.kaiju import Kaiju
from models.vet import Vet
import repositories.kaiju_repository as kaiju_repository
import repositories.vet_repository as vet_repository

vet_blueprint = Blueprint("vets", __name__)

# SHOW Display all vet in DB. GET method as default
@vet_blueprint.route("/vets")
def vet_all():
    vet = vet_repository.select_all_vets()
    return render_template("vets/index.html", vet=vet)

# SHOW new vets. GET method (possably belongs in other controller?)
@vet_blueprint.route("/vets/new", methods=['GET'])
def new_kaiju_to_vet():
    vets = vet_repository.select_all_vets()
    return render_template("vets/new.html", all_vets=vets)

# CREATE new vet and save to DB. POST method
@vet_blueprint.route("/vets",  methods=['POST'])
def create_vet():
    name = request.form['name']
    kaiju = request.form['kaiju']
    vet = Vet(name, kaiju)
    vet_repository.save_vet(vet)
    return redirect('/vets')

# SHOW vet by their <id> number. GET method
@vet_blueprint.route("/vets/<id>", methods=['GET'])
def show_vet(id):
    try:
        vet = vet_repository.select_single_kaiju(id)
        return render_template('vets/show.html', vet=vet)
    except (Exception) as error:
        print(error)
        return render_template('vets/error.html')
# Look into  ('vet/error.html', error=error.context)

# EDIT vet via their id. GET method
@vet_blueprint.route("/vets/<id>/edit", methods=['GET'])
def edit_vet(id):
    vet = vet_repository.select_single_vet(id)
    # vets = vet_repository.select_all_vets()
    return render_template('vets/edit.html', vet=vet)

# UPDATE vet via their id. POST method
@vet_blueprint.route("/vets/<id>", methods=['POST'])
def update_kaiju(id):
    name = request.form['name']
    kaiju = request.form['kaiju']
    vet = Vet(name, kaiju)
    vet_repository.update_vet(vet)
    return redirect('/vets')

# DELETE vet by id
@vet_blueprint.route("/vets/<id>/delete", methods=['POST'])
def delete_vet(id):
    vet_repository.delete_single_vet(id)
    return redirect('/vets')

# # DELETE all vet
# @vet_blueprint.route("/vets/delete", methods=['POST'])
# def delete_all_vet():
#     vet_repository.delete_all_vet()
#     return redirect('/vets')
