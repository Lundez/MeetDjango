from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        model = Person
        fields = ('email', 'name', 'lastname', 'password_hash')