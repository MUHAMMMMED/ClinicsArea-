from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import  *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import*
from django.views.decorators.csrf import csrf_protect



#
# # login
# @csrf_protect
# def login_request(request):
#     if request.method=='POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             user = User.objects.get(id=request.user.id)
#
#             login(request,user)
#             return redirect('User:home_view')
#
#         else:
#                 messages.error(request,"Invalid username or password")
#     return render(request, '../templates/login.html',
#     context={'form':AuthenticationForm()})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import User

@csrf_protect
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('User:home_view')
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@csrf_protect
@login_required
def home_view(request):
    if request.user.is_authenticated:
        if request.user.is_employee():
            return redirect('Dashboard:dashboard')
        elif request.user.is_manager():
            return redirect('User:manager_dashboard')
        elif request.user.is_hospital():
            return redirect('User:hospital_dashboard')

    return render(request, '../templates/login.html')

# cccccccccccccccccccc



from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model


User = get_user_model()
#
# def password_reset(request):
#     user_queryset = User.objects.all()
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         new_password = request.POST.get('new_password')
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             # Handle the case where the user does not exist
#             user = None
#         if user is not None:
#             # Update the user's password using the `update()` method
#             user.set_password(new_password)
#             User.objects.filter(pk=user.pk).update(password=user.password)
#             # Redirect to the manager dashboard after successful password reset
#             return redirect('User:manager_dashboard')
#
#     return render(request, 'password_reset.html', {'user_queryset': user_queryset})
# def home(request):
#     return render(request, '../templates/Customer.html')
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

User = get_user_model()

def password_reset(request):
    user_queryset = User.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Handle the case where the user does not exist
            user = None
        if user is not None:
            # Update the user's password using the `update()` method
            user.set_password(new_password)
            User.objects.filter(pk=user.pk).update(password=user.password)
            # Redirect to the manager dashboard after successful password reset
            return redirect('User:manager_dashboard')

    return render(request, 'password_reset.html', {'user_queryset': user_queryset})





@login_required
def manager(request):

    return render(request, '../templates/index.html')




@login_required
def hospital(request):
    return render(request, '../templates/index.html')

@login_required
def employee(request):
    return render(request, '../templates/employee.html')


class Manager_register(CreateView):
    model = User
    form_class = ManagerSignUpForm
    template_name = '../templates/Signup.html'
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('User:manager_dashboard')






class Hospital_register(CreateView):
    model = User
    form_class = HospitalSignUpForm
    template_name = '../templates/Signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('User:doctor_dashboard')

class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = '../templates/Signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('Dashboard:dashboard')

# logout
def logout_view(request):
    logout(request)
    return redirect('/')
