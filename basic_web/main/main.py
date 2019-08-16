from flask import Flask
from controller.project_controller import mod_project
from controller.business_unit_controller import mod_business_unit

app = Flask(__name__)

app.register_blueprint(mod_project)
app.register_blueprint(mod_business_unit)

if __name__ == "__main__":
    app.run(debug=True)
