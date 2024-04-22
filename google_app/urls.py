from django.urls import path
from . import views 

app_name = "google_app"

urlpatterns = [
    path('', views.login, name = 'login'),
]

