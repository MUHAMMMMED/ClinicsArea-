from django.shortcuts import render
import os
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from webs.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from .filters import *
from django.http import JsonResponse
from django.db.models import Sum
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

@login_required
def dashboard(request):
    user = User.objects.get(id=request.user.id)
    weB = WEB.objects.filter(Employee_WEB=user)
    categories = Categories.objects.filter(web__Employee_WEB=user)
    doctors = Doctors.objects.filter(web__in=weB)
    department=Department.objects.filter(web__in=weB)
    section = Section.objects.filter(web__in=weB)
    insurance = Insurance.objects.filter(web__in=weB)
    image= Image.objects.filter(web__in=weB)
    questions=Questions.objects.filter(web__in=weB)
    count = Appointment.objects.filter(web__Employee_WEB=user, status_appointment='انتظار').count()
        # Retrieve the Service objects that belong to the specific Categories object(s)
    services = Service.objects.filter(category_id__in=categories)
    context = {
        'count': count ,
        'weB': weB,
        'user': user,
        'categories': categories,
        'services': services,
        'Section':section,
        'doctors':doctors,
        'Insurance':insurance,
        'Image':image,
        'Questions':questions,
        'department':department,
    }
    return render(request, 'dashboard.html', context)



@login_required
def create_web(request):
    if not request.user.is_employee():
        return redirect('Dashboard:display_bookings')  # or any other URL you want
    if request.method == 'POST':
        form = WebForm(request.POST, request.FILES )
        if form.is_valid():
            web = form.save(commit=False)
        if form.is_valid():
            web = form.save(commit=False)
            user = User.objects.get(id=request.user.id)
            web.Employee_WEB=user
            web.save()
            return redirect('Dashboard:dashboard')
    else:
        form = WebForm()
    return render(request, 'web_form.html', {'form': form})

@login_required
def update_web(request, pk):
    # Retrieve the object you want to update
    web = get_object_or_404(WEB, pk=pk)
    if request.method == 'POST':
        # Create a form instance with the updated data
        form = WebForm(request.POST, request.FILES, instance=web)
        if form.is_valid():
            # Save the changes to the database
            form.save()
            return redirect('Dashboard:dashboard')
    else:
        # Create a form instance with the current data
        form = WebForm(instance=web)
    return render(request, 'web_form.html', {'form': form})



#  start Doctor
@login_required
def create_doctor(request ):
    # Retrieve the WEB instance that the doctor will be related to
    if request.method == 'POST':
        # If the form has been submitted, create a new instance and save it
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            web = WEB.objects.filter(Employee_WEB=request.user).first()
            new_doctor = form.save(commit=False)
            new_doctor.web = web
            new_doctor.save()
            return redirect('Dashboard:dashboard')
    else:
        # If the form has not been submitted, display the form
        form = DoctorForm()
    # Render the template with the form and the WEB instance
    title='  اضافه دكتور جديد'
    context = {'form': form, 'title':title }
    return render(request, 'create_doctor.html', context)


@login_required
def update_doctor(request, doctor_id):
    # Get the Doctor object with the given id
    doctor = get_object_or_404(Doctors, id=doctor_id)

    if request.method == 'POST':
        # Create a form instance with the submitted data and the Doctor object as the instance to update
        form = DoctorForm(request.POST, request.FILES, instance=doctor)

        if form.is_valid():
            # Save the updated Doctor object
            form.save()
            return redirect('Dashboard:dashboard')
    else:
        # Create a form instance with the Doctor object to pre-fill the form
        form = DoctorForm(instance=doctor)

    # Render the update doctor page with the form and doctor object
    title='  تحديث بيانات الدكتور    '
    context = {'form': form, 'title':title ,'doctor':doctor}
    return render(request, 'update_doctor.html', context)

