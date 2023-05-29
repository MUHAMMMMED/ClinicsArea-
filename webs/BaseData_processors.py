#
# from django.shortcuts import render, get_object_or_404
#
#
# from django.shortcuts import render, get_object_or_404
# from webs.models import *
#
# def categories_s(request, web_slug):
#     # Get the web object for the current request
#     web = get_object_or_404(WEB, slug=web_slug)
#
#     # Get all Categories objects for the current web object
#     categories = Categories.objects.filter(web=web)
#
#
#
#     context = {
#      'cat': categories,
#   }
#     return context
from django.shortcuts import render, get_object_or_404
from .models import WEB, Categories

from django.shortcuts import render, get_object_or_404
from .models import Categories, WEB

# def get_category_services(request, web_slug):
#     # Get the web object for the current request
#     web = get_object_or_404(WEB, slug=web_slug)
#
#     # Get all Categories objects for the current web object
#     cat = Categories.objects.filter(web=web)
#
#     # Create a dictionary to store the categories and their related services
#     category_services = {}
#
#
#     context = {
#      'cat': cat, }
#
#     return context
