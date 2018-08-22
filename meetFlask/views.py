from grest import GRest

from .models import Person


class PersonsView(GRest):
    __model__ = {"primary": Person}
    __selection_field__ = {"primary": "uid"}