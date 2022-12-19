from django.shortcuts import render
from django.http import HttpResponse


def basic(request):
    return render(request, "htmlbasic.html")


# def base2(request):
#     return render(request, "base2.html")


# def contact(request):
#     return render(request, "contact.html")

