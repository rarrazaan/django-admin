import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import os

# Create your views here.
def reset_password(request, id):
    if request.method == "POST":
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        
        if new_password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect(request.path)

        # Send the request to the backend API
        api_url = os.getenv("API_URL")
        url = f"{api_url}/v1/user/change-password/{id}"
        headers = {
            "Authorization": f"{settings.API_TOKEN}",  # Replace with your token
            "Content-Type": "application/json",
        }
        payload = {"password": new_password}

        try:
            response = requests.put(url, json=payload, headers=headers)
            if response.status_code == 200:
                messages.success(request, "Password changed successfully!")
                return redirect("admin:index")  # Redirect to admin panel
            else:
                messages.error(request, f"Error: {response.json().get('message', 'Unknown error')}")
        except requests.RequestException as e:
            messages.error(request, f"Request error: {str(e)}")

    return render(request, 'change-password.html', {'id': id})