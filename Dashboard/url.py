from django.contrib import admin
from django.urls import path
from  Dashboard.views  import *

app_name='Dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard'),

    path('create/', create_web, name='create_web'),
    path('web/<int:pk>/update/', update_web, name='web_update'),

    path('create_doctor/', create_doctor, name='create_doctor'),
    path('doctors/<int:doctor_id>/update/',  update_doctor, name='update_doctor'),
    path('doctor/<int:id>/delete_doctor/',  delete_doctor, name='delete_doctor'),

    path('create_section/', create_section, name='create_section'),
    path('section/<int:section_id>/update/',  update_section, name='update_section'),
    path('section/<int:id>/delete_section/',  delete_section, name='delete_section'),

    path('create_insurance/', create_insurance, name='create_insurance'),
    path('insurance/<int:insurance_id>/update/',  update_insurance, name='update_insurance'),
    path('insurance/<int:id>/delete_insurance/', delete_insurance, name='delete_insurance'),

    path('create_image/', create_image, name='create_image'),
    path('image/<int:image_id>/update/',  update_image, name='update_image'),
    path('image/<int:id>/delete_image/',  delete_image, name='delete_image'),

    path('create_question/', create_question, name='create_question'),
    path('question/<int:question_id>/update/',  update_question, name='update_question'),
    path('question/<int:id>/delete_question/',  delete_question, name='delete_question'),

    path('create_department/', create_department, name='create_department'),
    path('department/<int:department_id>/update/', update_department, name='update_department'),
    path('department/<int:id>/delete_department/',  delete_department, name='delete_department'),

    path('create_category/', create_category, name='create_category'),
    path('<int:pk>/update_category/', update_category, name='update_category'),
    path('categories/<int:pk>/delete/',delete_category, name='delete_category'),

    path('create_service/', create_service, name='create_service'),
    path('update_service/<int:service_id>/',update_service, name='update_service'),
    path('services/<int:id>/Service_delete/',  Service_delete, name='delete_service'),




    # other URL patterns for your app

    path('Appointment_waiting/', Appointment_waiting, name='Appointment_waiting'),
    path('Appointment_notanswering/', Appointment_notanswering, name='Appointment_notanswering'),
    path('Appointment_confirmed/', Appointment_confirmed, name='Appointment_confirmed'),
    path('Appointment_inquiries/', Appointment_inquiries, name='Appointment_inquiries'),
    path('Appointment_cancel/', Appointmentcancel, name='Appointment_cancel'),
    path('Appointment_visit/', Appointment_visit, name='Appointment_visit'),

    path('update_status/', update_status, name='update_status'),
    path('report/', Report, name='Report'),

]
