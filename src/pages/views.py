from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)

    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def info_view(request, *args, **kwargs):
    my_contect = {
        "my_text": "This is about me",
        "my_number": 5564322,
        "my_slut": [23423, 324324, 33]
    }
    return render(request, "info.html", my_contect)

def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})