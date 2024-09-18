from models import Dog


def create_table(base, engine):
    base.metadata.create_all(engine)


def save(session, dog):
    session.add(dog)
    session.commit()


def get_all(session):
    dogs = session.query(Dog).all()
    return dogs


def find_by_name(session, name):
    name = session.query(Dog).filter(Dog.name == name).first()
    return name


def find_by_id(session, id):
    id = session.query(Dog).filter(Dog.id == id).first()
    return id


def find_by_name_and_breed(session, name, breed):
    name_breed = (
        session.query(Dog).filter((Dog.name == name), (Dog.breed == breed)).first()
    )
    return name_breed


def update_breed(session, dog, breed):
    breed_update = session.query(Dog).filter(Dog.id == dog.id).first()

    if breed_update:
        breed_update.breed = breed
        session.commit()
    else:
        raise ValueError("No dog found with that id")
