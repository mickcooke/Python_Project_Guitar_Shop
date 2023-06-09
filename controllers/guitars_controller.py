from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.guitar import Guitar
from models.maker import Maker
import repositories.guitar_repository as guitar_repository
import repositories.maker_repository as maker_repository

guitars_blueprint = Blueprint("guitars", __name__)

@guitars_blueprint.route("/guitars")
def guitars():
    guitars = guitar_repository.select_all()
    return render_template("guitars/index.html", all_guitars = guitars)