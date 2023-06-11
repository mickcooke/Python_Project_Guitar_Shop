from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.guitar import Guitar
from models.maker import Maker
import repositories.guitar_repository as guitar_repository
import repositories.maker_repository as maker_repository

guitars_blueprint = Blueprint("guitars", __name__)

# SHOW ALL GUITARS
@guitars_blueprint.route("/guitars")
def guitars():
    guitars = guitar_repository.select_all()
    return render_template("guitars/index.html", all_guitars = guitars)

# SHOW ALL MAKERS
@guitars_blueprint.route("/makers")
def makers():
    makers = maker_repository.select_all()
    return render_template("makers/index.html", all_makers = makers)

# EDIT A GUITAR 
@guitars_blueprint.route("/guitars/edit/<id>", methods=['GET'])
def edit_guitar(id):
    guitar = guitar_repository.select(id)
    makers = maker_repository.select_all()
    return render_template("guitars/edit.html", guitar = guitar, all_makers = makers)

# EDIT A MAKER 
@guitars_blueprint.route("/makers/edit/<id>", methods=['GET'])
def edit_maker(id):
    maker = maker_repository.select(id)
    return render_template("makers/edit.html", maker = maker)

# UPDATE A GUITAR
@guitars_blueprint.route("/guitars/update/<id>", methods=['POST'])
def update_guitar(id):
    name = request.form['name']
    description = request.form['description']
    stock = request.form['stock']
    min_stock = request.form['min_stock']
    buy_price = request.form['buy_price']
    sell_price = request.form['sell_price']
    maker_id = request.form['maker_id']

    maker = maker_repository.select(maker_id)
    guitar = Guitar(name, description, stock, min_stock, buy_price, sell_price, maker, id)

    guitar_repository.update(guitar)
    return redirect('/guitars')

# UPDATE A MAKER
@guitars_blueprint.route("/makers/update/<id>", methods=['POST'])
def update_maker(id):
    name = request.form['name']
    contact = request.form['contact']
    tel = request.form['tel']
    email = request.form['email']


    maker = Maker(name, contact, tel, email, id)

    maker_repository.update(maker)
    return redirect('/makers')


# DELETE guitar by id
@guitars_blueprint.route("/guitars/delete/<id>", methods=['POST'])
def delete_guitar(id):
    guitar_repository.delete(id)
    return redirect('/guitars')

# DELETE Maker by id
@guitars_blueprint.route("/makers/delete/<id>", methods=['POST'])
def delete_maker(id):
    maker_repository.delete(id)
    return redirect('/makers')