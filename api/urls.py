from django.urls import path
from . import views
urlpatterns=[ 
    path('1/',views.studentapi1.as_view()),
    path('2/',views.studentapi2.as_view()),
    path('3/',views.studentapi3.as_view()),
]