from django.db import models
from neomodel import StructuredNode, StringProperty, UniqueIdProperty, \
    EmailProperty, BooleanProperty, Relationship, config

config.DATABASE_URL = 'bolt://neo4j:meet2018@localhost:7687'

class Group(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(required=True)

    members = Relationship('Person', 'IS_MEMBER')


class Person(StructuredNode):
    # uid = UniqueIdProperty()
    email = EmailProperty(required=True, unique_index=True)
    name = StringProperty(required=True)
    lastname = StringProperty(required=True,)
    is_active = BooleanProperty(default=0)
    password_hash = StringProperty(required=True,)

    friends = Relationship('Person', 'IS_FRIEND')
    groups = Relationship('Group', 'IS_MEMBER')
