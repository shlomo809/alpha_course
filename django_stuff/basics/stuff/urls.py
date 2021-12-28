from django.urls import path

from . import views

urlpatterns = [
    path('getRandomNumber/', views.getRandomNumber),
    path('getServerTime/', views.getServerTime),
    path('addPerson/', views.addPerson),
    path('getAllPeople/', views.getAllPeople),
    path('removePerson/<int:user_id>/', views.removePerson),
    path('updatePerson/', views.updatePerson),
]