import neomodel
from django.db import models
from neomodel import StructuredNode, StringProperty, UniqueIdProperty, \
    EmailProperty, BooleanProperty, Relationship, config, DateTimeProperty, One
from grest import models

neomodel.config.DATABASE_URL = "bolt://neo4j:meet2018@localhost:7687"

class Group(StructuredNode, models.Node):
    uid = UniqueIdProperty()
    name = StringProperty(required=True)

    members = Relationship('Person', 'IS_MEMBER')


class Person(StructuredNode, models.Node):
    # uid = UniqueIdProperty()
    email = EmailProperty(required=True, unique_index=True)
    name = StringProperty(required=True)
    lastname = StringProperty(required=True)
    is_active = BooleanProperty(default=0)
    password_hash = StringProperty(required=True)

    friends = Relationship('Person', 'IS_FRIEND')
    groups = Relationship('Group', 'IS_MEMBER')
    chat = Relationship('Chat', 'CHAT_MEMBER')

    event_joined = Relationship('Event', 'IS_JOINING')
    event_invited = Relationship('Event', 'IS_INVITED')
    event_declined = Relationship('Event', 'HAS_DECLINED')

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class Event(StructuredNode, models.Node):
    name = StringProperty(required=True)
    date = DateTimeProperty()
    description = StringProperty()
    location = StringProperty()

    joining = Relationship('Person', 'IS_JOINING')
    invited = Relationship('Person', 'IS_INVITED')
    declined = Relationship('Person', 'HAS_DECLINED')


class Chat(StructuredNode, models.Node):
    cid = UniqueIdProperty()
    name = StringProperty()

    messages = Relationship('Message', 'IN_CHAT')
    users = Relationship('Person', 'CHAT_MEMBER')


class Message(StructuredNode, models.Node):
    mid = UniqueIdProperty()
    message = StringProperty()
    timestamp = DateTimeProperty(default_now=True)

    chat = Relationship('Chat', 'IN_CHAT', cardinality=One)
    sender = Relationship('Person', 'SENDER', cardinality=One)
    unseen = Relationship('Person', 'READER')
