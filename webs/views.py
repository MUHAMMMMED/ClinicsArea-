
from webs.models import *
from webs.BaseData_processors import *
import pandas as pd
from webs.form import *
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.contrib.sessions.backends.db import SessionStore
from .models import *
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt




# # Create your views here.
def home(request):

    context = {   }
    return render(request, 'home.html', context)


def web(request, web_slug):
    # Get the WEB object with the given slug
    web = get_object_or_404(WEB, slug=web_slug)
    # Get all Categories objects for the current web object
    categories = Categories.objects.filter(web=web)
    doctors = Doctors.objects.filter(web=web)
    section = Section.objects.filter(web=web)
    insurance = Insurance.objects.filter(web=web)
    image= Image.objects.filter(web=web)
    questions=Questions.objects.filter(web=web)
    department=Department.objects.filter(web=web)
    # Create a dictionary to store the categories and their related services
    category_services = {}
    # Loop through each category and get its related services
    for category in categories:
        services = category.Services.all()
        category_services[category] = services

    # Render the categories_services template with the category_services dictionary
    if request.method=='POST':
        form= BookingForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.web=web
            myform.save()
            print('DOne')
            return redirect('webs:booking_confirmation', web_slug=web_slug)
    else:
        form = BookingForm()
        print('404')

    session_key = request.session.session_key
    if session_key:
        cart_item_count = CartItem.objects.filter(session_id=session_key, web=web).count()
    else:
        cart_item_count = 0

    if web.views is None:
        web.views = 0
    web.views += 1
    web.save()
    context = {
    'web': web,
    'category_services': category_services,
    'cart_item_count': cart_item_count,
    'form': form ,
     'doctors':doctors,
    'section':section,
    'insurance':insurance ,
    'image':image,
    'questions':questions,
    'department':department, }
 # Render the web template with the web object
    return render(request, 'WEb.html', context )


def increment_click_web_whatsapp(request, web_slug):
    try:
        web = get_object_or_404(WEB, slug=web_slug)
        if web.Click_whatsapp is None:
            web.Click_whatsapp = 0
        web.Click_whatsapp += 1
        web.save()
        return JsonResponse({'click_whatsapp': web.Click_whatsapp})
    except web.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)









def add_to_cart(request, id):
    # Get or create session
    session_key = request.session.session_key
    if not session_key:
        request.session.save()
        session_key = request.session.session_key
    # Get service object
    service = get_object_or_404(Service, id=id)
    web = service.category_id.web
    # Get cart item or create new one
    cart_item, created = CartItem.objects.get_or_create(
        session_id=session_key,
        service=service,
        web=web,    )

    cart_item_count = CartItem.objects.filter(session_id=session_key).count()
    data = {'cart_item_count': cart_item_count}
    return JsonResponse(data)










def categories_services(request, web_slug):
    # Get the web object for the current request
    web = get_object_or_404(WEB, slug=web_slug)
    # Get all Categories objects for the current web object
    categories = Categories.objects.filter(web=web)
    # Create a dictionary to store the categories and their related services
    category_services = {}
    # Loop through each category and get its related services
    for category in categories:
        services = category.Services.all()
        category_services[category] = services

    # Get the cart item count for the current session
    session_key = request.session.session_key
    if session_key:
        cart_item_count = CartItem.objects.filter(session_id=session_key, web=web).count()
    else:
        cart_item_count = 0

    if web.views is None:
        web.views_Categories = 0
    web.views_Categories += 1
    web.save()

    # Render the categories_services template with the category_services dictionary
    return render(request, 'categories_services.html', {'category_services': category_services,'cart_item_count':cart_item_count,'web': web})


#

def increment_click_web_category_whatsapp(request, web_slug):
    try:
        web = get_object_or_404(WEB, slug=web_slug)
        if web.Click_whatsapp_Categories is None:
            web.Click_whatsapp_Categories = 0
        web.Click_whatsapp_Categories += 1
        web.save()
        return JsonResponse({'click_whatsapp': web.Click_whatsapp_Categories})
    except web.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)


