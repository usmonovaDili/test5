from django.urls import path
from .views import *

urlpatterns=[
    path('',info),
    path('all/',info2)
]