@login_required
def delete_doctor(request, id):
    doctor = Doctors.objects.get(id=id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('Dashboard:dashboard')
    context = {'doctor': doctor}
    return render(request, 'delete_service.html', context)


#  start  Doctor


@login_required
def create_section(request ):
    if request.method == 'POST':
        form = SectionForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new Section object and save it
            section = form.save(commit=False)
            web = WEB.objects.filter(Employee_WEB=request.user).first()
            section.web = web
            section.save()
            return redirect('Dashboard:dashboard')
    else:
        form = SectionForm()
    title=' إضافة خدمات'
    context = {'form': form, 'title':title }
    return render(request, 'create_section.html', context)


@login_required
def update_section(request, section_id):
    # Get the section object with the given id
    section = get_object_or_404(Section, id=section_id)

    if request.method == 'POST':
        # Create a form instance with the submitted data and the section object as the instance to update
        form = SectionForm(request.POST, request.FILES, instance=section)

        if form.is_valid():
            # Save the updated Doctor object
            form.save()
            return redirect('Dashboard:dashboard')
    else:
        # Create a form instance with the section object to pre-fill the form
        form = SectionForm(instance=section)

    # Render the updatesection page with the form and doctor object
    title='  تحديث الخدمة '
    context = {'form': form, 'title':title ,'section':section}
    return render(request, 'update_section.html', context)



@login_required
def delete_section(request, id):
    section = Section.objects.get(id=id)
    if request.method == 'POST':
        section.delete()
        return redirect('Dashboard:dashboard')

    context = {'section': section}
    return render(request, 'delete_service.html', context)


#  end section




#  start department
@login_required
def create_department(request):
    # Get the WEB object with the given slug
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            # Create a new Department object and save it
            department = form.save(commit=False)
            web = WEB.objects.filter(Employee_WEB=request.user).first()
            department.web = web
            department.save()
            return redirect('Dashboard:dashboard')
    else:
        form = DepartmentForm()
    title=' إضافة قسم '
    context = {'form': form, 'title':title }
    return render(request, 'create_department.html', context)

@login_required
def update_department(request,  department_id):

    department = get_object_or_404(Department, id=department_id)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)

        if form.is_valid():

            form.save()
            return redirect('Dashboard:dashboard')
    else:
        form = DepartmentForm(instance=department)

    title='  تحديث القسم '
    context = {'form': form, 'title':title ,'department':department}
    return render(request, 'create_department.html', context)




@login_required
def delete_department(request, id):
    department = Department.objects.get(id=id)
    if request.method == 'POST':
        department.delete()
        return redirect('Dashboard:dashboard')

    context = {'department': department}
    return render(request, 'delete_service.html', context)

#  end department




#  start insurance
@login_required
def create_insurance(request  ):
    # Get the WEB object with the given slug
    if request.method == 'POST':
        form = InsuranceForm(request.POST)

        if form.is_valid():
            # Create a new Insurance object and save it
            insurance = form.save(commit=False)
            web = WEB.objects.filter(Employee_WEB=request.user).first()
            insurance.web = web
            insurance.save()
            return redirect('Dashboard:dashboard')
    else:
        form = InsuranceForm()
    title='  إضافة تأمين    '
    context = {'form': form, 'title':title }
    return render(request, 'create_insurance.html', context)


@login_required
def update_insurance(request, insurance_id):

    insurance = get_object_or_404(Insurance, id=insurance_id)

    if request.method == 'POST':
        form = InsuranceForm(request.POST, instance=insurance)

        if form.is_valid():

            form.save()
            return redirect('Dashboard:dashboard')
    else:
        form = InsuranceForm(instance=insurance)

    title=' تحديث  التأمين '
    context = {'form': form, 'title':title ,'insurance':insurance}
    return render(request, 'create_insurance.html', context)


@login_required
def delete_insurance(request, id):
    insurance = Insurance.objects.get(id=id)
    if request.method == 'POST':
        insurance.delete()
        return redirect('Dashboard:dashboard')

    context = {'insurance': insurance}
    return render(request, 'delete_service.html', context)
#  end insurance

#  start image
@login_required
def create_image(request ):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new Image object and save it
            image = form.save(commit=False)
            web = WEB.objects.filter(Employee_WEB=request.user).first()
            image.web = web
            image.save()
            return redirect('Dashboard:dashboard')
    else:
        form = ImageForm()
    title='إضافة صوره'
    context = {'form': form, 'title':title}
    return render(request, 'create_image.html', context)

