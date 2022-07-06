from django.contrib import admin
from mysite.models import booking


# Register your models here.
class Booking(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'email_address', 'phone', 'address', 'zip_code', 'message')

admin.site.register(booking, Booking)