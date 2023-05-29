# templatetags/custom_filters.py

# from django import template
# from datetime import datetime
# import calendar
#
# register = template.Library()
#
# @register.filter(name='month_name')
# def month_name(month_number):
#     return datetime.strptime(str(month_number), '%m').strftime('%B')
#
#
# register = template.Library()
# @register.filter(name='calendar')
# def calendar_format(value):
#     return calendar.monthcalendar(value.year, value.month)
#
#
# register = template.Library()
# @register.filter(name='calendar')
# def calendar(value):
#     return value
from django import template

register = template.Library()

@register.filter
def key(d, key_name):
    return d.get(key_name)
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

from django import template

register = template.Library()

@register.filter
def day(queryset, day):
    return queryset.filter(date__day=day)
from django import template

register = template.Library()

@register.filter
def day(queryset, day):
    return queryset.filter(date__day=day)




from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