@login_required
def update_image(request, image_id):

    image = get_object_or_404(Image, id=image_id)
    if request.method == 'POST':
        form = ImageForm(request.POST, instance=image)
        if form.is_valid():
            form.save()
            return redirect('Dashboard:dashboard')
    else:
        form = ImageForm(instance=image)

    title=' تحديث  الصورة  '
    context = {'form': form, 'title':title ,'image': image}
    return render(request, 'update_image.html', context)


@login_required
def delete_image(request, id):
    image = Image.objects.get(id=id)
    if request.method == 'POST':
        image.delete()
        return redirect('Dashboard:dashboard')

    context = {'image': image}
    return render(request, 'delete_service.html', context)

#  end image




#  start question
@login_required
def create_question(request ):
    # Get the WEB object with the given slug
    if request.method == 'POST':
        form = QuestionsForm(request.POST)

        if form.is_valid():
            # Create a new Questions object and save it
            question = form.save(commit=False)
            web = WEB.objects.filter(Employee_WEB=request.user).first()
            question.web = web
            question.save()

            return redirect('Dashboard:dashboard')
    else:
        form = QuestionsForm()
    title='   اضافة سؤال جديد '
    context = {'form': form, 'title':title }
    return render(request, 'create_question.html', context)

@login_required
def update_question(request, question_id):

    question = get_object_or_404(Questions, id=question_id)
    if request.method == 'POST':
        form = QuestionsForm(request.POST, instance=question)
        if form.is_valid():
            image = form.save()
            return redirect('Dashboard:dashboard')
    else:
        form = QuestionsForm(instance= question)

    title='   تحديث السؤال        '
    context = {'form': form, 'title':title ,'question': question}
    return render(request, 'create_question.html', context)



@login_required
def delete_question(request, id):
    question = Questions.objects.get(id=id)
    if request.method == 'POST':
        question.delete()
        return redirect('Dashboard:dashboard')

    context = {'question': question}
    return render(request, 'delete_service.html', context)



#  end question


#  start category
@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoriesForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            web = WEB.objects.filter(Employee_WEB=request.user).first()
            if web is None:
                # handle the case where no web instance is found for the current user
                pass
            else:
                category.web = web
                category.save()
                return redirect('Dashboard:dashboard')
    else:
        form = CategoriesForm()
    title='   اضافة تصنيف جديد        '
    context = {'form': form, 'title':title }
    return render(request, 'create_category.html',context)


@login_required
def update_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    if request.method == 'POST':
        form = CategoriesForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            if 'Image' in request.FILES:
                # Delete the previous image file if it exists
                if os.path.exists(category.Image.path):
                    os.remove(category.Image.path)
            category = form.save(commit=False)
            web = WEB.objects.filter(Employee_WEB=request.user).first()
            if web is None:
                # handle the case where no web instance is found for the current user
                pass
            else:
                category.web = web
                category.save()
                return redirect('Dashboard:dashboard')

    else:
        form = CategoriesForm(instance=category)
    title='   تحديث التصنيف        '
    context = {'form': form, 'title':title,'category':category }
    return render(request, 'update_category.html',context)



@login_required
def delete_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    if request.method == 'POST':
        # Delete the image file if it exists
        if category.Image:
            category.Image.delete()
        category.delete()
        return redirect('Dashboard:dashboard')

    context = {'category': category}
    return render(request, 'delete_category.html', context)

#  end category




#  start service

@login_required
def create_service(request):
    user = User.objects.get(id=request.user.id)
    weB = WEB.objects.filter(Employee_WEB=user)
    categories = Categories.objects.filter(web__Employee_WEB=user)
    print(categories)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            category_id = request.POST['category_id']
            category = Categories.objects.get(id=category_id)
            service.category_id = category
            service.save()
            return redirect('Dashboard:dashboard')
    else:
        form = ServiceForm(initial={'category_id': categories.first()})

    title='  إضافة عرض جديد  '
    context = {'form': form, 'title':title,'categories':categories}
    return render(request, 'create_service.html', context)


