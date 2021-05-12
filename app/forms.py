from django.forms import ModelForm
from app.models import Stores


# Create the form class.
class StoresForm(ModelForm):
    class Meta:
        model = Stores
        fields = ['name', 'storeName', 'address', 'district', 'city','state', 'phone']
