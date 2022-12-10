from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('find_password', views.search_password, name="find_password"),
    path('generate_password', views.generate_password, name="generate_password"),
]