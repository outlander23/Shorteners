from django.urls import path
from .views import *
urlpatterns = [
    path("", index, name="name"), 
    path('create/', create, name="create"),
    path('<str:pk>',go,name="go")
]
