
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'admin'
        EMPLOYEE = "EMPLOYEE", "employee"
        MANAGER = "MANAGER", "manager"
        Hospital = "Hospital", "hospital"



    role = models.CharField(max_length=50, help_text='This is role user in system', choices=Role.choices)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
 
    set_role = Role.ADMIN

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def is_admin(self):
        return self.role == self.Role.ADMIN

    def is_manager(self):
        return self.role == self.Role.MANAGER

    def is_employee(self):
        return self.role == self.Role.EMPLOYEE

    def is_Hospital(self):
        return self.role == self.Role.Hospital


    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.role == User.Role.ADMIN:
                self.role = self.set_role
            return super().save(*args, **kwargs)
        return super().save(*args, **kwargs)






class managerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role="MANAGER")


class Manager(User):
    set_role = User.Role.MANAGER
    REQUIRED_FIELDS = ['username']
    companies = managerManager()

    class Meta:
        proxy = True





class HospitalManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role="Hospital")


class Hospital(User):
    set_role = User.Role.Hospital
    REQUIRED_FIELDS = ['username']
    companies = HospitalManager()

    class Meta:
        proxy = True


class EmployeeManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role="EMPLOYEE")


class Employee(User):
    set_role = User.Role.EMPLOYEE
    employees = EmployeeManager()

    class Meta:
        proxy = True
