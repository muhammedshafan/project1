from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('home/', views.home, name="myapphome")
]
