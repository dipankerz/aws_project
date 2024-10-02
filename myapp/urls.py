# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.name_search_view, name='name_search'),
    path('add/<str:name>/', views.add_person_view, name='add_person'),
]
