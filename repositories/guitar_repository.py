from db.run_sql import run_sql

from models.guitar import Guitar
from models.maker import Maker
import repositories.maker_repository as maker_repository

def save(guitar):
    sql = "INSERT INTO guitars (name, description, stock, min_stock, buy_price, sell_price, maker_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [guitar.name, guitar.description, guitar.stock, guitar.min_stock, guitar.buy_price, guitar.sell_price, guitar.maker.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    guitar.id = id
    return guitar

def select_all():
    guitars = []

    sql = "SELECT * FROM guitars"
    results = run_sql(sql)

    for result in results:
        maker = maker_repository.select(result['maker_id'])
        guitar = Guitar(result['name'], result['description'], result['stock'], result['min_stock'], result['buy_price'], result['sell_price'], maker, result['id'] )
        guitars.append(guitar)
    return guitars

def delete_all():
    sql = "DELETE FROM guitars"
    run_sql(sql)

def select(id):
    guitar = None
    sql = "SELECT * FROM guitars WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        maker = maker_repository.select(result['maker_id'])
        guitar = Guitar(result['name'], result['description'], result['stock'], result['min_stock'], result['buy_price'], result['sell_price'], maker, result['id'] )
    return guitar



    