@login_required
def update_service(request, service_id):
    user = User.objects.get(id=request.user.id)
    weB = WEB.objects.filter(Employee_WEB=user)
    categories = Categories.objects.filter(web__Employee_WEB=user)
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            category_id = request.POST['category_id']
            category = Categories.objects.get(id=category_id)
            form.instance.category_id = category
            form.save()
            return redirect('Dashboard:dashboard')
    else:
        form = ServiceForm(instance=service, initial={'category_id': service.category_id})

    title='    تحديث  العرض  '
    context = {'form': form, 'title':title,'service':service,'categories':categories}
    return render(request, 'update_service.html', context)

@login_required
def Service_delete(request, id):
    service = Service.objects.get(id=id)

    if request.method == 'POST':
        service.delete()
        return redirect('Dashboard:dashboard')

    context = {'service': service}
    return render(request, 'delete_service.html', context)


#  end service


#  start  Appointment

@login_required
def Appointment_waiting(request):
   user = request.user
   weB = WEB.objects.filter(Employee_WEB=user)
   appointments = Appointment.objects.filter(web__Employee_WEB=user, status_appointment='انتظار')
   booking_filter = BookingFilter(request.GET, queryset=appointments)
   count_inquiries = Appointment.objects.filter(web__Employee_WEB=user, status_appointment='inquiries').count()
   count_waiting = Appointment.objects.filter(web__Employee_WEB=user, status_appointment='انتظار').count()
   count_notanswering = Appointment.objects.filter(web__Employee_WEB=user, status_appointment='notanswering').count()
   count_confirmed = Appointment.objects.filter(web__Employee_WEB=user, status_appointment='confirmed').count()
   count_visit = Appointment.objects.filter(web__Employee_WEB=user, status_appointment='visit').count()
   count_cancel = Appointment.objects.filter(web__Employee_WEB=user, status_appointment='cancel').count()

   title = 'انتظار'
   context = {
    'title': title,
    'Bookingfilter': booking_filter,
    'weB':weB,
    # count
    'count_waiting': count_waiting,
    'count_inquiries': count_inquiries,
    'count_notanswering': count_notanswering,
    'count_confirmed': count_confirmed,
    'count_visit': count_visit,
    'count_cancel': count_cancel,

   }

   return render(request, 'waiting.html', context)






@login_required
def Appointment_inquiries(request):
  user = User.objects.get(id=request.user.id)
  weB = WEB.objects.filter(Employee_WEB=user)
  booking = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='inquiries')
  Bookingfilter = BookingFilter(request.GET, queryset=booking)
  count_inquiries = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='inquiries').count()
  count_waiting = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='انتظار').count()
  count_notanswering = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='notanswering').count()
  count_confirmed = Appointment.objects.filter(web__Employee_WEB=user,status_appointment= 'confirmed').count()
  count_visit = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='visit').count()
  count_cancel = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='cancel').count()

  title='الاستفسار'
  context = {
  'title':title ,
  'Bookingfilter': Bookingfilter ,
   'weB':weB,
  # count
  'count_waiting':count_waiting,
  'count_inquiries':count_inquiries,
  'count_notanswering':count_notanswering,
  'count_confirmed':count_confirmed,
  'count_visit':count_visit,
  'count_cancel':count_cancel,
  }
  return render(request, 'waiting.html', context)




@login_required
def Appointment_notanswering(request):
  user = User.objects.get(id=request.user.id)
  weB = WEB.objects.filter(Employee_WEB=user)
  booking = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='notanswering')
  Bookingfilter = BookingFilter(request.GET, queryset=booking)
  # count
  count_inquiries = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='inquiries').count()
  count_waiting = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='انتظار').count()
  count_notanswering = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='notanswering').count()
  count_confirmed = Appointment.objects.filter(web__Employee_WEB=user,status_appointment= 'confirmed').count()
  count_visit = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='visit').count()
  count_cancel = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='cancel').count()

  title='عدم الرد'
  context = {
  'title':title ,
  'Bookingfilter': Bookingfilter ,
  'weB':weB,
  # count
  'count_waiting':count_waiting,
  'count_inquiries':count_inquiries,
  'count_notanswering':count_notanswering,
  'count_confirmed':count_confirmed,
  'count_visit':count_visit,
  'count_cancel':count_cancel,
  }
  return render(request, 'waiting.html', context)

