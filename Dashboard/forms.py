from django import forms
from webs.models import *

class WebForm(forms.ModelForm):
    class Meta:
        model = WEB
        fields = "__all__"
        exclude = ['Employee_WEB' ,'views','views_Categories','views_checkout','views_checkout','views_confirmation','Click_booking','Click_whatsapp','Click_whatsapp_Categories']


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = ['Name', 'jobtitle', 'Image']


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name','image']



class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = ['name']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'imagename']


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['question', 'answer']
        widgets = {
        'question': forms.Textarea(attrs={'rows': 5}),
         'answer': forms.Textarea(attrs={'rows': 5}),
         }





class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']




class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"
        exclude =['views','web' ]


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('active', 'Title', 'Description', 'Image', 'price',  'keywords','long_image')
        exclude =['views','Click_booking','Click_whatsapp']
        labels = {
            'active': 'Active',
            'Title': 'My Field Label',
            'Image': 'Image',
            'price': 'Price',
            'long_image':'Image',
            # 'category_id': 'Category ID',
        }
        widgets = {
            'Description': forms.Textarea(attrs={'rows': 5}),
            'keywords': forms.TextInput(attrs={'placeholder': 'e.g. keyword1, keyword2, keyword3','rows': 5}),
        }




class upServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('active', 'Title', 'Description', 'Image', 'price',  'keywords','category_id','long_image')
        exclude = ['views','Click_booking','Click_whatsapp']
        labels = {
            'active': 'Active',
            'Title': 'My Field Label',
            'Image': 'Image',
            'price': 'Price',
            'long_image':'Image',
            # 'category_id': 'Category ID',
        }
        widgets = {
            'Description': forms.Textarea(attrs={'rows': 5}),
            'keywords': forms.TextInput(attrs={'placeholder': 'e.g. keyword1, keyword2, keyword3'}),
        }
