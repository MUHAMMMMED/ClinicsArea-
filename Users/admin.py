from django.contrib import admin

from Users.models  import *
# Register your models here.

 
admin.site.register(User )

admin.site.register(Manager)
admin.site.register(Employee)
admin.site.register(Hospital)
# admin.site.register(Patient)
