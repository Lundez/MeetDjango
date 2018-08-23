from grest import GRest

from .models import Person, Group, Event, Chat, Message


class PersonsView(GRest):
    __model__ = {"primary": Person}
    __selection_field__ = {"primary": "email"}


class GroupsView(GRest):
    __model__ = {"primary": Group}
    __selection_field__ = {"primary": "uid"}


class EventsView(GRest):
    __model__ = {"primary": Event}
    __selection_field__ = {"primary": "eid"}


class ChatsView(GRest):
    __model__ = {"primary": Chat}
    __selection_field__ = {"primary": "cid"}


class MessagesView(GRest):
    __model__ = {"primary": Message}
    __selection_field__ = {"primary": "mid"}