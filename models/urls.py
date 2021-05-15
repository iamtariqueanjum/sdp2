from django.urls import path

from .views import *

urlpatterns = [
    path('',models_home, name='models-home'),
    path('details/<int:id>/',detail,name='models-detail'),
]