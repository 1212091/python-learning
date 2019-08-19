from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Project

engine = create_engine('mysql://dotran:Leonardo112019!@localhost/company')
engine.connect()
DBSession = sessionmaker(bind=engine)
session = DBSession()


def create_project(new_project):
    session.add(new_project)
    session.commit()


def get_project_from_project_id(project_id):
    return session.query(Project).filter_by(id=project_id).one()


def get_all_projects():
    return session.query(Project).all()


def delete_project_by_project_id(project_id):
    deleted_project = session.query(Project).filter_by(id=project_id).one()
    session.delete(deleted_project)
    session.commit()
