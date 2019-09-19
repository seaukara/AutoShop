from django.db import models

class User(models.Model):
    user_email = models.CharField(max_length=200)
    user_fname = models.CharField(max_length=100)
    user_lname = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=20)
    user_year = models.IntegerField(default=2019)
    user_make = models.CharField(max_length=20)
    user_model = models.CharField(max_length=20)

    def __str__(self):
        return self.user_email

class Appointment(models.Model):
    apt_email = models.ForeignKey(User, on_delete=models.CASCADE)
    apt_pref = models.DateTimeField('Preferred Appointment Time')
    apt_type = models.CharField(max_length=200)
    apt_ip = models.GenericIPAddressField(null=True)

    def __str__(self):
        return self.apt_email
