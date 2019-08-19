from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker

from database_setup import Employee

engine = create_engine('mysql://dotran:Leonardo112019!@localhost/company')
engine.connect()
DBSession = sessionmaker(bind=engine)
session = DBSession()


def create_employee(new_employee):
    session.add(new_employee)
    session.commit()


def get_employee_from_employee_id(employee_id):
    return session.query(Employee).filter_by(id=employee_id).one()


def edit_employee(employee):
    session.query(Employee).filter_by(id=employee.id).update({Employee.project_id: employee.project_id,
                                                              Employee.name: employee.name,
                                                              Employee.title: employee.title,
                                                              Employee.phone: employee.phone,
                                                              Employee.seat: employee.seat})
    session.commit()
    return employee


def get_all_employee_list():
    employee_list = session.query(Employee).all()
    employee_list_resp = []
    for employee in employee_list:
        employee_list_resp.append({'employee_id': employee.id, 'project_id': employee.project_id, 'name': employee.name,
                                   'title': employee.title, 'phone': employee.phone, 'seat': employee.seat})
    return employee_list_resp


def delete_employee_by_employee_id(employee_id):
    deleted_employee = session.query(Employee).filter_by(id=employee_id).one()
    session.delete(deleted_employee)
    session.commit()
