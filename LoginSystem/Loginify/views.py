from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserDetails

def hello_world(request):
    return HttpResponse("Hello world!")

# Signup View
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if UserDetails.objects.filter(email=email).exists():
            return HttpResponse("Email already registered. Try logging in.")

        user = UserDetails(username=username, email=email, password=password)
        user.save()

        return redirect("login")  # Redirect to login page upon success

    return render(request, "signup.html")  # Show signup form

# Login View
def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = UserDetails.objects.get(email=email, password=password)
            return HttpResponse(f"Welcome, {user.username}! Login Successful.")  # Show success message
        except UserDetails.DoesNotExist:
            return HttpResponse("Invalid email or password.")

    return render(request, "login.html")  # Show login form