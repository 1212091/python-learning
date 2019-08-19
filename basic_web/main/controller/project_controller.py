from flask import request, jsonify, make_response, Blueprint

from database_setup import Project
from main.repository import project_repository

mod_project = Blueprint('project', __name__, url_prefix='/project')


@mod_project.route("/", methods=["POST"])
def create_project():
    new_project = Project(name=request.get_json().get('name'), description=request.get_json().get('description'),
                          business_unit_id=request.get_json().get('business_unit_id'))
    project_repository.create_project(new_project)
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


@mod_project.route("/<int:project_id>", methods=["GET"])
def get_project_from_project_id(project_id):
    project = project_repository.get_project_from_project_id(project_id)
    return make_response(jsonify({'id': project.id, 'name': project.name, 'description': project.description}), 200)


@mod_project.route("/", methods=["GET"])
def get_all_projects():
    projects = project_repository.get_all_projects()
    projects_response = []
    for project in projects:
        projects_response.append({'id': project.id, 'name': project.name, 'description': project.description})
    return make_response(jsonify(projects_response), 200)


@mod_project.route("/<int:project_id>", methods=["DELETE"])
def delete_project_by_project_id(project_id):
    project_repository.delete_project_by_project_id(project_id)
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp
