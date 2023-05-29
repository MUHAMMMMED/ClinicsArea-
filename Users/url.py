from django.urls import path
from .views import*
app_name='Users'
#
urlpatterns=[
#
     path('login/',login_request, name='login'),
     path('home_view',home_view, name='home_view'),
     path('hospital',hospital, name='hospital_dashboard'),
     path('manager',manager, name='manager_dashboard'),
     path('employee',employee, name='employee_dashboard'),
 
     path('Manager_register/',Manager_register.as_view(), name='ManagerRegister'),
     path('Hospital_register/',Hospital_register.as_view(), name='Hospitalregister'),
     path('employee_register/',employee_register.as_view(), name='employeeRegister'),
     path('password_reset/',password_reset, name='password_reset'),
     path('logout/',logout_view, name='logout'),
]
