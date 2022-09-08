from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name = "index"),
   path('delete/<str:name_of_city>/', views.deleteview, name="delete")
]