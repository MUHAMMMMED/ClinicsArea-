



from django.contrib import admin
from django.urls import path
from  webs.views  import *
from django.conf.urls.static import static
from django.conf import settings
app_name='webs'
urlpatterns = [
 path('',home, name="home"),

  path('<slug:web_slug>/',  web, name='web'),

  path('<slug:web_slug>/categories/<int:id>/', categories, name='categories'),

  path('services/<int:id>/', services, name="service"),

  path('add-to-cart/<int:id>/', add_to_cart, name='add_to_cart'),

  path('<slug:web_slug>/cart_and_checkout/', cart_and_checkout, name='cart_and_checkout'),

  path('<slug:web_slug>/category/<int:category_id>/service/<int:service_id>/', services, name='service'),
    # ... other URL patterns ...
  path('booking_confirmation/<slug:web_slug>/',  booking_confirmation, name='booking_confirmation'),
    # other URL patterns ...
  path('<slug:web_slug>/categories-services/', categories_services, name='categories_services'),
    # other URL patterns ...
    # other URL patterns here
  path('cart-item/refresh/', cart_item_refresh_view, name='cart_item_refresh'),


  path('cart-item/delete/', cart_item_delete_view, name='cart_item_delete'),


  path('category/<int:category_id>/increment_click_whatsapp/', increment_click_category_whatsapp, name='increment_click_category_whatsapp'),

  path('categories/<slug:web_slug>/increment_web_categoryclick_whatsapp/', increment_click_web_category_whatsapp, name='increment_click_web_category_whatsapp'),

  path('web/<slug:web_slug>/increment_click_web_whatsapp/', increment_click_web_whatsapp, name='increment_click_web_whatsapp'),
  path('services/<int:service_id>/increment_click_whatsapp/',  increment_click_whatsapp, name='increment_click_whatsapp'),





]
