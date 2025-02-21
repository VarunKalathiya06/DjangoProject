from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import UserDetails
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserDetailsSerializer 
import json


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


@csrf_exempt
@api_view(['POST'])
def login(request):
    if request.method == "POST":
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = UserDetails.objects.get(email=email)
            if user.password == password:
                return JsonResponse({"message": "Login successful!"})
            else:
                return JsonResponse({"error": "Invalid password!"}, status=400)
        except UserDetails.DoesNotExist:
            return JsonResponse({"error": "User does not exist!"}, status=404)

    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserDetailsSerializer(data=request.data)  

        if serializer.is_valid():
            user = serializer.save()  
            return JsonResponse({"message": "User created successfully", "user_id": user.id}, status=201)
        return JsonResponse(serializer.errors, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
@api_view(['GET'])
def get_all_users(request):
    if request.method == "GET":
        users = UserDetails.objects.all()
        serializer = UserDetailsSerializer(users, many=True)  
        return Response({"users": serializer.data})

    return JsonResponse({"error": "Invalid request method"}, status=400)


@api_view(['GET'])
def get_user_by_email(request, email):
    try:
        user = UserDetails.objects.get(email=email)
        serializer = UserDetailsSerializer(user)  
        return Response(serializer.data)
    except UserDetails.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)


@csrf_exempt
@api_view(['PUT'])
def update_user(request, email):
    try:
        user = UserDetails.objects.get(email=email)
    except UserDetails.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

    serializer = UserDetailsSerializer(user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "User updated successfully"})
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@api_view(['DELETE'])
def delete_user(request, email):
    try:
        user = UserDetails.objects.get(email=email)
        user.delete()
        return JsonResponse({"message": "User deleted successfully"})
    except UserDetails.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

