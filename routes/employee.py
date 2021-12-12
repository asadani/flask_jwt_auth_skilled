from flask import Blueprint, make_response, jsonify

from auth import required_auth

employee_blueprint = Blueprint('report_blueprint', __name__)


@employee_blueprint.route('/employee')
def portal():
    res = {"message": "Welcome to employee portal"}
    return make_response(jsonify(res), 200)


@employee_blueprint.route('/employee/info')
@required_auth(["admin", "viewer"])
def info():
    res = {"message": "You can view employee info"}
    return make_response(jsonify(res), 200)


@employee_blueprint.route('/employee/salary')
@required_auth(["admin"])
def salary():
    res = {"message": "You can view employee salary"}
    return make_response(jsonify(res), 200)
