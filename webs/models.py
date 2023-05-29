from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from Users.models import *





# models.py

from django.db import models
from django.contrib.sessions.models import Session


class WEB(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    Employee_WEB = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee', blank=True, null=True)
    active = models.BooleanField(default=False)
    slug = models.CharField(max_length=50, unique=True, blank=True, null=True)
    FaviconIco= models.FileField(upload_to = "files/images/WEB/FaviconIco/%Y/%m/%d/",blank=True, null=True)
    logo = models.FileField(upload_to = "files/images/WEB/logo/%Y/%m/%d/",blank=True, null=True)
    keywords= models.CharField(max_length = 300,blank=True, null=True)
    pixal_id= models.CharField(max_length=500,blank=True, null=True)
    Title = models.CharField(max_length=100,blank=True, null=True)
    Title_logo = models.FileField(upload_to = "files/images/WEB/Title_logo/%Y/%m/%d/",blank=True, null=True)
    silderImage = models.FileField(upload_to = "files/images/WEB/silderImage/%Y/%m/%d/",blank=True, null=True)
    info = models.CharField(max_length = 300 ,blank=True, null=True)
    Description= models.CharField(max_length = 300 ,blank=True, null=True)
    PHONE = models.CharField(max_length = 300 ,blank=True, null=True)
    Whatsapp= models.CharField(max_length=500,blank=True, null=True)
    linkedinlinke= models.CharField(max_length=500,blank=True, null=True)
    snapchat= models.CharField(max_length=500,blank=True, null=True)
    instagramlinke= models.CharField(max_length=500,blank=True, null=True)
    Twitterlinke= models.CharField(max_length=500,blank=True, null=True)
    facebooklinke= models.CharField(max_length=500,blank=True, null=True)
    OpeningHours= models.CharField(max_length=500,blank=True, null=True)
    Address= models.CharField(max_length=500,blank=True, null=True)
    Map_Address= models.CharField(max_length=500,blank=True, null=True)
    views = models.IntegerField(default=0,blank=True, null=True)
    views_Categories = models.IntegerField(default=0,blank=True, null=True)
    views_checkout = models.IntegerField(default=0,blank=True, null=True)
    views_confirmation = models.IntegerField(default=0,blank=True, null=True)
    Click_booking= models.IntegerField(default=0,blank=True, null=True)
    Click_whatsapp= models.IntegerField(default=0,blank=True, null=True)
    Click_whatsapp_Categories= models.IntegerField(default=0,blank=True, null=True)

    def __str__(self):
         return self.slug

    def delete(self, *args, **kwargs):
        self.FaviconIco.delete()
        self.logo.delete()
        self.Title_logo.delete()
        self.silderImage.delete()

        super().delete(*args, **kwargs)



class Department(models.Model):
    web=models.ForeignKey(WEB,on_delete=models.CASCADE, related_name='department', blank=True, null=True)
    name = models.CharField(max_length=100)


class Questions(models.Model):
    web = models.ForeignKey(WEB, related_name='qestions', on_delete=models.CASCADE)
    question= models.CharField(max_length = 300 ,blank=True, null=True)
    answer = models.CharField(max_length=300,blank=True, null=True)
    def __str__(self):
         return self.question

#
class Image(models.Model):
   web=models.ForeignKey(WEB,on_delete=models.CASCADE, related_name='image', blank=True, null=True)
   image = models.FileField(upload_to = "files/images/WEB/Image/%Y/%m/%d/",blank=True, null=True)
   imagename = models.CharField(max_length = 300 ,blank=True, null=True)

   def __str__(self):
         return self.imagename

   def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)


#
class Insurance(models.Model):
   web=models.ForeignKey(WEB,on_delete=models.CASCADE, related_name='insurance', blank=True, null=True)
   name = models.CharField(max_length = 300 ,blank=True, null=True)
   def __str__(self):
         return self.name
#
class Section(models.Model):

   web=models.ForeignKey(WEB,on_delete=models.CASCADE, related_name='section', blank=True, null=True)
   name = models.CharField(max_length = 300 ,blank=True, null=True)
   image = models.FileField(upload_to = "files/images/WEB/Section/%Y/%m/%d/",blank=True, null=True)


   def __str__(self):
         return self.name

#
class Doctors(models.Model):
   web=models.ForeignKey(WEB,on_delete=models.CASCADE, related_name='doctors', blank=True, null=True)
   Image = models.FileField(upload_to = "files/images/WEB/Doctors/%Y/%m/%d/",blank=True, null=True)
   Name = models.CharField(max_length = 300 ,blank=True, null=True)
   jobtitle= models.CharField(max_length = 300 ,blank=True, null=True)
