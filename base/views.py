from django.shortcuts import render, redirect
import joblib
import pickle
import numpy as np
from django.core.mail import send_mail
from sklearn.preprocessing import StandardScaler
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User

# Global scaler variable
global scaler

def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Username or Password is incorrect!")

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')




# Function to make predictions using the features POONDI, CHOLAVARAM, REDHILLS, and CHEMBARAMBAKKAM
def getPredictions(poondi, cholavaram, redhills, chembarambakkam):
    model = joblib.load('linear_model.pkl')  # Load your saved model
    features = np.array([[poondi, cholavaram, redhills, chembarambakkam]])
    prediction = model.predict(features)
    return prediction[0]

# Result view to display prediction results
def result(request):
    # Retrieve feature values from the request
    poondi = float(request.GET['POONDI'])
    cholavaram = float(request.GET['CHOLAVARAM'])
    redhills = float(request.GET['REDHILLS'])
    chembarambakkam = float(request.GET['CHEMBARAMBAKKAM'])

    # Get the prediction
    result = getPredictions(poondi, cholavaram, redhills, chembarambakkam)

    return render(request, 'result.html', {'result': result})