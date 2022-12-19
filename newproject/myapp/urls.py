from django.urls import path
from . import views

urlpatterns = [
    path('', views.basic, name='htmlbasic'),
    # path('', views.base2, name="base2"),
    # path("contact/", views.contact, name="contact"),
]
