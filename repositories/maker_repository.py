from db.run_sql import run_sql

from models.maker import Maker

def save(maker):
    sql = "INSERT INTO makers (name, contact, tel, email, active) VALUES (%s, %s, %s, %s, %s ) RETURNING *"
    values = [maker.name, maker.contact, maker.tel, maker.email, maker.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    maker.id = id
    return maker

def select_all():
    makers = []

    sql = "SELECT * FROM makers"
    results = run_sql(sql)

    for result in results:
        maker = Maker(result['name'], result['contact'], result['tel'], result['email'], result['active'], result['id'] )
        makers.append(maker)
    return makers

def select(id):
    maker = None
    sql = "SELECT * FROM makers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        maker = Maker(result['name'], result['contact'], result['tel'], result['email'], result['active'], result['id'] )
    return maker

def update(maker):
    sql = "UPDATE makers SET (name, contact, tel, email, active) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [maker.name, maker.contact, maker.tel, maker.email, maker.active, maker.id]
    run_sql(sql, values)

# DELETE a maker
def delete(id):
    sql = "DELETE FROM makers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM makers"
    run_sql(sql)