from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='familiares-index'),
    path('filter/',views.filter_input, name='familiares-filter'),
]