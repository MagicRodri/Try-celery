from django.urls import include, path

from .views import fibonacci_create, fibonacci_list

urlpatterns = [
    path('',fibonacci_create,name='fibonacci-create'),
    path('list/',fibonacci_list,name='fibonacci-list')
]