@login_required
def Appointment_confirmed(request):
  user = User.objects.get(id=request.user.id)
  weB = WEB.objects.filter(Employee_WEB=user)
  booking = Appointment.objects.filter(web__Employee_WEB=user,status_appointment= 'confirmed')
  Bookingfilter = BookingFilter(request.GET, queryset=booking)
  # count
  count_inquiries = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='inquiries').count()
  count_waiting = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='انتظار').count()
  count_notanswering = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='notanswering').count()
  count_confirmed = Appointment.objects.filter(web__Employee_WEB=user,status_appointment= 'confirmed').count()
  count_visit = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='visit').count()
  count_cancel = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='cancel').count()

  title='حجز مؤكد'
  context = {
  'title':title ,
  'Bookingfilter': Bookingfilter ,
  'weB':weB,
  # count
  'count_waiting':count_waiting,
  'count_inquiries':count_inquiries,
  'count_notanswering':count_notanswering,
  'count_confirmed':count_confirmed,
  'count_visit':count_visit,
  'count_cancel':count_cancel,
  }
  # return render(request, 'confirmed.html', context)
  return render(request, 'waiting.html', context)

@login_required
def Appointment_visit(request):
  user = User.objects.get(id=request.user.id)
  weB = WEB.objects.filter(Employee_WEB=user)
  booking = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='visit')
  Bookingfilter = BookingFilter(request.GET, queryset=booking)

  # count
  count_inquiries = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='inquiries').count()
  count_waiting = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='انتظار').count()
  count_notanswering = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='notanswering').count()
  count_confirmed = Appointment.objects.filter(web__Employee_WEB=user,status_appointment= 'confirmed').count()
  count_visit = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='visit').count()
  count_cancel = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='cancel').count()
  title='حضر'


  context = {
  'title':title ,
  'Bookingfilter': Bookingfilter ,
  'weB':weB,
  # count
  'count_waiting':count_waiting,
  'count_inquiries':count_inquiries,
  'count_notanswering':count_notanswering,
  'count_confirmed':count_confirmed,
  'count_visit':count_visit,
  'count_cancel':count_cancel,
  }
  return render(request, 'waiting.html', context)

@login_required
def Appointmentcancel (request):
  user = User.objects.get(id=request.user.id)
  weB = WEB.objects.filter(Employee_WEB=user)
  booking = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='cancel')
  Bookingfilter = BookingFilter(request.GET, queryset=booking)
  # count
  count_inquiries = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='inquiries').count()
  count_waiting = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='انتظار').count()
  count_notanswering = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='notanswering').count()
  count_confirmed = Appointment.objects.filter(web__Employee_WEB=user,status_appointment= 'confirmed').count()
  count_visit = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='visit').count()
  count_cancel = Appointment.objects.filter(web__Employee_WEB=user,status_appointment='cancel').count()
  title='إلغاءحجزه'
  context = {
  'title':title ,
  'Bookingfilter': Bookingfilter ,
  'weB':weB,
  # count
  'count_waiting':count_waiting,
  'count_inquiries':count_inquiries,
  'count_notanswering':count_notanswering,
  'count_confirmed':count_confirmed,
  'count_visit':count_visit,
  'count_cancel':count_cancel,
  }
  # return render(request, 'cancel.html', context)
  return render(request, 'waiting.html', context)


@login_required
def update_status(request):

    appointment_id = request.GET.get('appointment_id')
    print('appointment_id', appointment_id)
    status = request.GET.get('status')
    print('status', status)
    appointment = Appointment.objects.get(id=appointment_id)
    print('appointment', appointment)
    appointment.status_appointment = status
    print('status_appointment', appointment)
    appointment.save()
    print('save', appointment)
    # Return a success response
    return JsonResponse({'success': True})

#  end  Appointment
#  start  Appointment


from django.db.models import Count

