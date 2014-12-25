from bottle import route, run, HTTPError, put, template
from sql import Person, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///person.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@route('/person/<name>')
def show(name):
    result = session.query(Person).filter_by(name=name).first()
    if result:
        return {'id': result.id, 'name': result.name}
    else:
        return HTTPError(404, "Name not found!")

@put('/person/<name>')
def new(name):
    new_person = Person(name=name)
    session.add(new_person)
    session.commit()
    return {'id': new_person.id, 'name': new_person.name}

@route('/persons')
def list():
    result = session.query(Person).all()
    return template("list", result=result)


if __name__ == "__main__":
    run(host='localhost', port=8080)