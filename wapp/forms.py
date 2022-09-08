from .models import City
from django.forms import ModelForm

class CityForm(ModelForm):
	class Meta:
		model = City
		fields = ['name_of_city']

	def __init__(self, *args, **kwargs):
		super(CityForm, self).__init__(*args, **kwargs)

		for name, field in self.fields.items():
			field.widget.attrs.update({'class': 'input', 'placeholder': 'City Name'})