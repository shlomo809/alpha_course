from django.shortcuts import render
from django.http import HttpResponse
import random
from datetime import datetime
import io
import json
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import People


def getRandomNumber(request):
    random_number = random.randrange(0, 2)
    return HttpResponse(random_number)


def getServerTime(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return HttpResponse(current_time)


@csrf_exempt
def addPerson(request):
    stream = io.BytesIO(request.body)
    data = JSONParser().parse(stream)

    try:
        (People.objects.get(pk=data['personal_id']))
        return HttpResponse("user already exists")
    except:
        new_person = People(name=data['name'], personal_id=data['personal_id'], birth_date=data['birth_date'])
        new_person.save()
        return HttpResponse(new_person)


@csrf_exempt
def getAllPeople(request):
    q = list(People.objects.all().values())
    return HttpResponse(q)



@csrf_exempt
def removePerson(request,user_id):
    try:
        (People.objects.get(pk=user_id))
        People.objects.get(pk=user_id).delete()
        return HttpResponse("user deleted")
    except:
      
        return HttpResponse("this user is not exists")

@csrf_exempt
def updatePerson(request):
    stream = io.BytesIO(request.body)
    data = JSONParser().parse(stream)
    print(People.objects.get(pk=data['personal_id']))
    try:
        (People.objects.get(pk=data['personal_id']))
        update_person = People(name=data['name'], personal_id=data['personal_id'], birth_date=data['birth_date'])
        update_person.save()
        
        p=People.objects.get(pk=data['personal_id'])
        
        
        return HttpResponse(p)
    except Exception as e:
        print (e)
        return HttpResponse("this user is not exists")
        