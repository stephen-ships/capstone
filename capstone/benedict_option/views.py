from typing import Text
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, request
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import random
import json
from .models import User, Prayer


def index(request):
    count = Prayer.objects.count()
    # Always load a random prayer on the first load up
    text = get_object_or_404(Prayer, pk=random.randint(1, count))
    return render(request, "benedict_option/index.html", {
    "text": text
    })

# def selectTime(request, time):



def loadPrayerLength(request, length):
    prayer = get_object_or_404(Prayer, length=length)

    test = prayer.to_json()
    return JsonResponse(test, safe=False)


def pray(request):
    return render(request, "benedict_option/pray.html")

# Copied from CS33a Project 4. Modified url paths
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "benedict_option/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "benedict_option/login.html")


# Copied from CS33a Project 4. Modified url paths
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# Copied from CS33a Project 4. Modified url paths
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "benedict_option/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "benedict_option/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "benedict_option/register.html")
