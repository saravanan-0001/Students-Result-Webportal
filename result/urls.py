from django.urls import path
from . import views

urlpatterns=[
    path('getmark',views.getmark,name='getmark')
]