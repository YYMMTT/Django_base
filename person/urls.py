from django.urls import path

from person.views import create_book
urlpatterns =[
    path('create',create_book)
]