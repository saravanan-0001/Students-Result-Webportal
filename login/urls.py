from django.urls import path
from . import views

urlpatterns=[
    path('signin',views.signin,name='signin'),
    path('enter',views.enter,name='enter'),
    path('update',views.update,name='update')
]