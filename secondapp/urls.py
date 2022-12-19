from django.urls import path
from secondapp import views

app_name = 'secondapp'

urlpatterns = [
    path('home/', views.home, name="secondapphome")
]
