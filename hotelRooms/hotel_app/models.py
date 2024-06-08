from django.contrib.auth.models import User
from django.db import models
from django.forms import IntegerField, BooleanField, CharField, ImageField


# Create your models here.
class Employee(models.Model):
    EMPLOYEE_CHOICES = (
        ("M", "M"),
        ("R", "R"),
        ("H", "H")
    )

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    description = models.TextField()
    year = models.IntegerField()
    employee_type = models.CharField(max_length=1, choices=EMPLOYEE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Room(models.Model):
    number = models.IntegerField()
    numberOfBeds = models.IntegerField()
    has_terace = models.BooleanField()
    is_clean = models.BooleanField()

    def __str__(self):
        return f"{self.number} {self.numberOfBeds}"

class EmployeeRooom(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

class Reservation(models.Model):
    code = models.CharField(max_length=4)
    date_from = models.DateField()
    date_to = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_confirmed = models.BooleanField()
    receptionist = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} {self.room.number}"
