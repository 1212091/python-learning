from flask import Blueprint, request, jsonify, make_response

from database_setup import Employee
from main.repository import employee_repository

mod_employee = Blueprint('employee', __name__, url_prefix='/employee')


@mod_employee.route("/", methods=["PUT"])
def create_employee():
    employee = Employee(project_id=request.get_json().get('project_id'),
                        name=request.get_json().get('name'),
                        title=request.get_json().get('title'),
                        phone=request.get_json().get('phone'),
                        seat=request.get_json().get('seat'))
    employee_repository.create_employee(employee)
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


@mod_employee.route("/<int:employee_id>", methods=["GET"])
def get_employee_by_employee_id(employee_id):
    selected_employee = employee_repository.get_employee_from_employee_id(employee_id)
    return make_response(
        jsonify({'employee_id': selected_employee.id, 'project_id': selected_employee.project_id,
                 'name': selected_employee.name, 'title': selected_employee.title,
                 'phone': selected_employee.phone, 'seat': selected_employee.seat}), 200)


@mod_employee.route("/", methods=["POST"])
def edit_employee():
    employee = Employee(id=request.get_json().get('id'),
                        project_id=request.get_json().get('project_id'),
                        name=request.get_json().get('name'),
                        title=request.get_json().get('title'),
                        phone=request.get_json().get('phone'),
                        seat=request.get_json().get('seat'))

    edited_employee = employee_repository.edit_employee(employee)
    return make_response(
        jsonify({'id': edited_employee.id, 'project_id': edited_employee.project_id,
                 'name': edited_employee.name, 'title': edited_employee.title,
                 'phone': edited_employee.phone, 'seat': edited_employee.seat}), 200)


@mod_employee.route("/", methods=["GET"])
def get_all_employee_list():
    employee_list_resp = employee_repository.get_all_employee_list()
    return make_response(jsonify(employee_list_resp), 200)


@mod_employee.route("/<int:employee_id>", methods=["DELETE"])
def delete_employee_by_employee_id(employee_id):
    employee_repository.delete_employee_by_employee_id(employee_id)
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp
