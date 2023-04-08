from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import Sign_Up_Form, Add_Record_Form
from . models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()

    # checks if a user has logged in
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']

        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Karibu, {username} You're logged in.")
            return redirect('home')
        else:
            messages.success(request, "Error logging in")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})

# def login_user(request):
#     pass

# Handles logout requests
def logout_user(request):

    logout(request)
    messages.success(request, "Adios you've been logged out")
    return redirect('home')
   
# view/request handeler for registration   
def register_user(request):
    if request.method == "POST":
        form = Sign_Up_Form(request.POST)
        if form.is_valid():
            form.save()

            # authenticate and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You are successfully registred")
            return redirect('home')       
    else:
        form = Sign_Up_Form()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

def employee_record(request, pk):
    if request.user.is_authenticated:
        # lookup the record to get a single objetc/item using the get method
        employee_record = Record.objects.get(id=pk)

        return render(request, 'record.html', {'employee_record': employee_record})
    else:
        messages.success(request, "You must be logged in to view")
        return redirect('home')
    
# function to delete selected employee 
def delete_employee(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Employee Deleted")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')
    
def add_record(request):
    form = Add_Record_Form(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "record added")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = Add_Record_Form(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')



        




