from django.shortcuts import render
from django.http import HttpResponse

from meetPage.models import Person

def index(request):
    #Person(name="Hampus", email="hampus.londogard@gmail.com", lastname="Londogard", password_hash="hej").save()
    #for person in Person.nodes.all():
    #    person.delete()
    return HttpResponse("Hello, world. You're at the polls index. :" + str(Person.nodes.all()[0]))