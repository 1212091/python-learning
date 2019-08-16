from flask_inputs import Inputs
from wtforms.validators import InputRequired


class BusinessUnitInputs(Inputs):
    json = {
        'bu_name': [InputRequired()]
    }
