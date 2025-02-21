from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserDetails


def Hello_World(request):
    return HttpResponse("Hello World!")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if UserDetails.objects.filter(email=email).exists():
            return HttpResponse("Email already registered!")

        user = UserDetails(username=username, email=email, password=password)
        user.save()

        return redirect("login") 

    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = UserDetails.objects.get(email=email)
            if user.password == password:
                return HttpResponse("Login successful!")
            else:
                return HttpResponse("Invalid password!")
        except UserDetails.DoesNotExist:
            return HttpResponse("User does not exist!")

    return render(request, "login.html")
