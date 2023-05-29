import django_filters

from webs.models import *
class BookingFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Appointment
        # fields = "__all__"
        fields = ('name','phone'   )
