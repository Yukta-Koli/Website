
from django.forms import ModelForm
from .models import booking


# Create a venue form
class Booking(ModelForm):
    class Meta:
        model = booking
        fields = ('first_name', 'last_name', 'email_address', 'phone', 'address', 'zip_code', 'message')

