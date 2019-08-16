from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from database_setup import Project, Business_unit
from main.exception.business_rule_exception import RemoveViolateRuleError

engine = create_engine('mysql://dotran:Leonardo112019!@localhost/company')
engine.connect()
DBSession = sessionmaker(bind=engine)
session = DBSession()


def delete_bu_by_bu_id(bu_id):
    deleted_business_unit = session.query(Business_unit).filter_by(id=bu_id).one()
    try:
        session.query(Project).filter_by(business_unit_id=bu_id).one()
        raise RemoveViolateRuleError("Business unit has project in it")
    except NoResultFound:
        session.delete(deleted_business_unit)
        session.commit()


def get_all_bu_list():
    bus = session.query(Business_unit).all()
    bus_response = []
    for bu in bus:
        bus_response.append({'id': bu.id, 'bu_name': bu.bu_name, 'location': bu.location})
    return bus_response


def create_bu(business_unit):
    session.add(business_unit)
    session.commit()


def get_bu_by_bu_id(business_unit_id):
    selected_bu = session.query(Business_unit).filter_by(id=business_unit_id).one()
    return selected_bu
