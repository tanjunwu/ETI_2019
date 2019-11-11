from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_index, name="home_index"),
    path("<int:pk>/", views.home_detail, name="home_detail"),
]
