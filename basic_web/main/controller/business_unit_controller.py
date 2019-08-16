from flask import Blueprint, request, jsonify, make_response, abort
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from database_setup import Business_unit
from main.exception.business_rule_exception import RemoveViolateRuleError
from main.repository import business_unit_repository
from main.validator.business_unit_validator import BusinessUnitInputs

mod_business_unit = Blueprint('business_unit', __name__, url_prefix='/bu')
engine = create_engine('mysql://dotran:Leonardo112019!@localhost/company')
engine.connect()
DBSession = sessionmaker(bind=engine)
session = DBSession()


@mod_business_unit.route("/", methods=["POST"])
def create_bu():
    inputs = BusinessUnitInputs(request)
    if not inputs.validate():
        return jsonify(success=False, errors=inputs.errors)
    business_unit = Business_unit(bu_name=request.get_json().get('bu_name'),
                                  location=request.get_json().get('location'))
    business_unit_repository.create_bu(business_unit)
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


@mod_business_unit.route("/<int:business_unit_id>", methods=["GET"])
def get_bu_by_bu_id(business_unit_id):
    selected_bu = business_unit_repository.get_bu_by_bu_id(business_unit_id)
    return make_response(
        jsonify({'id': selected_bu.id, 'name': selected_bu.bu_name, 'description': selected_bu.location}), 200)


@mod_business_unit.route("/", methods=["GET"])
def get_all_bu_list():
    bus_response = business_unit_repository.get_all_bu_list()
    return make_response(jsonify(bus_response), 200)


@mod_business_unit.route("/<int:bu_id>", methods=["DELETE"])
def delete_bu_by_bu_id(bu_id):
    business_unit_repository.delete_bu_by_bu_id(bu_id)
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


@mod_business_unit.errorhandler(RemoveViolateRuleError)
def internal_error(error):
    return make_response(jsonify(success=True, message="This business unit has project in it"), 500)


@mod_business_unit.errorhandler(NoResultFound)
def internal_error(error):
    return make_response(jsonify(success=True, message="This business unit is not existed"), 500)
