from flask import Flask
from controller.project_controller import mod_project
from controller.business_unit_controller import mod_business_unit
from controller.employee_controller import mod_employee

app = Flask(__name__)

app.register_blueprint(mod_project)
app.register_blueprint(mod_business_unit)
app.register_blueprint(mod_employee)

if __name__ == "__main__":
    app.run(debug=True)
