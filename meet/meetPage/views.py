from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .models import Person
from .serializers import PersonSerializer


class CreateView(generics.ListCreateAPIView):
    queryset = Person.nodes.all()
    serializer_class = PersonSerializer
    lookup_field = 'email'

    def get_object(self):
        return Person.nodes.get(email=self.kwargs[self.lookup_field])

    def perform_create(self, serializer):
        serializer.save()


def index(request):
    #Person(name="Hampus", email="hampus.londogard@gmail.com", lastname="Londogard", password_hash="hej").save()
    #for person in Person.nodes.all():
    #    person.delete()
    return HttpResponse("Hello, world. You're at the polls index. :" + str(Person.nodes.all()))