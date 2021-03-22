# kaiju controller, TBC

from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.kaiju import Kaiju
import repositories.kaiju_repository as kaiju_repository

kaiju_blueprint = Blueprint("kaiju", __name__)

@kaiju_blueprint.route("/kaiju")
def kaiju():
    kaiju = kaiju_repository.select_all()
    return render_template("kaiju/index.html", kaiju=kaiju)