def categories(request, web_slug, id):
    # Get the web object for the current request
    web = get_object_or_404(WEB, slug=web_slug)
    # Get the category object for the current request
    category = get_object_or_404(Categories, id=id, web=web)
    categories_nav = Categories.objects.filter(web=web)
    # Get the cart item count for the current session
    session_key = request.session.session_key
    if session_key:
        cart_item_count = CartItem.objects.filter(session_id=session_key, web=web).count()
    else:
        cart_item_count = 0

    if category.views is None:
        category.views = 0
    category.views += 1
    category.save()
    return render(request, 'categories.html', {'category': category, 'web': web, 'cart_item_count':cart_item_count,'categories_nav': categories_nav})





def increment_click_category_whatsapp(request, category_id):
    try:
        category = Categories.objects.get(id=category_id)
        if category.Click_whatsapp is None:
            category.Click_whatsapp = 0
        category.Click_whatsapp += 1
        category.save()
        return JsonResponse({'click_whatsapp': category.Click_whatsapp})
    except Categories.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)



def services(request, web_slug, category_id, service_id):


    try:
        # Get the web object for the current request
        web = get_object_or_404(WEB, slug=web_slug)
        categories_nav = Categories.objects.filter(web=web)
        # Get the category object for the current request
        category = get_object_or_404(Categories, id=category_id, web=web)
        # Get the service object for the current request
        service = get_object_or_404(Service, id=service_id, active=True)

        # Get all other services in the same category
        services_in_category = Service.objects.filter(category_id=category.id).exclude(id=service.id)

    except:
        # Display an error message if the requested category or service does not exist
        return render(request, 'error.html', {'message': 'The requested service could not be found.'})

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the booking and associate it with the current service
            booking = form.save(commit=False)
            booking.web = web # Set the web attribute of the booking object
            booking.save()
            booking.service.set([service])

            # Redirect the user to a confirmation page or some other view
            return redirect('webs:booking_confirmation', web_slug=web_slug)
    else:
        # Display an empty booking form
        form = BookingForm()

    # Get the cart item count for the current session
    session_key = request.session.session_key
    if session_key:
        cart_item_count = CartItem.objects.filter(session_id=session_key, web=web).count()
    else:
        cart_item_count = 0

    if service.views is None:
        service.views = 0
    service.views += 1
    service.save()
    # rest of the code
    # ... render the service detail template with the updated service object ...
    context = {
        'web': web,
        'category': category,
        'service': service,
        'services_in_category': services_in_category,
        'form': form,
        'categories_nav': categories_nav,
        'cart_item_count':cart_item_count
    }
    return render(request, 'salh.html', context)


def increment_click_whatsapp(request, service_id):
    try:
        service = Service.objects.get(id=service_id)
        if service.Click_whatsapp is None:
            service.Click_whatsapp = 0
        service.Click_whatsapp += 1
        print('service',service.Click_whatsapp)
        service.save()
        return JsonResponse({'click_whatsapp': service.Click_whatsapp})
    except Service.DoesNotExist:
        return JsonResponse({'error': 'Service not found'}, status=404)



def cart_and_checkout(request, web_slug):
    # Get the current session
    session_key = request.session.session_key
    if not session_key:
        request.session.save()
        session_key = request.session.session_key
    session = Session.objects.get(session_key=session_key)

    # Get all the cart items for the current session and web
    web = WEB.objects.get(slug=web_slug)
    categories_nav = Categories.objects.filter(web=web)
    cart_items = CartItem.objects.filter(session=session, web=web)

    if request.method == 'POST':
        # Create a new booking object and add the cart items to it
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.web = web
            booking.save()
            for cart_item in cart_items:
                booking.service.add(cart_item.service)

            # Delete the cart items for the current session and web
            cart_items.delete()
            return redirect('webs:booking_confirmation', web_slug=web_slug)
    else:
        booking_form = BookingForm()

        # Calculate the total price of the cart items
        total_price = sum(cart_item.service.price for cart_item in cart_items)
    if web.views_checkout is None:
        web.views_checkout = 0
    web.views_checkout += 1
    web.save()
    return render(request, 'cart.html', {'cart_items': cart_items, 'booking_form': booking_form, 'total_price': total_price , 'web':web,'categories_nav':categories_nav})






