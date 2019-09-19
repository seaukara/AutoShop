from django.contrib import admin
from .models import User, Appointment


class UserAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Email', {'fields': ['user_email']}),
        ('First name', {'fields': ['user_fname']}),
        ('Last name', {'fields': ['user_lname']}),
        ('Phone', {'fields': ['user_phone']}),
        ('Car Year', {'fields': ['user_year']}),
        ('Car Make', {'fields': ['user_make']}),
        ('Car Model', {'fields': ['user_model']}),
    ]

    list_display = ('user_email', 'user_fname', 'user_lname', 'user_phone',
                    'user_year', 'user_make', 'user_year')
    list_filter = ['user_email']
    search_fields = ['user_email']


class AppointmentAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Email', {'fields': ['apt_email']}),
        ('Appointment', {'fields': ['apt_pref']}),
        ('Description', {'fields': ['apt_type']}),
        ('IP', {'fields': ['apt_ip']})
    ]

    list_display = ('apt_email', 'apt_pref', 'apt_type', 'apt_ip')
    list_filter = ['apt_email']
    search_fields = ['apt_email']


admin.site.register(User, UserAdmin)
admin.site.register(Appointment, AppointmentAdmin)

