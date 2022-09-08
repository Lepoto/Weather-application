import requests
from django.shortcuts import render,redirect
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=e66f15a50621735d2ef508a405db3a13'

	err_msg = ''

	if request.method == 'POST':
		city_form = CityForm(request.POST)

		if city_form.is_valid():
			new_city = city_form.cleaned_data['name_of_city']
			existing = City.objects.filter(name_of_city=new_city).count()

			if existing == 0:
			    res = requests.get(url.format(new_city)).json()

			    if res['cod'] == 200:
			        city_form.save()
			    else:
			    	err_msg = 'City does not exist!'
			else:
				err_msg = 'City already exist'

	message = ''
	message_class = ''

	if err_msg:
		message = err_msg
		message_class = 'is-danger'
	else:
		message = ''
		message_class = ''

	city_form = CityForm()


	cities = City.objects.all()
	weather_data_city = []

	for city in cities:

	    res = requests.get(url.format(city)).json()

	    city_weather = {
            'city': city.name_of_city,
            'temperature': res['main']['temp'],
            'description': res['weather'][0]['description'],
            'icon': res['weather'][0]['icon'],
            'country': res['sys']['country'],
	    }

	    weather_data_city.append(city_weather)
	    #print(weather_data_city)

	context = {
	    'weather_data': weather_data_city,
	    'city': city_form,
	    'message': message,
	    'message_class': message_class,
	    }

	return render(request, 'wapp/weather.html', context)

def deleteview(request, name_of_city):
	City.objects.get(name_of_city=name_of_city).delete()

	return redirect('index')