#
# import phonenumbers
# from twilio.rest import Client
#
#
# def cart_and_checkout(request, web_slug):
#     # Get the current session
#     session_key = request.session.session_key
#     if not session_key:
#         request.session.save()
#         session_key = request.session.session_key
#     session = Session.objects.get(session_key=session_key)
#
#     # Get all the cart items for the current session and web
#     web = WEB.objects.get(slug=web_slug)
#     categories_nav = Categories.objects.filter(web=web)
#     cart_items = CartItem.objects.filter(session=session, web=web)
#
#     if request.method == 'POST':
#         # Create a new booking object and add the cart items to it
#         booking_form = BookingForm(request.POST)
#         if booking_form.is_valid():
#             booking = booking_form.save(commit=False)
#             booking.web = web
#             booking.save()
#             for cart_item in cart_items:
#                 booking.service.add(cart_item.service)
#
#             # Send a WhatsApp message with the booking details
#             account_sid = 'your_account_sid'
#             auth_token = 'your_auth_token'
#             client = Client(account_sid, auth_token)
# # Create the message body
#
#
#             message_body = f'New booking made on {web.slug}:\n'
#             message_body += f'Booking ID: {booking.id}\n'
#             message_body += f'Service(s): {", ".join(str(service) for service in booking.service.all())}\n'
#             # message_body += f'Total price: {booking.total_price}\n'
#             message_body += f'Customer name: {booking.name}\n'
#             # message_body += f'Customer email: {booking.customer_email}\n'
#             # message_body += f'Customer phone: {booking.customer_phone}\n'
#
#             # Send the message
#             try:
#                 phone_number = phonenumbers.parse(recipient)
#                 if not phonenumbers.is_valid_number(phone_number):
#                     raise ValueError('Invalid phone number')
#                 recipient = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)
#                 message = client.messages.create(
#                     body=message_body,
#                     from_='whatsapp:+20112003453',  # Replace with your own Twilio WhatsApp number
#                     to=recipient
#                 )
#             except Exception as e:
#                 print(f'Error sending WhatsApp message: {e}')
#
#             # Delete the cart items for the current session and web
#             cart_items.delete()
#             return redirect('webs:booking_confirmation', web_slug=web_slug)
#     else:
#         # bookingAnd here's the rest of the code:
#
#
#         booking_form = BookingForm()
#
#         # Calculate the total price of the cart items
#         total_price = sum(cart_item.service.price for cart_item in cart_items)
#     if web.views_checkout is None:
#         web.views_checkout = 0
#     web.views_checkout += 1
#     web.save()
#     return render(request, 'cart.html', {'cart_items': cart_items, 'booking_form': booking_form, 'total_price': total_price , 'web':web,'categories_nav':categories_nav})
#
#
















@csrf_exempt
def cart_item_delete_view(request):
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id')
        try:
            cart_item = CartItem.objects.get(id=cart_item_id)
            cart_item.delete()
            return JsonResponse({'success': True})
        except CartItem.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'CartItem does not exist.'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})



def cart_item_refresh_view(request):
    if request.method == 'GET':
        cart_items = CartItem.objects.all()
        cart_item_data = []
        for cart_item in cart_items:
            cart_item_data.append({
                'id': cart_item.id,
                'session_id': cart_item.session.id,
                'service_id': cart_item.service.id,
                'web_id': cart_item.web.id if cart_item.web else None,
                # Add other CartItem fields as needed
            })
        return JsonResponse({'cart_items': cart_item_data})
    else:
        return JsonResponse({'error': 'Invalid request method.'})


def booking_confirmation(request, web_slug):
    # Get the last booking object created

    web = WEB.objects.get(slug=web_slug)
    if web.views_confirmation is None:
        web.views_confirmation = 0
    web.views_confirmation += 1
    web.save()
    booking = Appointment.objects.last()

    # Render the booking confirmation template with the booking ID and web slug
    return render(request, 'booking_confirmation.html', {'booking': booking, 'web': web})