@login_required
def Report(request):

    user = get_object_or_404(User, id=request.user.id)
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)
    weB = WEB.objects.filter(Employee_WEB=user)
    # weB = WEB.objects.filter(Employee_WEB=user, created_at__range=[start_date, end_date])

    total_web_Click_whatsapp = weB.aggregate(click_count=Sum('Click_whatsapp'))
        # Click_whatsapp _Categories
    total_web_whatsapp_Categories = weB.aggregate(click_count=Sum('Click_whatsapp_Categories'))
        # views_HOME
    total_web_views  = weB.aggregate(click_count=Sum('views'))
        # total_web_views_ALL_Categories
    total_web_views_ALL_Categories = weB.aggregate(click_count=Sum('views_Categories'))
        # views_confirmation
    total_web_views_confirmation  = weB.aggregate(click_count=Sum('views_confirmation'))
        # views_checkout
    total_web_views_checkout  = weB.aggregate(click_count=Sum('views_checkout'))

    if start_date and end_date:
        cat= Categories.objects.filter(web__Employee_WEB=user, created_at__range=[start_date, end_date]).annotate(appointment_count=Count('Services__appointment'))
        ser = Service.objects.filter(category_id__in=cat, created_at__range=[start_date, end_date]).annotate(appointment_count=Count('appointment'))
    else:
        cat= Categories.objects.filter(web__Employee_WEB=user).annotate(appointment_count=Count('Services__appointment'))
        ser = Service.objects.filter(category_id__in=cat).annotate(appointment_count=Count('appointment'))




        # Categories
    # cat= Categories.objects.filter(web__Employee_WEB=user, created_at__range=[start_date, end_date])
        # Click_whatsapp
    total_categories_clicks = cat.aggregate(click_count=Sum('Click_whatsapp'))
        # views_Categories
    total_categories_views= cat.aggregate(click_count=Sum('views'))

    # ser = Service.objects.filter(category_id__in=cat, created_at__range=[start_date, end_date])


        # Click_whatsapp
    total_services_clicks = ser.aggregate(click_count=Sum('Click_whatsapp'))

    total_services_views = ser.aggregate(click_count=Sum('views'))

    # status_appointment_counts = Appointment.objects.values('status_appointment__title').annotate(count=Count('id'))
    # Type_appointment_counts = Appointment.objects.values('Type_appointment__title').annotate(count=Count('id'))



        # total_clicks_whatsapp
    total_views = sum([
        total_web_views.get('click_count', 0) or total_web_views.get('click_count') == 0,
        total_web_views_ALL_Categories.get('click_count', 0) or
        total_web_views_ALL_Categories.get('click_count') == 0,
        total_web_views_confirmation.get('click_count', 0) or
        total_web_views_confirmation.get('click_count') == 0,
        total_web_views_checkout.get('click_count', 0) or
        total_web_views_checkout.get('click_count') == 0,

        total_categories_views.get('click_count', 0) or
        total_categories_views.get('click_count') == 0,
        total_services_views.get('click_count', 0) or
        total_services_views.get('click_count') == 0,
    ])

        # total_clicks_whatsapp
    total_clicks = sum([
    total_categories_clicks.get('click_count', 0) or total_categories_clicks.get('click_count') == 0,
    total_services_clicks.get('click_count', 0) or total_services_clicks.get('click_count') == 0,
    total_web_Click_whatsapp.get('click_count', 0) or total_web_Click_whatsapp.get('click_count') == 0,
    total_web_whatsapp_Categories.get('click_count', 0) or total_web_whatsapp_Categories.get('click_count') == 0,
    ])

    context = {
        'web': weB,
        'user': user,
        'categories': cat,
        'services': ser,
        # total_views
        'total_views':total_views,
        # clicks_whatsapp
        'total_clicks':total_clicks ,

        'categories_count': total_categories_clicks,
        'total_services_clicks':total_services_clicks,
        'total_web_Click_whatsapp':total_web_Click_whatsapp,
        'total_web_whatsapp_Categories':total_web_whatsapp_Categories,

        'total_web_views_ALL_Categories':total_web_views_ALL_Categories,
        'total_services_views':total_services_views,
        'total_categories_clicks':total_categories_clicks,
        'total_categories_views':total_categories_views,






    }
    return render(request, 'report.html', context)
