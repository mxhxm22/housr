from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Property
from .forms import PropertyForm
from django.contrib.auth.models import User, auth
from django.contrib import messages


def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

class PropertyDetailView(DetailView):
    model = Property
    context_object_name = 'property'
    template_name = 'property_detail.html'


def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'create_property.html', {'form': form})

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2:       
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                print('User Created')
                return redirect('login')

        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')