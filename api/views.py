from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework import generics
from .serializers import studentSerializer
from .models import students
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

"""
filtering using serach filter
This works same as how filters work on admin panel
it is the same implementation as adminpanel filters
"""
class studentapi1(generics.ListAPIView):
    serializer_class=studentSerializer
    queryset=students.objects.all()
    filter_backends=[SearchFilter]
    search_fields=['name'] #we can only serach using the fields mentioned in this
                            #now we can only serch with these fields
                
    """we can use lookup in the fields like
        serach_fields=['=name'] --> This will search against the exact name,
        like so we have ^ -->startswith,
        regext --> $,
        and @ 
    """


"""fliltering using DjangoFilterBackend class 
Need to install this library to work with ,it supports highly 
customizable field filtering for rest_framework

pip install django-filter

add in Installed apps

django_filters

we can read docs in https://django-filter.readthedocs.io/en/latest/index.html

in settings.py use this global setting:

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS':['django_filters.rest_framework.DjangoFilterBackend'],
}

we can set it for per view basis:

for this:
    fron django_filerts.rest_framework import DjangoFilterBackend
class studentapi(generics.ListAPIView):
    serializer_class=studentSerializer
    queryset=students.objects.all()
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['name']

"""

class studentapi2(generics.ListAPIView):
        serializer_class=studentSerializer
        queryset=students.objects.all()
        filter_backends=[DjangoFilterBackend]
        filterset_fields=['name','city']
                          


"""OrderingFilter

    By default, the query parameter is named 'ordering', but this may by overridden with the ORDERING_PARAM setting.

    Ex:http://example.com/api/users?ordering=username

    class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['username', 'email']

"""



class studentapi3(generics.ListAPIView):
        serializer_class=studentSerializer
        queryset=students.objects.all()
        filter_backends=[OrderingFilter]
        ordering_fields=['name','city']
        ordering=['-name']

"""Specifying a default ordering
If an ordering attribute is set on the view, this will be used as the default ordering."""