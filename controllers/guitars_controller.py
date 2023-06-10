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

@guitars_blueprint.route("/makers")
def makers():
    makers = maker_repository.select_all()
    return render_template("makers/index.html", all_makers = makers)

@guitars_blueprint.route("/guitars/edit/<id>", methods=['GET'])
def edit_guitar(id):
    guitar = guitar_repository.select(id)
    makers = maker_repository.select_all()
    return render_template("guitars/edit.html", guitar = guitar, all_makers = makers)