#
   def delete(self, *args, **kwargs):
        self.Image.delete()
        super().delete(*args, **kwargs)
#



# __________________________________

class Categories(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    keywords = models.CharField(max_length=300, blank=True, null=True)
    Image = models.FileField(upload_to="files/images/WEB/Categories/%Y/%m/%d/", blank=True, null=True)
    Name = models.CharField(max_length=300, blank=True, null=True)
    web = models.ForeignKey(WEB, on_delete=models.CASCADE, related_name='categories', blank=True, null=True)
    views = models.IntegerField(default=0,blank=True, null=True)
    Click_whatsapp= models.IntegerField(default=0,blank=True, null=True)
    def __str__(self):
        return self.Name
    #
    def delete(self, *args, **kwargs):
        self.Image.delete()
        super().delete(*args, **kwargs)






class Service(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    keywords = models.CharField(max_length=300, blank=True, null=True)
    Image = models.FileField(upload_to="files/images/WEB/Service/%Y/%m/%d/", blank=True, null=True)
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category_id=models.ForeignKey(Categories,on_delete=models.CASCADE, related_name='Services', blank=True, null=True)
    long_image = models.FileField(upload_to = "files/images/WEB/Service/long/%Y/%m/%d/",blank=True, null=True)
    views = models.IntegerField(default=0,blank=True, null=True)
    Click_booking= models.IntegerField(default=0,blank=True, null=True)
    Click_whatsapp= models.IntegerField(default=0,blank=True, null=True)
    #
    # def __str__(self):
    #     return self.Title

    def delete(self, *args, **kwargs):
        self.Image.delete()
        self.long_image.delete()
        super().delete(*args, **kwargs)



#
# class ArticleSeries(models.Model):
#     def image_upload_to(self, instance=None):
#         if instance:
#             return os.path.join("ArticleSeries", slugify(self.slug), instance)
#         return None
#
#     title = models.CharField(max_length=200)
#     subtitle = models.CharField(max_length=200, default="", blank=True)
#     slug = models.SlugField("Series slug", null=False, blank=False, unique=True)
#     published = models.DateTimeField("Date published", default=timezone.now)
#     author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
#     image = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to ,max_length=255)
#
#
#








class CartItem(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    web = models.ForeignKey(WEB, on_delete=models.CASCADE,  blank=True, null=True)






class Appointment(models.Model):

    Undefined = "كيف عرفتنا"
    insurance = 'تأمين'
    Friend = 'صديق '
    family = 'أسرة'
    neighbors = 'الجيران'
    Google = 'جوجل '
    Whatsapp = 'واتساب'
    snapchat = 'سناب'
    Instagram = 'انستقرام'
    Twitter = 'تويتر'
    Facebook = 'فيس بوك '
    ticktock = 'تيك توك'
    YouTube = 'يوتيوب '
    Email = 'البريد الإلكتروني'
    Site = 'موقع'
    other = 'آخر'

    CHOICES_knew = (
        (Undefined, "كيف عرفتنا"),
        (insurance, 'تأمين'),
        (Friend, 'صديق '),
        (family, 'أسرة'),
        (neighbors, 'الجيران'),
        (Google, 'جوجل '),
        (Whatsapp, 'واتساب'),
        (snapchat, 'سناب'),
        (Instagram, 'انستقرام'),
        (Twitter, 'تويتر'),
        (Facebook, 'فيس بوك '),
        (ticktock, 'تيك توك'),
        (YouTube, 'يوتيوب '),
        (Email, 'البريد الإلكتروني'),
        (Site, ' موقع الإلكتروني'),
        (other, 'آخر'),
    )

    waiting = 'انتظار'
    Inquiries="الاستفسار"
    notanswering= 'عدم الرد'
    cancel ='إلغاءحجزه'
    confirmed="حجز مؤكد"
    Visit =  'حضر'

    STATUS_CHOICES = (('waiting','انتظار'),('inquiries', 'الاستفسار'),('cancel', 'إلغاءحجزه'),('notanswering', 'عدم الرد'),('confirmed', 'حجز مؤكد'),    ('visit', 'حضر'),)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    service=models.ManyToManyField(Service,blank=True)
    web = models.ForeignKey(WEB, on_delete=models.CASCADE, blank=True, null=True)
    knew_from = models.CharField(max_length=50, choices=CHOICES_knew, blank=True, null=True)
    status_appointment =models.CharField(max_length=30, choices=STATUS_CHOICES , default=waiting)
    note = models.CharField(max_length=500, blank=True, null=True)
