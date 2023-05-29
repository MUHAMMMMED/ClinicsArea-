from django import forms
from webs.models import *
 

class  booking(forms.ModelForm):



      class Meta:
           model = Appointment
           fields = "__all__"
           # fields = ('name','phone', 'knew','Message')
           # exclude = ['STATUS','created_at',  ]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Appointment
        # fields = "__all__"
        fields = ('name','phone','knew_from','note' )
        exclude = ['web','service','status_appointment',  ]
        widgets = {
            'note': forms.Textarea(attrs={'rows': 5}),
        }
